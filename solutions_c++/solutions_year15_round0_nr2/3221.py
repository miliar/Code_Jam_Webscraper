#include <bits/stdc++.h>

#define M_PI 3.14159265358979323846
#define all(x) (x).begin(), (x).end()
#define pb push_back
#define mp make_pair
#define FILE "codejam"

using namespace std;

typedef long long ll;
typedef unsigned long long ull;

const int INF = numeric_limits<int>::max();
const ll LLINF = numeric_limits<ll>::max();
const ull ULLINF = numeric_limits<ull>::max();

int countTurns(int n, int k)
{
    if(n <= k)
        return 0;
    return countTurns(n - k, k) + 1;
}

int main()
{
    freopen(FILE".in", "r", stdin);
    freopen(FILE".out", "w", stdout);
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int tests;
    cin >> tests;
    for(int t = 1; t <= tests; t++)
    {
        int d;
        cin >> d;
        vector<int> v(d);
        int ans = -INF;
        for(int i = 0; i < d; i++)
        {
            cin >> v[i];
            ans = max(ans, v[i]);
        }
        sort(all(v));
        int ma = ans;
        for(int i = 1; i <= ma; i++)
        {
            int curAns = 0;
            for(int j = 0; j < d; j++)
                curAns += countTurns(v[j], i);
            curAns += i;
            ans = min(ans, curAns);
        }
        cout << "Case #" << t << ": " << ans << endl;
    }
}
