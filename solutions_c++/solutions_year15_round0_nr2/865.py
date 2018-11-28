#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <map>
#include <queue>
#include <cmath>
#include <vector>
#include <string>
#include <iomanip>
#define Mod (1000000007LL)
#define eps (1e-12)
#define Pi (acos(-1.0))
using namespace std;
int n;
int ans,tmp;
int p[1100];
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int T,cas=0;
    scanf("%d",&T);
    while(T--)
    {
        scanf("%d",&n);
        for(int i=0;i<n;i++)
        scanf("%d",&p[i]);
        sort(p,p+n);
        ans = p[n-1];
        //printf("%d\n",ans);
        for(int i=1;i<ans;i++)
        {
            tmp = 0;
            for(int j=0;j<n;j++)
            {
                tmp += (p[j]-1)/i;
            }
            ans = min(ans,tmp+i);
        }
        printf("Case #%d: %d\n",++cas,ans);
    }
    return 0;
}
