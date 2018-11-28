#include <iostream>
#include <cstring>
#include <cstdio>
#include <cmath>
#define prt(k) cout<<#k" = "<<k<<endl;
using namespace std;
typedef long long ll;
const int N = 2333;
int a[N];
int n;
#include <queue>
#include <algorithm>

int b[N], c[N];
int ans;


int main()
{
    freopen("B.in","r",stdin); freopen("B.out","w",stdout);
    int re, ca=1;
    cin>>re;
    while (re--)
    {
        cin>>n;
        int ma = 0;
        for (int i=1;i<=n;i++)
            scanf("%d", a+i), ma=max(ma, a[i]);
        sort(a+1, a+n+1);
        reverse(a+1, a+n+1);
        ans = ma;
        for (int k=1;k<=ma;k++)
        {
            int tmp = 0;
            for (int i=1;i<=n;i++)
            {
                if (a[i]<=k)
                {
                    continue;
                }
                else tmp += (a[i]+k-1)/k - 1;
            }
            ans = min(ans, k+tmp);
        }
        printf("Case #%d: %d\n", ca++, ans);
    }

    return 0;
}
/**
34
1
3
4
1 2 1 2
1
4
1
9
3
3 3 3

*/
