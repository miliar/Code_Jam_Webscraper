#include <cstdio>
#include <queue>
#include <set>
#include <algorithm>
#include <cstring>
using namespace std;
char s[20];
int n, a[20], tmp[20];
int dis[2100];
queue<int> Q;
void work() {
	scanf("%s", s);
	int n = strlen(s);
	int st = 0;
	for (int i = 0; i < n; ++i) {
		int t = s[i] == '+' ? 1 : 0;
		st |= t * (1 << i);	
	}
	Q.push(st);	
	memset(dis, 63, sizeof(dis));
	dis[st] = 0;
	while (Q.size()) {
		int s = Q.front(); Q.pop();
		for (int i = 1; i <= n; ++i) 
			if (s & (1 << (i - 1)))
				a[i] = 1;
			else a[i] = 0;
			
		for (int i = 1; i <= n; ++i) {
			int ss = 0;
			for (int j = 1; j <= i; ++j)
				tmp[j] = 1 - a[j];
			reverse(tmp + 1, tmp + i + 1);
			for (int j = 1; j <= i; ++j)
				ss |= tmp[j] * (1 << (j - 1));
			for (int j = i + 1; j <= n; ++j)
				ss |= a[j] * (1 << (j - 1));
			if (dis[s] + 1 < dis[ss]) {
				dis[ss] = dis[s] + 1;
				Q.push(ss);
			}
		}
	}
	printf("%d\n", dis[(1 << n) - 1]);
}
int main() {
	//freopen("B.in","r",stdin);
	//freopen("B.out","w",stdout);
	int T = 0;
	scanf("%d", &T);
	for (int i = 1; i <= T; ++i) {
		printf("Case #%d: ", i);
		work();
	}
}
