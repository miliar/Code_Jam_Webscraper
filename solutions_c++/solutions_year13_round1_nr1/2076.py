#include<iostream>
#include<cmath>
using namespace std;
int main()
{
    freopen("C:\\Users\\Dell\\Desktop\\input.txt","r",stdin);
    freopen("C:\\Users\\Dell\\Desktop\\output.txt","w",stdout);
    int t,n;
    cin>>n;
    for(t=1;t<=n;t++)
    {
                     double r,t1,pi=3.141,k=0;int cnt=0,i=1;
                     cin>>r>>t1;
                     //r=r/10;
                     //t1=t1/10;
                     while(1)
                     {
                     t1-=((r+i)*(r+i)-(r+k)*(r+k));
                     cnt++;
                     k=k+2;
                     i+=2;
                     if(t1<0)
                     break;
                     }
                     if(cnt==0)
                     cnt=1;
                     cout<<"Case #"<<t<<": "<<cnt-1<<endl;
    }
                     
                     return 0;
}
                     
                     