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

int main() {
#ifdef _FIO_
	freopen("D-small-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif // _FIO_
	int t;
	scanf("%d", &t);
	for (int kase = 1; kase <= t; ++kase) {
		int k, c, s;
		scanf("%d%d%d", &k, &c, &s);
		printf("Case #%d:", kase);
		for (int i = 1; i <= s; ++i)
			printf(" %d", i);
		puts("");
	}
#ifdef _FIO_
	fclose(stdin);
	fclose(stdout);
#endif // _FIO_
	return 0;
}
