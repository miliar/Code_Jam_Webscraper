#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    freopen("a.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    long long sum, maxx;
    long long  x;
    cin >> t;
    long long a, buf;
    int n;
    vector<long long> v, ans;
    for (int i = 0; i < t; ++i) {
        cin >> a >> n;
        if (a == 1) {
            for (int j = 0; j < n; ++j) {
                cin >> x;
            }
            cout << "Case #" << i + 1 << ": " << n << endl;
            continue;
        }
        v.clear();
        ans.clear();
        for (int j = 0; j < n; ++j) {
            cin >> x;
            v.push_back(1LL * x);
            ans.push_back(0);
        }
        sort(v.begin(), v.end());
        buf = a;
        for (int j = 0; j < n; ++j) {
            ans[j] = 0;
            if (buf > v[j]) {
                buf += v[j];
            } else {
                while (buf <= v[j]) {
                    ans[j] += 1;
                    buf += buf - 1;
                }
                buf += v[j];
            }
        }
        sum = 0LL;
        maxx = 0LL;
        for (int j = n - 1; j >= 0; --j) {
            sum += ans[j];
            maxx = max(maxx, sum - 1LL * (n - j));
        }
        sum = 0LL;
        for (int j = 0; j < n; ++j) {
            sum += ans[j];
        }
        cout << "Case #" << i + 1 << ": " << sum - maxx << endl;
    }
    return 0;
}
