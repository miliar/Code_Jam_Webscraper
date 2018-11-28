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

typedef pair<int, int> PP;
typedef long long LL;
#define pb push_back
#define fr first
#define sc second

int a[20000], n, m, cnt[1000];
void f(){
	memset(cnt, 0, sizeof(cnt));
	cin >> n >> m;
	for (int i = 0; i < n; i ++) cin >> a[i], cnt[a[i]] ++;
	int res = 0;
	while (n) {
		int t = m;
		int ok = 1;
		for (int k = 0; k < 2; k ++){
			int i;
			for ( i = t; i >= 1; i --) {
				if (cnt[i]) {
					t -= i; cnt[i] --; n --; break;
				}
				else continue;
			}
		}
		res ++;
	}
	cout << res << endl;
}

int main() {
	#ifdef _TEST_
	freopen("input.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	#endif
	int testcase; 
	cin >> testcase;
	for (int i = 0; i < testcase; i ++) {
		cout << "Case #" << i + 1 <<": ";
		f();
	}

	return 0;
}
