#include <bits/stdc++.h>

using namespace std;

#define pb push_back
#define mp make_pair
#define fs first
#define sc second

#define all(x) x.begin(), x.end()

typedef long long ll;
typedef unsigned long long uli;
typedef long double ld;

const int INF = 1e9;
const ll lINF = 1e18;
const int P = 1e9 + 7, Q = 1e9 + 9;
const int base = 41;
const double PI = 3.141592653589793238;
const double eps = 1e-7;

#ifdef DEBUG
#define dout(x) cerr << x
#else
#define dout(x)
#endif // DEBUG

#ifdef DEBUG
#define END {cout << endl; return main ();}
#else
#define END return 0
#endif

int N;

pair< pair< int, int >, int > hm (int n)
{
    if (n == 1)
        return mp (mp (1, 0), 0);
    else
    {
        pair< pair< int, int >, int > res = hm (n / 2);
        pair< pair< int, int >, int > ans = mp (mp (res.fs.fs + res.sc, res.fs.sc + res.fs.fs), res.sc + res.fs.sc);
        return ans;
    }
}

string result (string s, int n)
{
    if (n == 1)
    {
        string res = "";
        res += s[0];
        return res;
    }
    else
    {
        string temp = result (s, n / 2);
        string toret = "";
        for (int i = 0 ; i < temp.size () ; ++i)
        {
            if (temp[i] == 'P')
                toret += "PR";
            else if (temp[i] == 'R' && N > n)
                toret += "SR";
            else if (temp[i] == 'R')
                toret += "RS";
            else if (N > 2 * n)
                toret += "SP";
            else
                toret += "PS";
        }
        return toret;
    }
}

int main()
{
    freopen ("a.in", "r", stdin);
    freopen ("a.out", "w", stdout);
    int T;
    cin >> T;
    for (int Ti = 1 ; Ti <= T ; ++Ti)
    {
        cout << "Case #" << Ti << ": ";

        int n, r, p, s;
        cin >> n >> r >> p >> s;
        N = 1 << n;
        pair< pair< int, int >, int > temp = hm (N);
        dout(r << ' ' << s << ' ' << p << endl);
        dout(temp.fs.fs << ' ' << temp.fs.sc << ' ' << temp.sc << endl << endl);
        string pat = "...";
        bool ok = true;
        if (r == temp.sc)
        {
            pat[2] = 'R';
            if (p == temp.fs.sc)
            {
                pat[1] = 'P';
                if (s == temp.fs.fs)
                {
                    pat[0] = 'S';
                    ok = false;
                }
            }
        }
        if (p == temp.sc && ok)
        {
            pat[2] = 'P';
            if (s == temp.fs.sc)
            {
                pat[1] = 'S';
                if (r == temp.fs.fs)
                {
                    pat[0] = 'R';
                    ok = false;
                }
            }
        }
        if (s == temp.sc && ok)
        {
            pat[2] = 'S';
            if (r == temp.fs.sc)
            {
                pat[1] = 'R';
                if (p == temp.fs.fs)
                {
                    pat[0] = 'P';
                    ok = false;
                }
            }
        }
        if (ok)
        {
            cout << "IMPOSSIBLE\n";
            continue;
        }
        dout(pat << endl);
        cout << result (pat, N) << endl;
    }
    return 0;
}
