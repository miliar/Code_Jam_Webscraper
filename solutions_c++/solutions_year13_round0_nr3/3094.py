#include <vector>
#include <list>
#include <map>
#include <set>
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
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <ctime>
#define maxl 5100000
#define ll long long
#define INF 0x3f3f3f3f

using namespace std;

const int maxlen = 1010;
const int base = 10000;

class HP {
public:
	int len, s[maxlen];
	HP() { *this = 0; }
	HP(int n) { *this = n; }
	HP(const char* str) { *this = str; }
	friend ostream& operator<<(ostream& cout, const HP& x);
	HP operator=(const char* str) {
		len = strlen(str);
		for(int i=1; str[i]; ++i) s[i] = str[len-i] - '0';
		return *this;
	}
	HP operator=(int n) {
		if(n == 0) { len = 1; s[1] = 0; return *this; }
		for(len=0; n; ) { s[++len] = n % 10; n /= 10; }
		return *this;
	}
	HP operator*(const HP& b) {
		HP c; c.len = len + b.len;
		for(int i=1; i<=c.len; ++i) c.s[i] = 0;
		for(int i=1; i<=len; ++i) for(int j=1; j<=b.len; ++j) c.s[i+j-1] += s[i] * b.s[j];
		for(int i=1; i<=c.len; ++i) { c.s[i+1] += c.s[i] / 10; c.s[i] %= 10; }
		while(c.len > 1 && !c.s[c.len]) --c.len;
		return c;
	}
	HP operator+(const HP& b) {
		HP c; c.len = max(len, b.len) + 1;
		for(int i=1; i<=c.len; ++i) c.s[i] = 0;
		for(int i=1; i<=c.len; ++i) {
			if(i <= len) c.s[i] += s[i];
			if(i <= b.len) c.s[i] += b.s[i];
			c.s[i+1] = c.s[i] / 10;
			c.s[i] %= 10;
		}
		if(!c.s[c.len]) c.len--;
		return c;
	}
	HP operator-(const HP& b) {
		HP c;
		for(int i=1, j=0; i<=len; ++i) {
			c.s[i] = s[i] - j;
			if(i <= b.len) c.s[i] -= b.s[i];
			if(c.s[i] < 0) { j = 1; c.s[i] += 10; } else j = 0;
		}
		c.len = len; while(c.len > 1 && !c.s[c.len]) c.len--;
		return c;
	}

	int compare(const HP& b) {
		if(len > b.len) return 1;
		if(len < b.len) return -1;
		int i = len;
		while(i > 1 && s[i] == b.s[i]) i--;
		return s[i] - b.s[i];
	}
};

ostream& operator<<(ostream& cout, const HP& x) {
	for(int i=x.len; i>=1; --i) cout << x.s[i]; return cout;
}

ll st[maxl];
int top, A, B, a[200], c[200];

void dfs(int now, int tot, int mid) {
	if(now == mid) {
		ll num = 0;
		for(int i=0; i<tot; ++i) num = num * 10 + a[i];
		st[top++] = num * num;
		return;
	}

	int s = (now == 0) ? 1 : 0;
	for(int i=s; i<4; ++i) {
		a[now] = a[tot - 1 - now] = i;

		int flag = 1;
		for(int j=now; j<mid; ++j) {
			c[j] += a[now] * a[j - now];
			if(c[j] > 9) flag = 0;
		}

		if(flag) {
			dfs(now + 1, tot, mid);
		}

		for(int j=now; j<mid; ++j) {
			c[j] -= a[now] * a[j-now];
		}
		a[now] = a[tot - 1 - now] = 0;

		if(!flag) break;
	}
}

void init() {
	top = 0;
	st[top++] = 1;
	st[top++] = 4;
	st[top++] = 9;

	for(int i=2; i<=8; ++i) {
		memset(c, 0, sizeof c);
		memset(a, 0, sizeof a);
		dfs(0, i, (i + 1) / 2);
	}
	//dfs(0, 30, 15);
}

int solve(int n) {
	if(n == 0) return 0;
	if(n == 1) return 1;

	int ans = 0;
	for(int i=0; i<top; ++i) if(st[i] <= n) {
		//printf("%I64d %d\n", st[i], k);
		ans++;
	}
	return ans;
}

int main() {

	init();

	//for(int i=0; i<20; ++i) printf("%d %d\n", i, st[i]);

	int t;
	scanf("%d", &t);
	for(int q=1; q<=t; ++q) {
		scanf("%d%d", &A, &B);
		int y = solve(B);
		int x = solve(A - 1);
		//printf("x %d %d\n", y, x);
		printf("Case #%d: %d\n", q, y - x);
	}
	return 0;
}


