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

LL t, q, p, k, W, c;

LL f(LL x)
{
    LL L = 1, G = 0;
    while (x--) {
        G = G * k + L;
        L *= 2;
    } 
    return W;
}

int main()
{
    freopen(fname"in", "r", stdin);
    freopen(fname"out", "w", stdout);

    ios_base::sync_with_stdio(false);
    cin.tie(0);

    cin >> t;
    for (int q = 1; q <= t; q++)
    {
        LL s;
        cin >> k >> c >> s;
        W = 1;
        for (int i = 1; i < c; i++)
            W *= k;
        cout << "Case #" << q << ": ";
        p = 1;
        for (int i = 1; i <= k; i++)
        {
            cout << p << " ";
            p += f(c);
        }

        cout << "\n";
    }
}
