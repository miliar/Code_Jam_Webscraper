//Solution by Zhusupov Nurlan
#include <bits/stdc++.h>

using namespace std;

typedef long long LL;
typedef map<string , int> MSI;
typedef vector<int> VI;
typedef pair<int, int> PII;

#define endl '\n'
#define pb(x) push_back(x)
#define sqr(x) ((x) * (x))
#define F first
#define S second
#define SZ(t) ((int) t.size())
#define len(t) ((int) t.length())
#define base LL(1e9 + 7)
#define fname ""
#define sz 1000 * 1000
#define EPS (1e-8)
#define INF ((int)1e9 + 9)
#define mp make_pair

int test, n;
PII p[sz];

int main()
{
    freopen(fname"in", "r", stdin);
    freopen(fname"out", "w", stdout);

    ios_base::sync_with_stdio(false);
    cin.tie(0);

    cin >> test;
    for (int t = 1; t <= test; t++)
    {
        cout << "Case #" << t << ": ";
        cin >> n;
        int S = 0;
        for (int i = 1; i <= n; i++) {
            cin >> p[i].F;
            p[i].S = i;
            S += p[i].F;
        }
    
        p[n + 1].F = 0;
        bool f = 0;
        while (1)
        {
            if (f) cout << " ";
            f = 1;
            sort(p + 1, p + 1 + n);
            reverse(p + 1, p + 1 + n);
            if (p[1].F > S / 2) cerr << "FUCK" << t << endl;
            if (p[1].F == 1 && p[2].F == 1 && p[3].F == 0)
            {
                cout << char(p[1].S + 'A' - 1) << char(p[2].S + 'A' - 1);
                S -= 2;
                break;
            }
            if (!p[1].F) break;
            if (p[2].F > (S - 1) / 2)
            {
                cout << char(p[1].S + 'A' - 1) << char(p[2].S + 'A' - 1);
                p[1].F--;
                p[2].F--;
                S -= 2;
            }
            else
            {
            cout << char(p[1].S + 'A' - 1);
            p[1].F--;
            S--;
            }
        }
        cout << "\n";
    }
}
