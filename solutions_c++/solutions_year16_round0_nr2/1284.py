#include <bits/stdc++.h>
using namespace std;
#define pb push_back
#define mp make_pair
typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
#define sz(c) (int)(c).size()
#define ALL(c) (c).begin(), (c).end()

void solve (string s, int test)
{
    cerr << "s = " << s << endl;

    int cnt = 0;
    while (s != string(sz(s), s[0]))
    {
        int j = 0;

        for (int i = 0; i < 1; i++)
        {
            while (j + 1 < sz(s) && s[j + 1] == s[j])
                j++;
            j++;
        }

        reverse(s.begin(), s.begin() + j);
        for (int i = 0; i < j; i++)
            s[i] ^= '+' ^ '-';
        cnt++;
    }

    if (s == string(sz(s), '-'))
        cnt++;
    else
        assert(s == string(sz(s), '+'));

    printf("Case #%d: %d\n", test, cnt);
}

int main()
{
    #ifndef ONLINE_JUDGE
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "w", stdout);
    #endif

 //   ios_base::sync_with_stdio(false);
 //   cin.tie(0);

    int t;
    cin >> t;

    string n;
    int test = 1;
    while (cin >> n)
        solve (n, test), test++;
}
