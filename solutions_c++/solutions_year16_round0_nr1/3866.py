#include <bits/stdc++.h>
using namespace std;

#define in cin
#define out cout

#define REP(i,n) for(int i=0; i<n; i++)
#define REPE(i,s,e) for(int i=s; i<=e; i++)
#define REPV(i,s,e) for(int i=s; i>=e; i--)

#define all(v) v.begin(), v.end()
#define pb push_back
#define isin(a,b,c) ((a)<=(c)&&(c)<=(b))
#define maxn(a,b) ((a)>(b)?(a):(b))
#define minn(a,b) ((a)<(b)?(a):(b))

#define ll long long
#define pii pair<int, int>
#define pll pair<ll, ll>
#define pdd pair<double, double>

#define X first
#define Y second
#define intINF 2147483647
#define llINF 9223372036854775807LL
#define PI 3.1415926535897
#define MOD 1000000007

int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

    int tc; in >> tc;
    REPE(_TC, 1, tc)
    {
        ll n; in >> n;
        if(n == 0)
        {
            printf("Case #%d: INSOMNIA\n", _TC);
            continue;
        }

        int ck[10];
        REP(i, 10) ck[i] = 0;
        REP(i, 10000)
        {
            ll t = n*i;
            while(t)
            {
                ck[t % 10] = 1;
                t /= 10;
            }

            bool f = true;
            REP(j, 10) if(ck[j] == 0) f = false;

            if(f)
            {
                printf("Case #%d: %lld\n", _TC, n*i);
                break;
            }
        }
    }

    return 0;
}
