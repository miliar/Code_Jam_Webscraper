#include<iostream>
#include<fstream>
using namespace std;
const int maxlongint=(1<<31)-1;
int t,o,ans,i,j,n,k;
int a[2000];
int main()
{
    //freopen("1.in","r",stdin);
    //freopen("1.out","w",stdout);
    cin>>t;
    for (int o=1;o<=t;o++)
    {
        ans=maxlongint;
        cin>>n;
        for (i=1;i<=n;i++)cin>>a[i];
        for (i=1;i<=1100;i++)
        {
            k=i;
            for (j=1;j<=n;j++)k+=(a[j]-1)/i;
            ans=min(ans,k);
        }
        cout<<"Case #"<<o<<": "<<ans<<endl;
    }
}
