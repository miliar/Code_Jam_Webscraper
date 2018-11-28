# include <iostream>
# include <cmath>
# include <algorithm>
# include <map>
# include <unordered_set>
# include <memory.h>
# include <vector>
using namespace std;
 
 
const int MD = 1000000000 + 7;
const int MAX_E = 500333;
const int MAX_N = 1047;

#define time ez_contest
#define rank ez_timus

void solve(int tc) {
    cout << "Case #" << tc << ": ";
    long long k, c, s;
    cin >> k >> c >> s;
    for (int i = 1; i < k; i++) {
        cout << i << " ";
    }
    cout << k << "\n";
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    ios_base::sync_with_stdio(false);
    int tc;
    cin >> tc;
    for (int t = 1; t <= tc; t++) {
        solve(t);
    }
    return 0;
}

