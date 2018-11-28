//.RandomUsername (Nikola Jovanovic)
//Google Code Jam 2015
//Qualification Round
//B

#include <bits/stdc++.h>
#define MAXN 1005
#define lld long long
#define ff(i,a,b) for(int i=a; i<=b; i++)
#define fb(i,a,b) for(int i=a; i>=b; i--)
#define par pair<int, int>
#define fi first
#define se second
#define mid (l+r)/2
#define INF 1000000000LL

using namespace std;

int t;
int p[MAXN];
int n;
int maks;
int mint;
int tim;

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d", &t);
    for(int tt=1; tt<=t; tt++)
    {
        scanf("%d", &n);
        maks = -1;
        ff(i, 1, n)
        {
            scanf("%d", &p[i]);
            maks = max(maks, p[i]);
        }
        mint = INF;
        ff(ks, 1, maks)
        {
            tim = ks;
            ff(i, 1, n)
            {
                tim += (p[i] - 1) / ks;
            }
            mint = min(mint, tim);
        }
        printf("Case #%d: %d\n", tt, mint);
    }
    return 0;
}
