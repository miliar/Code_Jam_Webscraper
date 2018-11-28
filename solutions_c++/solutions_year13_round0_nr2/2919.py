#include <iostream>
#include <string.h>
#include <cstdio>
#include <map>
#include <set>
#include <vector>
#include <queue>
#include <stack>
#include <algorithm>
#include <cstdlib>
#include <limits.h>
#include <vector>
#include <string>
#include <ctype.h>
#include <complex>
#include <cmath>
using namespace             std;
const int                   Maxn=600,Maxm=2500000,Mo=1000000007,oo=INT_MAX;
struct F {
    int c1,c2,b;
};
int                         n,m,cs,ck;
int                         a[Maxn][Maxn],l[Maxn],r[Maxn];
int main()
{
    ios::sync_with_stdio(0);
    freopen("B-large (1).in","r",stdin);
    freopen("1.out","w",stdout);
    cin>>cs;
    int tt=0;
    while (cs--)
    {
        ck=0;
        memset(l, 0, sizeof(l));
        memset(r, 0, sizeof(r));
        cout<<"Case #"<<++tt<<": ";
        cin>>n>>m;
        for(int i=1;i<=n;i++)
            for (int j=1;j<=m;j++) cin>>a[i][j];
        for (int i=1;i<=n;i++)
            for (int j=1;j<=m;j++)
            {
                l[i]=max(l[i],a[i][j]);
                r[j]=max(r[j],a[i][j]);
            }
        for (int i=1;i<=n;i++)
            for (int j=1;j<=m;j++)
                ck=ck||(a[i][j]<l[i]&&a[i][j]<r[j]);
        if (!ck) cout<<"YES\n";
        else cout<<"NO\n";
    }
}
