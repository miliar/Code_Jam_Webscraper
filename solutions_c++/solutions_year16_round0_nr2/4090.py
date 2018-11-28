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

char data[N];

int n;

set <pair<int, char> > vis;

int turn(int num, int i) {
	int left = num >> i, right = num & ((1 << i) - 1);
	while (i--) {
		left = (left << 1) ^ (right & 1) ^ 1;
		right >>= 1;
	}
	return left;
}

bool dfs(int num, int times) {
	if (num == 0) return true;
	vis.insert(MP(num, times));
	int i = n - 1;
	while ((num & (1 << i)) == 0) {
		--i;
	}
	while (i >= 0) {
		int t = turn(num, i + 1);
		if (vis.find(MP(t, times - 1)) == vis.end() && times && dfs(t, times - 1)) {
			return true;
		}
		--i;
	}
	return false;
}

int main(void){
	//freopen("B-small-attempt0.in", "r", stdin);
	int T, Test_Counter = 0;
	scanf("%d", &T);
	while (T--) {
		scanf("%s", data);
		int num = 0;
		n = strlen(data);
		for (int i = n; i; --i) {
			num = (num << 1) + (data[i - 1] == '-');
		}
		vis.clear();
		for (int Ans = 0; Ans <= 100; ++Ans) {
			if (dfs(num, Ans)) {
				printf("Case #%d: %d\n", ++Test_Counter, Ans);
				break;
			}
		}
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