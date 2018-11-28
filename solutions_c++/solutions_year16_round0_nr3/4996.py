#include <algorithm>
#include <iostream>
#include <iomanip>
#include <cstring>
#include <climits>
#include <complex>
#include <fstream>
#include <cassert>
#include <cstdio>
#include <bitset>
#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <ctime>
#include <set>
#include <map>
#include <cmath>

using namespace std;

const int maxn = 55555;
int n;
int a, b;
char opt[5];

int main() {
	freopen("in", "r", stdin);
	int T;
	while(~scanf("%d", &n)) {
		int ans;
		double cur = 0x7f7f7f7f;
		for(int i = 1; i <= n; i++) {
			double tmp;
			scanf("%d", &a);
			scanf("%s", opt);
			scanf("%d", &b);
			switch(opt[0]) {
				case'+': tmp = double(double(a) + double(b)); break;
				case'-': tmp = double(double(a) - double(b)); break;
				case'*': tmp = double(double(a) * double(b)); break;
				case'/': tmp = double(double(a) / double(b)); break;
			}
			cout << tmp << endl;
			if(cur - 9.0 > abs(tmp - 9.0)) {
				cur = abs(tmp - 9.0);
				ans = i;
			}
		}
		printf("%d\n", ans);
	}
	return 0;
}
