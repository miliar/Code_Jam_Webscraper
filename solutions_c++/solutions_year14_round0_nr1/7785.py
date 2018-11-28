//#pragma comment(linker,"/STACK:102400000,102400000")
#include <cctype>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <ctime>
#include <map>
#include <set>
#include <list>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <string>
#include <vector>
#include <fstream>
#include <iomanip>
#include <numeric>
#include <sstream>
#include <utility>
#include <iostream>
#include <algorithm>
#include <stdexcept>
#include <functional>

using namespace std;

#define PB push_back
#define MP make_pair
#define AA first
#define BB second
#define BGN begin()
#define END end()
#define SZ size()
#define SORT(p) sort(p.BGN,p.ED)
#define CLR(a, b) memset(a, (b), sizeof(a))
#define mabs(x) (x < 0 ? -x : x)
#define sqr(x) ((x)*(x))
#define ITE ::iterator
typedef long long LL;
typedef pair<int, int> PII;
typedef vector <int> VI;
typedef set < int > SI;

int main() {
//    freopen("A-small-attempt0.in", "r", stdin);
//    freopen("A-small-attempt0.out", "w", stdout);
    int Test;
    cin >> Test;
    for(int Case = 1; Case <= Test; Case++) {
        int n, ans, cnt;
        int g[10][10], f[20] = {0};
        cin >> n;
        for(int i = 1; i <= 4; i++) {
            for(int j = 1; j<= 4; j++) {
                cin >> g[i][j];
            }
        }
        for(int j = 1; j <= 4; j++) {
            f[g[n][j]] = Case;
        }
        cin >> n;
        for(int i = 1; i <= 4; i++) {
            for(int j = 1; j <= 4; j++) {
                cin >> g[i][j];
            }
        }
        ans = -1; cnt = 0;
        for(int j = 1; j <= 4; j++) {
            if(f[g[n][j]] == Case) {
                ans = g[n][j]; cnt++;
            }
        }
        cout << "Case #" << Case << ": ";
        if(cnt == 0) {
            cout << "Volunteer cheated!" << endl;
        }
        else if( cnt == 1) {
            cout << ans << endl;
        }
        else cout << "Bad magician!" << endl;
    }
    return 0;
}
