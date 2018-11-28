/*********By Yu*********/
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <string>
#define OUT(x) cout << #x << ": " << (x) << endl
using namespace std;
typedef long long LL;
const int mmax=1000006;

int n;
double a[1100],b[1100];
bool use[1100];
int main()
{
    freopen("in.in","r",stdin);
    freopen("ans.in","w",stdout);
    int t,i,j;
    scanf("%d",&t);
    int cas=1;
    while(t--)
    {
        memset(use,false,sizeof(use));
        scanf("%d",&n);
        for(i=1;i<=n;i++)
        {
            scanf("%lf",&a[i]);
        }
        for(i=1;i<=n;i++)
        {
            scanf("%lf",&b[i]);
        }
        sort(a+1,a+n+1);
        sort(b+1,b+n+1);
        int ans1=0,ans2=0;
        int ix=n;
        for(i=1;i<=n;i++)
        {
            for(j=1;j<=n;j++)
            {
                if(use[j])
                    continue;
                if(a[i]>b[j])
                {
                    ans1++;
                    use[j]=true;
                }
                else
                {
                    use[ix]=true;
                    ix--;
                }
                break;
            }
        }
        memset(use,false,sizeof(use));
        for(i=1;i<=n;i++)
        {
            for(j=1;j<=n;j++)
            {
                if(use[j])
                    continue;
                if(b[j]>a[i])
                {
                    use[j]=true;
                    break;
                }
            }
            if(j>n)
            {
                ans2++;
                for(j=1;j<=n;j++)
                {
                    if(!use[j])
                    {
                        use[j]=true;
                        break;
                    }
                }
            }
        }
        printf("Case #%d: %d %d\n",cas++,ans1,ans2);
    }
    return 0;
}
