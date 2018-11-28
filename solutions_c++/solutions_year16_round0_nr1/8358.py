
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

    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);

    ll t, n, x, j, k = 1;

    cin >> t;

    vector < ll > vis(10);

    forl(p, 1, t)
    {
        cin >> n;

        forn(i, 10)
        {
            vis[i] = 0;
        }

        if (n == 0)
        {
            cout << "Case #" << p << ": INSOMNIA\n";
        }
        else
        {
            j = 0;
            k = 1;

            while(k)
            {
                j++;
                x = n * j;

                while(x)
                {
                    vis[x % 10] = 1;

                    x /= 10;
                }

                forn(i, 10)
                if (vis[i] == 0)
                    break;
                else if (i == 9)
                {
                    cout << "Case #" << p << ": " << j * n << endl;
                    k = 0;
                }
            }
        }
    }
}
