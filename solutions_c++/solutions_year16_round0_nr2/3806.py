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

#define NAME "b-large"

int main() {
	//freopen(NAME".in", "r", stdin);
	freopen(NAME".out", "w", stdout);
	int i, j, k, u, v, w;
	int TE;
	cin >> TE;
	for (int CA = 1; CA <= TE; ++CA) {
		string str, filter;
		cin >> str;
		filter = str[0];
		for (i = 1; i < str.length(); ++i) {
			if (str[i] != filter[filter.length() - 1]) {
				filter += str[i];
			}
		}
		int ans = filter.length() - 1;
		if (filter[filter.length() - 1] == '-') {
			++ans;
		}
		printf("Case #%d: %d\n", CA, ans);
	}
	return 0;
}
