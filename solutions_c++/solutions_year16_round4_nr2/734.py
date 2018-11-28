// RandomUsername (Nikola Jovanovic)
// GCJ 2016 R2
// B

#include <bits/stdc++.h>
#define DBG false
#define debug(x) if(DBG) printf("(ln %d) %s = %d\n", __LINE__, #x, x);
#define lld long long
#define ff(i,a,b) for(int i=a; i<=b; i++)
#define fb(i,a,b) for(int i=a; i>=b; i--)
#define par pair<int, int>
#define fi first
#define se second
#define mid (l+r)/2
#define INF 1000000000
#define MAXN 205
#define DIS 200

using namespace std;

int t, n, k;
double p[MAXN];
double DP[MAXN][MAXN][2*MAXN];

int main()
{
    freopen("B2.in", "r", stdin);
    freopen("B2.out", "w", stdout);
    scanf("%d", &t);
    ff(tt, 1, t)
    {
        fprintf(stderr, "CAO %d %d\n", t, tt);
        scanf("%d %d", &n, &k);
        ff(i, 0, n-1)
            scanf("%lf", &p[i]);
        int MASKS = (1 << n);
        double ret = 0.0;
        ff(MASK, 0, MASKS - 1)
        {
            if(__builtin_popcount(MASK) != k) continue;
            // we picked k, we have our group, calc prob
            double prob_tie = 1.0;
            double CURR = 0.0;
            int MASKS2 = (1 << k);
            // every voting scenario possible, add them all up
            ff(MASK2, 0, MASKS2 - 1)
            {
                prob_tie = 1.0;
                int it = 0; // mask2 pointer, does he vote yes or no?
                int balance = 0;
                ff(bit, 0, n - 1)
                {
                    if( (MASK & (1 << bit)) == 0 ) continue; // not voting
                    // voting!
                    if( (MASK2 & (1 << it)) == 0 )
                    {
                        // voting no
                        balance--;
                        prob_tie *= (1 - p[bit]);
                    }
                    else
                    {
                        // voting yes
                        balance++;
                        prob_tie *= p[bit];
                    }
                    it++;
                }
                if(balance == 0) CURR += prob_tie;
            }
            // found new best?
            ret = max(ret, CURR);
        }
        printf("Case #%d: %0.7f\n", tt, ret);
    }
    return 0;
}
