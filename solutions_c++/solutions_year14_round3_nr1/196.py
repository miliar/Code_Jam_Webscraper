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

LL p, q;

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int T;
    cin >> T;
    for(int Ca = 1; Ca <= T; Ca++) {
        scanf("%I64d/%I64d", &p, &q);
        LL g = __gcd(p, q);
        p /= g, q /= g;

        int ans = 1234;
        for(int d = 1; d < 50; d++) {
            LL a = (1LL<<d);
            if((q >> d) <= p) {
                ans = min(ans, d);
            }
        }
        for(int i = 0; i < 50; i++) {
            LL qq = q << i;
            if(qq > (1LL<<50)) {
                ans = 1234;
                break;
            }
            int flag = 0;
            for(int j = 0; j < 50; j++) {
                if(qq == (1LL<<j)) {
                    flag = 1;
                    break;
                }
            }
            if(flag) break;
        }
        if(ans < 1000) {
            printf("Case #%d: %d\n", Ca, ans);
        }
        else {
            printf("Case #%d: impossible\n", Ca);
        }
    }
    return 0;
}
