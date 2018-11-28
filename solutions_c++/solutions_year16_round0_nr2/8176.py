#include <bits/stdc++.h>
#include <time.h>
using namespace std;

#define space " "
#define enter "\n"
#define fi first
#define se second
#define mp make_pair
#define input(s)\
    freopen(s,"r",stdin)
#define output(s)\
    freopen(s,"w",stdout)
#define INF 2000000007
#define LINF 40000000000000000007
#define PI 3.14159265359

typedef long long ll;
typedef unsigned long long ull;
typedef pair <ll, ll> pll;
typedef long double ld;
typedef pair <int, int> pii;
typedef vector <int> vi;
typedef vector <pii> vii;
typedef set <int> si;
typedef set <pii> sii;
typedef map <int, int> mii;

template <typename T> T sqr (T x) { return x * x; }
template <typename T> T gcd (T a, T b) { return b ? gcd(b, a % b) : a; }

int t;

int main ()
{
    input("B-large.in");
    output("Redownload B-large.in");
    ios_base :: sync_with_stdio(false);
    cin >> t;
    for (int j = 1; j <= t; j++)
    {
        string s;
        int ans = 0;
        cin >> s;
        if (s[s.size() - 1] == '-')
            ans++;
        for (int i = 1; i < s.size(); i++)
            ans += (s[i] != s[i - 1]);
        cout << "Case #" << j << ": " << ans << enter;
    }
}
