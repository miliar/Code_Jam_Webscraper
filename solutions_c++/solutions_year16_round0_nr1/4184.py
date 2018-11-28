#include <bits/stdc++.h>

#define all(x) (x).begin(), (x).end()
#define pb push_back
#define mp make_pair
#define FILE "sheep"

using namespace std;

typedef long long ll;
typedef unsigned long long ull;

const int INF = numeric_limits<int>::max();
const ll LLINF = numeric_limits<ll>::max();
const ull ULLINF = numeric_limits<ull>::max();
const double PI = acos(-1.0);

bool used[15];

bool getDigits(ll n)
{
    while(n)
    {
        used[n % 10] = 1;
        n /= 10;
    }
    for(int i = 0; i < 10; i++)
        if(!used[i])
            return 0;
    return 1;
}

int main()
{
    freopen(FILE".in", "r", stdin);
    freopen(FILE".out", "w", stdout);
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int T;
    cin >> T;
    for(int tt = 1; tt <= T; tt++)
    {
        memset(used, 0, sizeof(used));
        ll n;
        cin >> n;
        bool f = 0;
        for(ll i = 1; i <= 1000000; i++)
        {
            if(getDigits(i * n))
            {
                f = 1;
                cout << "Case #" << tt << ": " << i * n << '\n';
                break;
            }
        }
        if(!f)
            cout << "Case #" << tt << ": INSOMNIA\n";
    }
    return 0;
}
