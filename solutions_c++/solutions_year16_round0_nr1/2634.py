#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <queue>
#include <map>
#include <iostream>
using namespace std;

typedef long long ll;
bool vis[10];
int main() {
	freopen("A-large.txt","r",stdin);
    freopen("out.txt","w",stdout);
 	int T;
	cin >> T;
	int cas = 0;
	while(T --) {
		int n;
		memset(vis, 0, sizeof(vis));
		scanf("%d", &n);
		ll m = n;
		printf("Case #%d: ", ++ cas);
		if(m == 0) {
			puts("INSOMNIA");
			continue;
		}
		int cnt = 10;
		int top = 0;
		ll last = 0;
		while(cnt) {
			ll num = m * (++ top);
			last = num; 
			while(num) {
				int dig = num % 10;
				num /= 10;
				if(vis[dig] == 0) cnt --, vis[dig] = 1;
			}	
		}
		printf("%lld\n", last);
	}
}

