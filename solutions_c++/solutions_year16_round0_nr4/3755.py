#include <iostream>
#include <map>
#include <stdio.h>
#include <cstddef>
#include <sstream>
#include <vector>
#include <stdexcept>
#include <fstream>
#include <queue>

using namespace std;

void solve(long long k, long long c)
{
    vector <long long> ans(k);
    for (long long i = 0; i < k; i++) {
        ans[i] = i + 1;
    }
    for (long long i = 2; i <= c; i++) {
        for (long long j = 0; j < k; j++) {
            long long cur = ans[j] % k;
            if (!cur) cur = k;
            ans[j] = (ans[j] - 1) * k + cur;
        }
    }
    for (auto &el : ans) {
        cout << el << " ";
    }
    cout << endl;
}

int main()
{
    long long T;
    cin >> T;
    for (long long i = 0; i < T; i++) {
        cout << "Case #" << i + 1 << ": ";
        long long k, c, s;
        cin >> k >> c >> s;
        solve(k, c);
    }
    return 0;
}
