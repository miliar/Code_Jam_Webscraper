#include <iostream>
#include <queue>
#include <cstdlib>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <cmath>
#include <algorithm>
#include <cstring>
#include <stack>
#include <iomanip>

#define FOR(i,x,y) for(int i =(int)(x); i<(int)(y); i++)
#define REP(i, N) FOR(i, 0, N)
#define SZ(x) (int)x.size()

using namespace std;

typedef vector<int> vin;
typedef pair<int, int> pii;
typedef vector<pair<int, int>> vpii;
typedef vector<vector<int>> vvin;

typedef long long LL;
typedef unsigned long long ULL;

string good = "GABRIEL";
string bad = "RICHARD";

int main () {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int T; cin >> T;
    int kk = 1;
    while (T --> 0) {
        cout << "Case #" << kk << ": ";
        int x, n, m; cin >> x >> n >> m;
        if (n > m) {
            int t = n;
            n = m;
            m = t;
        }
        string ret = good;
        if (x > 6) ret = bad;
        else if (x > n && x > m) ret = bad;
        else if ((n*m) % x != 0) ret = bad;
        else if (x - 1 > n) ret = bad;

        if (x == 1) ret = good;
        cout << ret << endl;
        kk++;
    }
    return 0;
}

