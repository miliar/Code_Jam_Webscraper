#include<iostream>
using namespace std;
int main()
{
    int t,w,r,c,i,ans;
    cin>>t;
    for(i=1;i<=t;i++)
    {
        cin>>r>>c>>w;
        ans=((c+w-1)/w);
        ans+=((r-1)*(c/w));
        cout<<"Case #"<<i<<": "<<ans+w-1<<endl;
    }
}