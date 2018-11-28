#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
const int maxn=113;
double a[maxn];
double b[maxn];
int hash[maxn];
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    int n;
    scanf("%d",&t);
    int cas=1;
    while(t--)
    {
        scanf("%d",&n);
        for(int i=0;i<n;i++)
        {
            scanf("%lf",&a[i]);
        }
        for(int i=0;i<n;i++)
        {
            scanf("%lf",&b[i]);
        }
        sort(a,a+n);
        sort(b,b+n);
        int ans=0;
        memset(hash,-1,sizeof(hash));
        for(int i=0;i<n;i++)
            for(int j=0;j<n;j++)
            {
                if(a[j]>b[i]&&(hash[j]==-1))
                {
                //  cout<<a[j]<<endl;
                    ans++;
                    hash[j]=1;
                    break;
                }
            }
          //  cout<<ans<<endl;
            memset(hash,-1,sizeof(hash));
        int ans1=0;
        for(int i=0;i<n;i++)
            for(int j=0;j<n;j++)
            {
                if(b[j]>a[i]&&(hash[j]==-1))
                {
                    ans1++;
                    hash[j]=1;
                    break;
                }
            }
        printf("Case #%d: %d %d\n",cas++,ans,n-ans1);
    }
    return 0;
}
