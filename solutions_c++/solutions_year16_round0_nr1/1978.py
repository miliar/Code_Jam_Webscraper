#include <iostream>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>

using namespace std;

int T,N;

bool vis[10];

int main() {
	freopen("1B.in","r",stdin);
	freopen("1B.out","w",stdout);
	scanf("%d",&T);
	for (int kase = 1;kase <= T; kase++) {
		scanf("%d",&N);
		if (N == 0) printf("Case #%d: INSOMNIA\n",kase);
		else {
			memset(vis,0,sizeof vis); 
			long long ans = 0,tot = 0;
			for (int j = 1;j <= 1000; j++) {
				long long w = N;
				w *= j;
				while (w) {
					if (!vis[w%10]) tot++,vis[w%10] = 1;
					w /= 10;
				}
				if (tot == 10) { ans = (long long)(N) * j;  break; }
			}
			if (ans != 0) printf("Case #%d: %lld\n",kase,ans);
			else printf("error\n");
		}
	}
	return 0;
}