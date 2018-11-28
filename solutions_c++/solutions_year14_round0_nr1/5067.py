#include <string>
#include <vector>
#include <set>
#include <map>
#include <iostream>
#include <algorithm>
#include <sstream>
#include <cmath>
#include <string.h>
#include <queue>
#include <cstdio>
#include <cassert>
#include <deque>
#include <stack>
#include <utility>
#include <numeric>
#include <ctime>

using namespace std;

#define forn(i, n) for (int i = 0; i < (int)(n); i++)
#define for1(i, n) for (int i = 1; i <= (int)(n); i++)
#define forv(i, v) forn(i, v.size())

#define mp make_pair
#define pb push_back
#define all(v) v.begin(), v.end()

typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;

void solve(int tc) {
    cout << "Case #" << tc << ": ";
    vector<int> ans(2);
    vector< vector<int> > p(2, vector<int>(17, 0));
    forn(it, 2) {
        cin >> ans[it];
        for1(i, 4) {
            for1(j, 4) {
                int x;
                cin >> x;
                p[it][x] = i;
            }
        }
    }
    int cnt = 0, res = -1;
    for1(x, 16) {
        if (p[0][x] == ans[0] && p[1][x] == ans[1]) {
            cnt++;
            res = x;
        }
    }
    if (cnt == 1) cout << res << endl; 
    else if (cnt == 0) cout << "Volunteer cheated!" << endl;
    else cout << "Bad magician!" << endl;
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int tc;
    cin >> tc;
    forn(i, tc) solve(i + 1);
    return 0;
}
