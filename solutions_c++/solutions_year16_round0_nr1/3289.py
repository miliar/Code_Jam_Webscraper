#include<bits/stdc++.h>
using namespace std;

int array[10]={0};

bool check_array()
{
   for(int i = 0; i<= 9;i++)
   {
       if(array[i]==0)
        return 0;
       
   }
    return 1;
}


int main()
{   freopen("A-large.in","r",stdin);
    freopen("A.large.1.out","w",stdout);
    int t;
    cin>>t;
    for(int i = 1; i<= t; i++)
        {
        
        long long int n;
        int flag=1;
        cin>>n;
        if(n==0)
            cout<<"Case "<<"#"<<i<<": "<<"INSOMNIA\n";
        else 
        {  long long int j = 1;
            while(flag==1)
            {
                long long int d = j*n;
                while(d>0)
                {
                    array[d%10]++;
                    d=d/10;
                }
                
                if(check_array())
                {
                cout<<"Case "<<"#"<<i<<": "<<j*n<<endl; 
                flag=0;   
                }
                
                else j++;
                
            }
           
        }
        
        for(int k = 0; k<= 9; k++) array[k]=0;
    }
    return 0;
}
