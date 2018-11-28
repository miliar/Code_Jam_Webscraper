#include <bits/stdc++.h>

#define pb push_back
#define mp make_pair
#define fi first
#define prev asfansjfansjabfasjlbfa
#define se second
#define I "%d"
#define II "%d%d"
#define III "%d%d%d"
#define time afsaGAEgagknlenkawgn
#define out_files freopen("A-large.in", "r", stdin);freopen("output.txt", "w", stdout)

using namespace std;

typedef vector <int> vi;
typedef long long ll;
typedef unsigned long long ull;
typedef pair <int, int> pii;
typedef vector <pii> vii;
typedef vector <vi> vvi;
typedef long double ld;

#ifdef WIN32
    #define I64 "%I64d"
#else
    #define I64 "%lld"
#endif // WIN32

const int inf = (int)1e9;
const ll INF = 1LL*inf*inf;
const double eps = 1e-9;
const int SZ = 1000;
const int md = (int)1e9+7;

int t, use[10], now;
ll n;

void check(ll n)
{
    while (n)
    {
        int k = n%10;
        if (!use[k]) now++, use[k]++;
        n/=10;
    }
}

int main()
{
    out_files;
    scanf(I, &t);
    for (int q=1; q<=t; q++)
    {
        scanf(I64, &n);
        int flag = 0;
        now = 0;
        for (int i=0; i<10; i++)
            use[i] = 0;
        ll k = n;
        for (int i=1; i<1000; i++)
        {
            n = k*i;
            check(n);
            if (now == 10)
            {
                printf("Case #%d: %I64d\n", q, n);
                flag = 1;
                break;
            }
        }
        if (!flag)
            printf("Case #%d: INSOMNIA\n", q);
    }
}
