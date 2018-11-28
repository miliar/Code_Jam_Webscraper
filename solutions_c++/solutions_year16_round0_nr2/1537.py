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

char str[128];

int main() {
#ifdef _FIO_
	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif // _FIO_
	int t;
	scanf("%d", &t);
	for (int kase = 1; kase <= t; ++kase) {
		scanf("%s", str);
		char prev = '\0';
		int cnt = 0;
		for (int i = 0; str[i]; ++i)
			if (str[i] != prev) {
				prev = str[i];
				++cnt;
			}
		int ans = cnt;
		if ((cnt % 2) ^ (str[0] == '-'))
			--ans;
		printf("Case #%d: %d\n", kase, ans);
	}
#ifdef _FIO_
	fclose(stdin);
	fclose(stdout);
#endif // _FIO_
	return 0;
}
