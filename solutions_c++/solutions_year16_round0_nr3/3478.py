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

int Ans[12];

vector <int> primes;

LL trans(LL t, int k) {
	LL Ans = 0, sum = 1;
	for (int i = 0; i < 32; ++i) {
		if ((1LL << i) & t) {
			Ans += sum;
		}
		sum = sum * k;
	}
	return Ans;
}

int IsPrime(LL num) {
	int lim = sqrt(num + 0.5);
	for (int i = 0; i < primes.size() && primes[i] <= lim; ++i)
		if (num % primes[i] == 0)
			return primes[i];
	return -1;
}

int Check(LL num, int k) {
//	printf("Check %I64d %d\n", num, k);
	num = trans(num, k);
//	cout << "Num = " << num << endl;
//	printf("Prime = %d\n", IsPrime(num));
	return IsPrime(num);
}

void prepare() {
	int lim = sqrt(0x7ffffffff + 0.5);
	for (int i = 2; i <= lim; ++i) {
		if (IsPrime(i) == -1) {
			primes.PB(i);
		}
	}
}

int main(void) {
	int T, Test_Counter = 0;
	prepare();
	scanf("%d", &T);
	while (++Test_Counter <= T) {
		int n, k;
		printf("Case #%d:\n", Test_Counter);
		scanf("%d%d", &n, &k);
		for (LL i = (1LL << (n - 1LL)) + 1LL; i < (1LL << n) && k; i += 2) {
			bool flag = true;
//			cout << "Check num = " << trans(i, 10) << endl;
			for (int j = 2; j <= 10 && flag; ++j) {
				Ans[j] = Check(i, j);
//				printf("Get %d = %d\n", j, Ans[j]);
				if (Ans[j] == -1)
					flag = false;
			}
			if (flag) {
				--k;
				cout << trans(i, 10);
				for (int j = 2; j <= 10; ++j) {
					printf(" %d", Ans[j]);
				}
				putchar('\n');
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