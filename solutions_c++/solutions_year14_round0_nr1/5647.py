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

#define MAX 105

typedef long long ll;

int main() {
    int T, F, S;
    cin >> T;
    REPN(tc, 1, T+1) {
        set <int> seti;
        int cnt = 0, res = 0, x;
        cin >> F;
        REP(i, 4) {
            REP(j, 4) {
                cin >> x;
                if (i+1 == F) seti.insert(x);
            }
        }
        cin >> F;
        REP(i, 4) {
            REP(j, 4) {
                cin >> x;
                if (i+1 == F) {
                    if (seti.count(x)) res = x, cnt++;
                }
            }
        }
        cout << "Case #" << tc << ": ";

        if (cnt == 1)
            cout << res << "\n";
        else if (cnt == 0) 
            cout << "Volunteer cheated!\n";
        else 
            cout << "Bad magician!\n";
    }
}

