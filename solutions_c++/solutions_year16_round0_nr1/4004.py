#include <set>
#include <map>
#include <queue>
#include <deque>
#include <cmath>
#include <vector>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <iostream>
#include <algorithm>

#define dprint(expr) fprintf(stderr, #expr " = %d\n", expr)
#define MP make_pair
#define PB push_back

using namespace std;

typedef long long LL;
typedef pair <int, int> PII;

const int N = 1e5 + 7;
const int INF = 0x3f3f3f3f;
const int MOD = 1e9 + 7;
const double EPS = 1e-6;
const double PI = acos(-1.0);

bool vis[12];

int cnt;

bool judge(int n) {
	while (n) {
		int t = n % 10;
		n = n / 10;
		if (!vis[t]) {
			vis[t] = true;
			++cnt;
		}
	}
	return cnt == 10;
}

int main(void){
	int T;
	int Counter = 0;
	scanf("%d", &T);
	while (T--) {
		int n;
		scanf("%d", &n);
		printf("Case #%d: ", ++Counter);
		if (n == 0) {
			cout << "INSOMNIA" << endl;
			continue;
		}
		LL Ans = n;
		memset(vis, 0, sizeof(vis));
		cnt = 0;
		while (!judge(Ans)) {
			Ans += n;
		}
		//printf("n = %d, Ans =", n);
		cout << Ans << endl;
	}
	return 0;
}
//
//                       _oo0oo_
//                      o8888888o
//                      88" . "88
//                      (| -_- |)
//                      0\  =  /0
//                    ___/`---'\___
//                  .' \\|     |// '.
//                 / \\|||  :  |||// \
//                / _||||| -:- |||||- \
//               |   | \\\  -  /// |   |
//               | \_|  ''\---/''  |_/ |
//               \  .-\__  '-'  ___/-. /
//             ___'. .'  /--.--\  `. .'___
//          ."" '<  `.___\_<|>_/___.' >' "".
//         | | :  `- \`.;`\ _ /`;.`/ - ` : | |
//         \  \ `_.   \_ __\ /__ _/   .-` /  /
//     =====`-.____`.___ \_____/___.-`___.-'=====
//                       `=---='
//
//
//     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//
//               ·ð×æ±£ÓÓ         ÓÀÎÞBUG
//
//
//