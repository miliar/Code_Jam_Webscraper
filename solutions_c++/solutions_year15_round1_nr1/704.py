// RandomUsername (Nikola Jovanovic)
// Google Code Jam 2015
// Round 1A
// A

#include <bits/stdc++.h>
#define MAXN 1005
#define lld long long
#define ff(i,a,b) for(int i=a; i<=b; i++)
#define fb(i,a,b) for(int i=a; i>=b; i--)
#define par pair<int, int>
#define fi first
#define se second
#define mid (l+r)/2

using namespace std;

int n, m, t;
int a[MAXN];
int maksdiff = 0;
int ret1;
int ret2;

int main()
{
    freopen("Ain.txt","r",stdin);
    freopen("Aout.txt", "w", stdout);

    scanf("%d", &t);
    for(int tt=1; tt<=t; tt++)
    {
        maksdiff = 0;
        ret1 = 0;
        ret2 = 0;
        scanf("%d", &n);
        ff(i, 1, n)
        {
            scanf("%d", &a[i]);
        }
        ff(i, 2, n)
        {
            if(a[i-1] - a[i] > 0)
            {
                ret1 += a[i-1] - a[i];
                maksdiff = max(maksdiff, a[i-1] - a[i]);
            }
        }
        ff(i, 2, n)
        {
                ret2 += min(a[i-1], maksdiff);
        }
        //imamo sve
        printf("Case #%d: %d %d\n", tt, ret1, ret2);
    }
    return 0;
}
