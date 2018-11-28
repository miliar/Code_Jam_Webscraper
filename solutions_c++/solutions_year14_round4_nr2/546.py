#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

#define pii pair<int, int>
vector<pii> q;
#define MAXN 1010
int fen[MAXN * 2];
void add(int x, int v)
{
    for (; x <= MAXN; x += x & -x)
        fen[x] += v;
}
int get(int x)
{
    int ans = 0;
    for (; x > 0; x -= x & -x)
        ans += fen[x];
    return ans;
}
int main()
{
    int tt;
    cin >> tt;
    for (int tc = 1; tc <= tt; tc++)
    {
        cout << "Case #" << tc << ": ";
        int n;
        cin >> n;
        q.clear();
        for (int i = 1; i <= n; i++)
        {
            int a;
            cin >> a;
            q.push_back(pii(a, i));
            add(i, 1);
        }
        sort(q.begin(), q.end());
        int ans = 0;
        for (int i = 0; i < n; i++)
        {
            add(q[i].second, -1);
            ans += min(get(q[i].second), get(MAXN) - get(q[i].second));
        }
        cout << ans << endl;
    }
}
