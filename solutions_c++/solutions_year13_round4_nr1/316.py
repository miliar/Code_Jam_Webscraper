#include <iostream>
#include <vector>
#include <stack>
#include <algorithm>

using namespace std;

constexpr long long mod = 1000002013;

int n;

long long cost(long long i)
{
    return (i * n - (i * (i - 1ll)) / 2ll) % mod;
}

void solve()
{
    long long a = 0, b = 0;
    long long m;
    cin >> n >> m;
    vector<pair<long long, long long> > v;
    for (int i = 0; i < m; ++i) {
        long long o, e, p;
        cin >> o >> e >> p;
        a += cost(e - o) * p;
        a %= mod;
        v.emplace_back(o, p);
        v.emplace_back(e, -p);
    }
    sort(v.begin(), v.end(), [](const pair<long long, long long>& a, const pair<long long, long long>& b){
         return a.first < b.first || (a.first == b.first && a.second > b.second);
    });
    stack<pair<long long, long long> > s;
    for (auto& p: v) {
        if (p.second < 0) {
            long long cnt = -p.second;
            long long to = p.first;
            while (cnt > 0) {
                b += cost(to - s.top().first) * min(cnt, s.top().second);
                b %= mod;
                cnt -= s.top().second;
                if (cnt >= 0) {
                    s.pop();
                } else {
                    s.top().second = -cnt;
                }
            }
        } else {
            s.push(p);
        }
    }
    cout << (a - b + mod) % mod;
}

int main()
{
    int t;
    cin >> t;
    for (int i = 0; i < t; ++i) {
        cout << "Case #" << i + 1 << ": ";
        solve();
        cout << endl;
    }
    return 0;
}
