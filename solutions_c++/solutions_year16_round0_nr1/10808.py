#include <stack>
#include <stdio.h>
#include <list>
#include <cassert>
#include <set>
#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <unordered_map>
#include <queue>
#include <functional>
#include <cstring>
#include <algorithm>
#include <cctype>
//#pragma comment(linker, "/STACK:102400000,102400000")
#include <string>
#include <map>
#include <cmath>
//using namespace std;
#define LL long long
#define ULL unsigned long long
#define SZ(x) (int)x.size()
#define Lowbit(x) ((x) & (-x))
#define MP(a, b) make_pair(a, b)
#define MS(p, num) memset(p, num, sizeof(p))
#define PB push_back
#define X first
#define Y second
#define ROP freopen("input.txt", "r", stdin);
#define MID(a, b) (a + ((b - a) >> 1))
#define LC rt << 1, l, mid
#define RC rt << 1|1, mid + 1, r
#define LRT rt << 1
#define RRT rt << 1|1
#define FOR(i, a, b) for (int i=(a); (i) < (b); (i)++)
#define FOOR(i, a, b) for (int i = (a); (i)<=(b); (i)++)
const double PI = acos(-1.0);
const int INF = 0x3f3f3f3f;
const double eps = 1e-8;
const int MAXN = 300 + 10;
const int MOD = 1e9 + 7;
const int dir[][2] = {{0, 1}, {0, -1}, {-1, 0}, {1, 0}, {-1, 1}, {-1, -1}, {1, 1}, {1, -1}};
const int seed = 131;
int cases = 0;
typedef std::pair<int, int> pii;

int main() {
    ROP;
    freopen("out.txt", "w", stdout);
    int T;
    scanf("%d", &T);
    while (T--) {
        std::set<int> st;
        printf("Case #%d: ", ++cases);
        LL n;
        std::cin >> n;
        LL num = n;

        int cnt = 0;
        if (n == 0) { puts("INSOMNIA"); continue; }
        while (true) {
            LL tmp = num;
            while (tmp) {
                st.insert(tmp % 10);
                tmp /= 10;
            }
            if (SZ(st) == 10) break;
            num += n;
        }
        std::cout << num << std::endl;
    }
    return 0;
}

