#include <bits/stdc++.h>
#define ll long long int

using namespace std;
int isP(ll n){
    ll i;

    if (n==2)
        return 1;

    if (n%2==0)
        return 0;
     //   if(1==0)
//cout<<"Check";
    for (i=2;i<=sqrt(n);i++)
        if (n%i==0)
            return 0;
//     if(1==0)
//cout<<"Check";
    return 1;
}

void generate(int n,ll jj)
{
    // base case
    if (n <= 0)
        return;
 
    //    if(1==0)
//cout<<"Check";
    vector<string> arr;
 
    arr.push_back("0");
    arr.push_back("1");
 
    ll i, j;
    string br[68000];
    for (i = 2; i < (1<<n); i = i<<1)
    {
        
        for (j = i-1 ; j >= 0 ; j--)
            arr.push_back(arr[j]);
 
       
        for (j = 0 ; j < i ; j++)
            arr[j] = "0" + arr[j];
 
      
        for (j = i ; j < 2*i ; j++)
            arr[j] = "1" + arr[j];
    }
    int first=0;
    int sec,c,flag=0;
    ll k,sum,t;
    ll cr[10000][10];
    j=0;
    for (i = 0 ; i < arr.size() ; i++ )
    {
        if(arr[i][0]==arr[i][n-1] && arr[i][0]=='1')
        {
            c=1;
            sec=0;
            for(int d=2;d<=10;d++)
            {
            sum=0;
            k=1;
             //    if(1==0)
//cout<<"Check";
            for(int m=n-1;m>=0;m--)
            {
                if(arr[i][m]=='1')
                {
                sum+=k;
                }
                else
                sum+=0;
                k=k*d;
            }
         //    if(1==0)
//cout<<"Check";
            if(isP(sum)==1)
            {
            flag=1;
        
            break;
            }
            else
            {
        
                c++; 
            for(t=2;t<=sum;t++)
            {
               
                if(sum%t==0)
                {
                 
                cr[first][sec++]=t;
                
                break;
                }
            }
                    if(c==10)
                {
        
                        j++;
    
                        br[first]=arr[i];
                        first++;
                        if(j==jj)
                            break;
    }
        }
    
            
        }
    
        if(j==jj)
        break;
        }
    
    }
    for(i=0;i<jj;i++)
    {
        cout<<br[i]<<" ";
        for(j=0;j<9;j++)
        cout<<cr[i][j]<<" ";
        cout<<"\n";
    }
    }
 
int main()
{
    int n,t;
    ll jj;
    cin>>t;
    cin>>n>>jj;
    cout<<"Case #1:\n";
    generate(n,jj);
    return 0;
}