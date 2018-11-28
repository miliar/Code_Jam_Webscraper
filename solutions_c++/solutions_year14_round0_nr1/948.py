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
#include <limits>
#include <cstring>
#include <string>
using namespace std;

#define pairii pair<int, int>
#define llong long long
#define pb push_back
#define sortall(x) sort((x).begin(), (x).end())
#define INFI  numeric_limits<int>::max()
#define INFL  numeric_limits<long>::max()
#define INFLL numeric_limits<llong>::max()
#define INFD  numeric_limits<double>::max()
#define MOD 1000000007
#define PI 3.1415926535897932384626433832795028841971693993751058209749445923
#define FOR(i,s,n) for (int (i) = (s); (i) < (n); (i)++)
#define FORZ(i,n) FOR((i),0,(n))

void solve() {
    int row; cin >> row;
    int num[4];
    int tmp[4];
    FORZ(i,4) {
        FORZ(j,4) scanf("%d", tmp+j);
        if (i == row-1) {
            FORZ(j,4) num[j] = tmp[j];
        }
    }
    cin >> row;
    int cnt = 0;
    int res;
    FORZ(i,4) {
        FORZ(j,4) scanf("%d", tmp+j);
        if (i == row-1) {
            FORZ(j,4) FORZ(k,4) {
                if (num[j] == tmp[k]) {
                    cnt++;
                    res = num[j];
                }
            }
        }
    }
    if (cnt == 1) cout << res << endl;
    else if (cnt > 1) cout << "Bad magician!" << endl;
    else cout << "Volunteer cheated!" << endl;
}

int main() {
#ifdef DEBUG
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
#endif
    
    int t; cin >> t;
    FORZ(i,t) {
        cout << "Case #" << i+1 << ": ";
        solve();
    }

    return 0;
}
