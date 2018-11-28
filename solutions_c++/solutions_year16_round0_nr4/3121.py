#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
using namespace std;

typedef long long LL;
typedef pair<int,int> PII;
#define MP make_pair
#define PB push_back
#define SZ size()
#define AA first
#define BB second
#define BG begin()
#define ED end()
#define SQ(x) ((x)*(x))
#define cmin(x,y) x=min(x,y)
#define cmax(x,y) x=max(x,y)

#define NAME "d-small"

int main() {
    //freopen(NAME".in", "r", stdin);
    freopen(NAME".out", "w", stdout);
    int i, j, k, u, v, w;
    LL K, C, S;
    int te;
    cin >> te;
    for(int ca = 1; ca <= te; ++ca) {
        cin >> K >> C >> S;
        cout << "Case #" << ca << ":";
        for(LL i = 0; i < S; ++i) {
            LL p = 0;
            for(LL j = 0; j < C; ++j) {
                p = p * K + i;
            }
            cout << " " << p + 1;
        }
        cout << endl;
    }
    return 0;
}
