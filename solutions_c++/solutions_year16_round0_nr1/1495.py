/*                    _oo0oo_
                     o8888888o
                     88" . "88
                     (| -_- |)
                     0\  =  /0
                   ___/`---'\___
                 .' \\|     |// '.
                / \\|||  :  |||// \
               / _||||| -:- |||||_ \
              |   | \\\  _  /// |   |
              | \_|  ''\___/''  |_/ |
              \  .-\__  '_'  __/-.  /
            ___'. .'  /--.--\  `. .'___
         ."" '<  `.___\_<|>_/___.'  >' "".
        | | :  `- \`.;`\ _ /`;.`/ -`  : | |
        \  \ `_.   \_ __\ /__ _/   ._` /  /
    =====`-.____`.___ \_____/ ___.`____.-`=====
                      `=---='


    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

             ·ð×æ±£ÓÓ         ÓÀÎÞBUG
*/

#include<iostream>
#include<iomanip>
#include<fstream>
#include<sstream>
#include<cstring>
#include<cctype>
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<algorithm>
#include<vector>
#include<list>
#include<map>
#include<set>
#include<deque>
#include<queue>
#include<stack>
#include<bitset>
#include<utility>
#include<string>
#include<ctime>
#include<numeric>
#include<functional>
using namespace std;

#define _FIO_

const double EPS = 1e-8;
const double PI = acos(-1.0);
const double INF = 1e10;
#define LL long long
#define ULL unsigned long long
#define MP make_pair
#define wait system( "pause" );
#define sqr(x) ((x)*(x))

int ans[1000010];

bool check(LL a, bool cnt[]) {
	while (a) {
		cnt[a % 10] = true;
		a /= 10;
	}
	for (int i = 0; i < 10; ++i)
		if (!cnt[i])
			return false;
	return true;
}

int main() {
#ifdef _FIO_
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif // _FIO_
	for (int n = 1; n <= 1000000; ++n) {
		bool cnt[10];
		memset(cnt, 0, sizeof(cnt));
		for (ans[n] = n; !check(ans[n], cnt); ans[n] += n);
	}
	int t;
	scanf("%d", &t);
	for (int kase = 1; kase <= t; ++kase) {
		int n;
		scanf("%d", &n);
		if (n == 0)
			printf("Case #%d: INSOMNIA\n", kase);
		else
			printf("Case #%d: %d\n", kase, ans[n]);
	}
#ifdef _FIO_
	fclose(stdin);
	fclose(stdout);
#endif // _FIO_
	return 0;
}
