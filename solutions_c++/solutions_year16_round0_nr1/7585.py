#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cstring>

using namespace std;
int cnt;
bool vis[10];
inline bool judge(int x) {
	while(x) {
		if(!vis[x % 10]) {
			vis[x % 10] = true;
			cnt ++;
		}
		x /= 10;
	}
	return cnt == 10;
}
inline int calc(int x) {
	memset(vis, false, sizeof vis);
	cnt = 0;
	int cur = x;
	while(!judge(cur)) {
		cur += x;
	}
	return cur;
}
int main() {
	int T;
	scanf("%d", &T);
	for(int cas = 1; cas <= T; ++cas) {
		int x;
		scanf("%d", &x);
		if(x == 0)
			printf("Case #%d: INSOMNIA\n", cas);
		else
			printf("Case #%d: %d\n", cas, calc(x));
	}
	return 0;
}