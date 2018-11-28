#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>
using namespace std;

int main() {
    int T, N, X;
    multiset<int> S;
    cin >> T;
    for(int t = 1; t <= T; ++t) {
        cin >> N >> X;
        S.clear();
        for(int i = 0; i < N; ++i) {
            int x;
            cin >> x;
            S.insert(x);
        }
        int ans = 0;
        while(!S.empty()) {
            ans += 1;
            multiset<int>::iterator it = S.end();
            it--;
            int y = *it;
            S.erase(it);
            it = S.upper_bound(X - y);
            if(it != S.begin()) S.erase(--it);
        }
        cout << "Case #" << t << ": " << ans << endl;
    }
    return 0;
}
