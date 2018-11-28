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
int n, cnt;
bool us[10];

bool f (int x)
{
    while (x)
    {
        if (!us[x % 10])
            us[x % 10] = true, cnt++;
        x /= 10;
    }
    if (cnt == 10)
        return true;
    return false;
}

int main ()
{
    input("A-large.in");
    output("Redownload A-large.in");
    ios_base :: sync_with_stdio(false);
    cin >> t;
    for (int T = 1; T <= t; T++)
    {
        cin >> n;
        int a = n;
        int i;
        cnt = 0;
        memset(us, 0, sizeof(us));
        for (i = 1; i <= 1000000; i++)
        {
            if (f(a))
            {
                cout << "Case #" << T << ": " << a << enter;
                break;
            }
            a += n;
        }
        if (cnt != 10)
            cout << "Case #" << T << ": " << "INSOMNIA" << enter;
        cerr << i << space;

    }
}
