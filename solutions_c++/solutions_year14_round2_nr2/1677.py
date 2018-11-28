#include <string>
#include <cstring>
#include <cstdio>
#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
using namespace std;
#define N 310


void solve() {
    int a, b, k;
    cin >> a >> b >> k;
    int ans = 0;
    int n = min(a, b), m = max(a, b);
    for(int i=0;i<n;i++) {
        for(int j=0;j<m;j++) {
            if((i&j) < k) {
                ans++;
                // cout << int(i&j) << endl;
            }
        }
    }
    cout << ans << endl;
}

int main() {
    int T;
    cin >> T;
    for(int i=1;i<=T;i++) {
        cout << "Case #" << i << ": ";
        solve();
    }
    return 0;
}