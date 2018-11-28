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
        string s; in >> s;
        int cnt = 0;
        REPV(i, s.size()-1, 0)
        {
            if(s[i] == '-')
            {
                cnt++;
                REP(j, i+1) s[j] = (s[j] == '+') ? '-' : '+';
            }
        } //out << s << "\n";

        printf("Case #%d: %d\n", _TC, cnt);
    }

    return 0;
}
