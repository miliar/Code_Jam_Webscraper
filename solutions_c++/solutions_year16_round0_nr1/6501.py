//Done by: K Ashwin

#include<bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;

#define REP(i, a, b) \
for (int i = int(a); i <= int(b); i++) // a to b, and variable i is local!
#define TR(c, it) \
for (auto it = (c).begin(); it != (c).end(); it++)

#define s(x) scanf("%d", &x)
#define sl(x) scanf("%lld", &x)
#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define set0(a) memset(a, 0, sizeof(a))
#define setdp(a) memset(a, -1, sizeof(a))
#define INF 2000000000
#define MOD 1000000007

bool has[15];

void conv(int x)
{
    while (x) {
        has[x % 10] = 1;
        x /= 10;
    }
}

bool check()
{
    for (int i = 0; i <= 9; i++) {
        if (!has[i])
            return 0;
    }

    return 1;
}

int main()
{
    int t, n, tmp;

    freopen("inp.txt", "r", stdin);
    freopen("op.txt", "w", stdout);

    s(t);

    int tt = 0;
    while (t--) {
        ++tt;

        s(n);
        //n = tt;

        if (n == 0) {
            printf("Case #%d: INSOMNIA\n", tt);

            continue ;
        }

        set0(has);

        tmp = n;
        while (1) {
            conv(n);

            if (check()) {
                printf("Case #%d: %d\n", tt, n);

                break ;
            }

            n += tmp;
        }
    }

    return 0;
}
