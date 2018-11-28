
#include <bits/stdc++.h>

#define forn(i,n) for(long long i = 0; i < n; i++)
#define ford(i,n) for(int i = n - 1; i > -1; i--)
#define forl(i,l,r) for(int i = l; i <= r; i++)
#define forst(it, a, ll) for(set < ll > :: iterator it = a.begin(); it != a.end(); it++)
#define forld(i,l,r) for(int i = l; i >= r; i--)
#define FAST_READ ios_base::sync_with_stdio(false);
#define INF 100000000000
#define MOD 1000000007
#define pi 3.14159265358973238462643383
#define EPS 0.00000000001
#define f first
#define s second
#define pb push_back
#define mp(i, j) make_pair(i, j)
#define COUT(n, a) fixed << setprecision(a) << n

using namespace std;

typedef unsigned long long ull;
typedef int long long ll;
typedef long long ld;
typedef string str;

int main()
{
    FAST_READ

    freopen("B-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);

    ll t, ans, mi;
    str n;

    cin >> t;

    vector < ll > a;

    forl(p, 1, t)
    {
        cin >> n;

        ans = 0;

        a.clear();
        a.pb(1);

        forl(i, 1, n.length() - 1)
        {
            if (n[i] == n[i - 1])
                a[a.size() - 1]++;
            else
                a.pb(1);
        }

        cout << "Case #" << p << ": ";

        if (n[0] == '-')
        {
            if (n[n.length() - 1] == '+')
                cout << a.size() - 1 << endl;
            else
                cout << a.size() << endl;
        }
        else
        {
            if (a.size() == 1)
                cout << 0 << endl;
            else
                if (n[n.length() - 1] == '+')
                cout << a.size() - 1 << endl;
            else
                cout << a.size() << endl;
        }
    }
}
