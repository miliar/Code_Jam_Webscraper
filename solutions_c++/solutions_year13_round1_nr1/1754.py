#include<iostream>
using namespace std;
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    long long int z=1;
    cin>>t;
    while(t--)
    {
     long long int r,n,sum=0,count=0;
     cin>>r>>n;
     sum=2*r+1;
     xy:
     if(sum<=n)
     {
      r=r+2;count++;
      sum+=2*r+1;
      goto xy;          
     }  
     else
     {
      cout<<"Case #"<<z++<<": "<<count<<endl;    
     }        
    }
 return 0;    
}
