#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>

using namespace std;

#define MAX 100000
#define INF 2140000000
#define MOD 1000000007

int main() {
	#ifndef ONLINE_JUDGE
		freopen("in.txt","r",stdin);
		freopen("out.txt","w",stdout);
	#endif

	int test, kk = 1;
	long double c, f, x, p = 2, ans = 0;
	cin >> test;

	while (test--) {
		cin >> c >> f >> x;
		ans = 0;
		p = 2;
		cout << "Case #" << kk++ << ": ";
		while (1) {
			if ((x-c)*(p+f) > p*x) {
				ans += c / p;
				p = p + f;
			}
			else {
				ans += x / p;
				break;
			}
		}

		printf("%.6Lf\n", ans);
	}
		
	
	return 0;
}