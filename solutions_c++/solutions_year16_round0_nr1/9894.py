#include <bits/stdc++.h>
#define ll long long
#define sc(a) scanf("%lld", &a)
#define pr(a) printf("%lld\n", a)

using namespace std;

bool vis[10];

int main()
{
	ll cur,z,i,j,k,l,m,n,ct,t;
	freopen("A-large.in", "r", stdin);
	freopen("opt.txt", "w", stdout);
	sc(t);
	for (z = 1; z <= t; z++) {
		sc(n);
		cur = n;
		if (n == 0) {
			printf("Case #%lld: INSOMNIA\n", z);
		}
		else {
			for (i = 0; i < 10; i++) 
				vis[i] = 0;
			ct=0;
			while (ct < 10) {
				m = cur;
				while (m) {
					k = m%10;
					if (vis[k] == 0) {
						vis[k] = 1;
						ct++;
					}
					m /= 10;
				}
				cur += n;
			}
			printf("Case #%lld: %lld\n", z, cur-n);
		}
	}

 	return 0;
}

