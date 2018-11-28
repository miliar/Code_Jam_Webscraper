#include <bits/stdc++.h>
#define _ << " " <<

#define X first
#define Y second

using namespace std;

typedef pair<int, int> Point;
typedef long long lint;
typedef int8_t int8;


void solve() {
    lint N; cin >> N;
    if(N == 0) {
        cout << "INSOMNIA" << endl;
        return;
    }

    set<int> seen;
    lint x = 0;
    while(true) {
        x += N;

        lint tmp = x;
        while(tmp > 0) {
            seen.insert(tmp%10);
            tmp/=10;
        }
        if(seen.size() == 10) {
            cout << x << endl;
            return;
        }
    }

}


int main() {
    ios_base::sync_with_stdio(false);
    int T; cin >> T;

    for(int t = 1; t <= T; ++t) {
        cout << "Case #" << t << ": ";
        solve();
    }
    return 0;
}

