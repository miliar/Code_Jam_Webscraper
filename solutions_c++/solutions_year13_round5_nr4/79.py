#include<cstdio>
#include<iostream>
#include<cstring>
#include<algorithm>
using namespace std;

int n, tar, sta;
bool vis[1 << 21];
double dp[1 << 21], f[1 << 21];
char s[55];

int main() {
	freopen("D-small-attempt0.in", "r", stdin);
	freopen("D-small.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int V = 1; V <= T; ++V) {
	  printf("Case #%d: ", V);
	  scanf("%s", s);
	  n = strlen(s);
	  tar = (1 << n) - 1;
	  memset(dp, 0, sizeof(dp));
	  memset(vis, 0, sizeof(vis));
	  memset(f, 0, sizeof(f));
		sta = 0;
	  for (int i = 0; i < n; ++i) {
	    sta <<= 1;
	    if (s[i] == 'X') ++sta;
		}
		vis[sta] = true;
		f[sta] = 1;
		for (int i = 0; i < tar; ++i) {
		  if (vis[i] == false) continue;
		  //cout << i << ' ' << dp[i] << endl;
		  int tmp = i;
		  for (int j = 0; j < n; ++j) {
		    int price = n, it = j;
		    while ((tmp >> it) % 2) {
		    	--price;
					it = it == 0 ? n - 1 : it - 1;
		  	}
		  	vis[tmp | (1 << it)] = true;
		  	dp[tmp | (1 << it)] += (dp[tmp] + price * f[tmp]) / n;
		  	f[tmp | (1 << it)] += f[tmp] / n;
		  	//cout << "##" << (tmp | (1 << it)) << ' ' << (dp[tmp] + price)  << endl;
			}
		}
	  printf("%.12lf\n", dp[tar]);
	}
	return 0;
}

