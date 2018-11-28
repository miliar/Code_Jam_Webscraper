#include<iostream>
using namespace std;
long long int a[10000001],n=10000000,b[10000001];
long long int palin(long long int x)
{
     long long int y=0,temp=x;
     while(temp){y=(y*10)+(temp%10);temp/=10;}
     if(y==x) return 1;
     return 0;
     }
int main()
{
    for(int i=1;i<=n;i++)
    a[i]=i*i;
    for(int i=1;i<=n;i++)
    {
            if(palin(i)==1 && palin (a[i])==1  )
            b[i]=1;
            else b[i]=0;
            }
    int test,y,x;
    cin>>test;int jkl = 1;
    while(test--)
    {
               cin>>x>>y;
               int ans=0,i=1;
               for(;i<=1000;i++)
               if(a[i]>=x) break;
               for(;a[i]<=y;i++)
             {
                       ans+=b[i];
                       }    
                       cout<<"Case #"<<jkl<<": "<<ans<<endl;
                 jkl++;
                 }
    return 0;
}
