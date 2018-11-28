#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
using namespace std;

typedef long long LL;
typedef pair<int,int> PII;
#define MP make_pair
#define PB push_back
#define SZ size()
#define AA first
#define BB second
#define BG begin()
#define ED end()
#define SQ(x) ((x)*(x))
#define cmin(x,y) x=min(x,y)
#define cmax(x,y) x=max(x,y)

#define NAME "A-large"

set<LL> S;
int digit[10];
int cnt = 0;
LL cur = 0;

inline bool update_digit(LL cur, int digit[], int &cnt) {
	if (S.find(cur) != S.end()) {
		return false;
	}
	S.insert(cur);
	int x;
	do {
		x = cur % 10;
		cur /= 10;
		if(digit[x] == 0) {
			digit[x] = 1;
			++cnt;
		}
	}while(cur);
	return true;
}

int main() {
	//freopen(NAME".in", "r", stdin);
	freopen(NAME".out", "w", stdout);
	LL i, j, k, u, v, w;
	int t;
	cin >> t;
	int ca = 0;
	cerr << t << "-----------" << endl;

	while(ca < t) {
		cerr << ca <<endl;
		++ca;
		cin >> w;
		S.clear();
		cnt = 0;
		memset(digit, 0, sizeof(digit));
		cur = 0;
		while(cnt < 10) {
			cur += w;
			bool flag = update_digit(cur, digit, cnt);
			if (!flag) {
				break;
			}
		}
		if (cnt < 10) {
			printf("Case #%d: INSOMNIA\n", ca);
		}
		else {
			printf("Case #%d: %lld\n", ca, cur);
		}
	}
	return 0;
}
