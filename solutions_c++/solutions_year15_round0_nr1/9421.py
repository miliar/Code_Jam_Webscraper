/////////////////////////////
// Header code
/////////////////////////////
#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;
typedef complex <double> cd;
typedef vector <int> vi;
typedef vector <double> vd;
typedef vector <ll> vl;
typedef vector <int>::iterator vit;
typedef pair <int, int> pii;
typedef vector < pair <int, int> > vii;
typedef vector < pair <int, int > >::iterator viit;
typedef vector < pair <double, double> > vdd;
typedef vector < cd > vcd;
typedef vector < pair <ll, ll> > vll;
typedef set <int> si;
typedef set <int>::iterator sit;

#define ALL(a) (a).begin(), (a).end()
#define SORT(a) std::sort((a).begin(), (a).end())
#define REVERSE(a) std::reverse((a).begin(), (a).end())
#ifdef _HOME_
    #define LOG(e) cout << #e << " = " << e << endl;
#else
    #define LOG(e)
#endif
#define X first
#define Y second
#define sqr(a) ((a)*(a))
#define FORI(n) for (int i = 0; i < n; ++i)
#define FOR(i, n) for (int i = 0; i < n; ++i)

template <typename T> istream &operator>>(istream &in, vector <T> &v) { for (size_t i = 0; i < v.size(); ++i) in >> v[i]; return in; }
template <typename T> ostream &operator<<(ostream &out, vector <T> const &v) { for (size_t i = 0; i < v.size(); ++i) out << v[i] << " "; return out; }
template <typename T1, typename T2> ostream &operator<<(ostream &out, pair <T1, T2> const &p) { out << p.first << " " << p.second; return out; }

#define EPS 1e-7
#define MOD (1000000000 + 321)
#define PI 3.14159265358979323846
#define INF 1000000000
#define SINF 1000000

void solution();

int main(int argc, char *argv[])
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	const clock_t start = clock();
    ios::sync_with_stdio(false);
    cin.tie(0);
    solution();
    cerr.precision(5);
    cerr << endl << "Time: " << fixed << double( clock () - start ) / (double)CLOCKS_PER_SEC << endl;
    return EXIT_SUCCESS;
}

//////////////////////////////
// Solution code
//////////////////////////////

void solution()
{
    int testCount;
    cin >> testCount;
    for (int test = 1; test <= testCount; ++test)
    {
        cout << "Case #" << test << ": ";
        int n;
        string s;
        cin >> n >> s;
        int cnt = 0, ans = 0;
        for (int i = 0; i <= n; ++i)
        {
            int k = s[i] - '0';
            if (k == 0)
                continue;
            if (i <= cnt)
                cnt += k;
            else
            {
                ans += i - cnt;
                cnt = i;
                cnt += k;
            }
        }
        cout << ans;
        cerr << ans << endl;

        cout << endl;
    }
}


