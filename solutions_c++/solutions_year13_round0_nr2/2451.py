#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>

using namespace std;

#define pb push_back
#define mp make_pair

#define ALL(x) (x).begin(),(x).end()
#define CLR(a,b) memset(a,b,sizeof(a))
#define REPN(x,a,b) for (int x=a; x<b;++x)
#define REP(x,b) REPN(x, 0, b)

#define dbg(x) cout << #x << " = " << x << endl;
#define dbg2(x, y) cout << #x << " = " << x << "  " << #y << " = " << y << endl;
#define dbg3(x, y, z) cout << #x << " = " << x << "  " << #y << " = " << y << "  " << #z << " = " << z << endl;
#define dbg4(x, y, z, w) cout << #x << " = " << x << "  " << #y << " = " << y << "  " << #z << " = " << z << "  " << #w << " = " << w <<  endl;

int main() {

    int T, n, m, A[105][105];
    cin >> T;
    REP(tc, T) {
        cin >> n >> m;
        priority_queue < pair <int, pair <int, int> > > Q;
        REP(i, n) REP(j, m) cin >> A[i][j], Q.push(mp(-A[i][j], mp(i, j)));

        bool res = true;

        while (!Q.empty()) {
            int w = -Q.top().first, y = Q.top().second.first, x = Q.top().second.second;
            Q.pop();

            bool bo1 = 1, bo2 = 1;
            REP(i, n) if (A[i][x] > w) bo1 = false;
            REP(i, m) if (A[y][i] > w) bo2 = false;
            if (!bo1 && !bo2) {
                res = false;
                break;
            }
        }

        if (res) cout << "Case #" << tc+1 << ": YES\n";
        else cout << "Case #" << tc+1 << ": NO\n";
    }
	
	return 0;
}

