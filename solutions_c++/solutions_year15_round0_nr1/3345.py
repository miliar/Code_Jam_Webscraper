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

int main()
{
    freopen(FILE".in", "r", stdin);
    freopen(FILE".out", "w", stdout);
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int test;
    cin >> test;
    for(int t = 1; t <= test; t++)
    {
        int n;
        cin >> n;
        string s;
        cin >> s;
        map<int, int> m;
        for(int i = 0; i <= n; i++)
            m[i] = s[i] - '0';
        int sum = 0, ans = 0;
        for(auto k: m)
        {
            if(k.second)
            {
                if(sum >= k.first)
                    sum += k.second;
                else
                {
                    ans += k.first - sum;
                    sum += k.first - sum + k.second;
                }
            }
        }
        cout << "Case #" << t << ": " << ans << endl;
    }
}
