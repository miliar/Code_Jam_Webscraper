#include<bits/stdc++.h>
using namespace std;
long long int powers[11][18];
long long int aux[12];
long long int aux2[12];
void solve()
{
    
    for(int i = 2; i<= 10; i++)
    {
        for(int j=0;j<=16;j++)
            {   
                if(j==0)
                powers[i][j]=1;
                
                else
                powers[i][j]=i*powers[i][j-1];
                
            }
        
        
    }
}

long long int check_prime(long long int x)
{  if(x==2||x==3||x==5||x==7)
return 0;
    
    for(long long int i = 2; i<= sqrt(x)+1; i++)
    {
        if(x%i==0)
            return i;
        
    }
        
    return 0;
}

int main()
{   
    solve();
    int t,n,maxcount;
    freopen("C-small-attempt2.in","r",stdin);
    freopen("coin-jam-3.out","w",stdout);
    cin>>t>>n>>maxcount;
    int finalcount=0;
    cout<<"Case "<<"#1:"<<endl;
    long long int b = (1<<n);
    int bin[18]={0};
    for(long long int k = 2; k<=b; k++)
    {   int count = 0;
        long long int d = k;
        int s = 0;
        while(d>0)
        {
            bin[s++]=d%2;
            d=d/2;
        }
        if(bin[15]==1&&bin[0]==1)
        {
            for(int j = 2; j<= 10; j++)
        {    
            for(int q = 0; q<= s-1; q++)
            {
            aux[j]= aux[j]+ (bin[q]*powers[j][q]); 
            }
            
            long long int dest = check_prime(aux[j]);
            if(dest!=0&&dest!=aux[j]&&bin[0]==1&&bin[s-1]==1)
            {count++;
             aux2[j]=dest;
            }
            
            else
               break;
                
        }
        
        if(count==9)
        {
           for(int c = s-1; c>=0; c--)
                cout<<bin[c];
           
           cout<<" ";
                    
           for(int l = 2; l<= 10; l++)
            cout<<aux2[l]<<" ";
            
            cout<<endl;
            
            finalcount++;
        
        }
        
        for(int i = 0; i<=11; i++)
        {
            aux[i]=0;
            aux2[i]=0;
        }
        
        for(int i = 0; i<= 17; i++)
            bin[i]=0;
        
       if(finalcount==maxcount)
            break;
        }
        
        
    }
    
   // cout<<endl<<endl<<finalcount;
    
    return 0;
}
