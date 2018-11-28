#include <algorithm>
#include <stack>
#include <bitset>
#include <cassert>
#include <map>
#include <string>
#include <iostream>
#include <queue>
#include <set>
#include <vector>
#include <cmath>
#include <limits>

using namespace std;

typedef long long ll;
typedef vector<int> vi;

#define sz(x) int((x).size())
#define FOR(i,a,b) for(int (i) = (a); (i) < (b); ++(i))
#define REP(i,n) for(int (i) = 0; (i) < (n); ++(i))
#define pb push_back
#define all(c) (c).begin(), (c).end()
#define square(a) (a)*(a)
#define mp(a,b) make_pair((a),(b))

const int oo = numeric_limits<int>::max();


int main() {
    int T, maxv, res, cnt;
    char c;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        res = 0;
        cnt = 0;
        cin >> maxv;
        for (int v = 0; v <= maxv; v++) {
            cin >> c;
            if (c == '0') continue;
            else if (cnt >= v) {
                cnt += c-'0';
            }
            else {
                res += v-cnt;
                cnt += v-cnt + c-'0';
            }
        }
        cout << "Case #" << t << ": " << res << endl;
    }
}
