// RandomUsername (Nikola Jovanovic)
// GCJ 2016 Q
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
#define INF 2000000000
#define MAXT 105
#define MAXLEN 10000005
#define EPS 1e-6
#define MAXN 150

using namespace std;

char s[MAXN];
int t;

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("b.out", "w", stdout);
    scanf("%lld", &t);
    ff(tt, 1, t)
    {
        scanf("%s", s);
        int len = strlen(s);
        char state = '+';
        int ret = 0;
        fb(i, len-1, 0)
        {
            if(s[i] != state)
            {
                ret++;
                if(state == '-') state = '+';
                else state = '-';
            }
        }
        printf("Case #%d: %d\n", tt, ret);
    }
    return 0;
}
