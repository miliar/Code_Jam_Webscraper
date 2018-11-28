//#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;
#define pb push_back
#define mp make_pair
#define fst first
#define snd second
#define forn(i, n) for (int i = 0; i < (int)(n); ++i)
typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<ll> vll;
typedef vector<char> vc;
typedef pair<int, int> pii;
typedef vector<pii> vii;
#define sz(c) (int)(c).size()
#define all(c) (c).begin(), (c).end()

void solve (string s, int test)
{
    int k;
    cin >> k;

    cout << "Case #" << test << ": ";
    int cnt = 0;
    forn (i, sz(s) - k + 1) if (s[i] == '-')
    {
        cnt++;
        forn (j, k)
            s[i + j] ^= '-' ^ '+';
    }

    if (s == string(sz(s), '+'))
        cout << cnt << endl;
    else
        cout << "IMPOSSIBLE" << endl;
}

int main()
{
    #ifndef ONLINE_JUDGE
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "w", stdout);
    #endif // ONLINE_JUDGE

    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;

    string n;
    int test = 1;
    while (cin >> n)
        solve(n, test), test++;
}
