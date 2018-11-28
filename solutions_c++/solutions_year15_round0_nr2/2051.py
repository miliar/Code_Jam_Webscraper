#include<cstdio>
#include<iostream>
#include<queue>
using namespace std;
int n;
int f[1010];
int main()
{
    freopen("bl.in","r",stdin);
    freopen("bl.out","w",stdout);
    int tt;
    cin>>tt;
    for(int ii=1;ii<=tt;ii++)
    {
        cin>>n;
        for(int i=0;i<n;i++)
            cin>>f[i];
        int ans=1000000000;
        for(int t=1;t<=1000;t++)
        {
            int k=0;
            for(int i=0;i<n;i++)
                k+=(f[i]+t-1)/t-1;
            if (k+t<ans)
                ans=k+t;
        }
        cout<<"Case #"<<ii<<": "<<ans<<endl;
    }
    return 0;
}        

