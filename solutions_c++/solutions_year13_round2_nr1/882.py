#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <cassert>
using namespace std;

typedef map< pair< int, int >, int > Cache;
Cache cache;
vector< int > moto;

int solve(int a, int n) {
    if (n == -1)
        return 0;
    if (a > 1e6)
        return 0;
    auto key = make_pair(a, n);
    auto cached = cache.find(key);
    if (cached != cache.end())
        return cached->second;
    if (moto[n] < a)
        return cache[key] = solve(a + moto[n], n - 1);
    if (a == 1)
        return cache[key] = solve(a, n - 1) + 1;
    return cache[key] = min(solve(2 * a - 1, n), solve(a, n - 1)) + 1;
}

int main() {
    int T;
    cin >> T;
    for (int i = 1; i <= T; i++) {
        cache.clear();
        int a, n;
        cin >> a >> n;
        moto.resize(n);
        for (auto &m : moto)
            cin >> m;
        sort(moto.rbegin(), moto.rend());
        cout << "Case #" << i << ": " << solve(a, moto.size() - 1) << "\n";
    }
    return 0;
}
