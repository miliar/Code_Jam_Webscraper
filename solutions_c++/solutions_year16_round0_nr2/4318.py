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
#define out_files freopen("B-large.in", "r", stdin);freopen("output.txt", "w", stdout)

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

int t;
string s;

int main()
{
    out_files;
    scanf(I, &t);
    for (int q=1; q<=t; q++)
    {
        cin >> s;
        int n = (int)s.length(), opened = 0, ans = 0;
        for (int i=0; i<n; i++)
            if (s[i] == '-') opened = 1;
            else if (opened) ans += 2, opened = 0;
        if (opened) ans += 2;
        if (s[0] == '-') ans--;
        printf("Case #%d: %d\n", q, ans);
    }
    return 0;
}
