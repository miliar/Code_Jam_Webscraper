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

void foo(string s, int dep, int g)
{
    if(dep == 0)
    {
        if(g) REP(i, s.size()) out << "G";
        else out << s;
        return;
    }
    REP(i, s.size())
    {
        if(s[i] == 'G') foo(s, dep-1, 1);
        else foo(s, dep-1, 0);
    }
    return;
}

int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

    int tc; in >> tc;
    REPE(_TC, 1, tc)
    {
        printf("Case #%d: ", _TC);
        int k, c, s; in >> k >> c >> s;

        if(k == 1)
        {
            printf("1\n");
        }
        else if(c == 1)
        {
            if(k <= s) REP(i, k) printf("%d ", i+1);
            else printf("IMPOSSIBLE");
            printf("\n");
        }
        else if((k+1)/2 > s)
        {
            printf("IMPOSSIBLE\n");
        }
        else
        {
            int a = 0;
            int b = 2;

            REP(i, (k+1)/2)
            {
                printf("%d ", a+b);
                a += 2*k;
                b += 2; if(b > k) b = k;
            }
            printf("\n");
        }
    }

    return 0;
}
