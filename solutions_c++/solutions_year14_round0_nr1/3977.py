#include<bits/stdc++.h>
#define si(n) scanf("%d",&n);
#define sl(n) scanf("%lld",&n);
#define ss(n) scanf("%s",n);
#define fr(i, n) for(i = 0; i < n; i++)
#define ms(i, n) memset(i, n, sizeof(i))
typedef long long LL; 
using namespace std;
int main () {
	//freopen ("input.txt","r",stdin);
	//freopen ("codejamoutput.txt","w",stdout);
	int t, u, n, a, m, i, j, cnt[20], ans;
	si(t);
	u = t;
	while (t--) {
		si(n);
		--n;
		ms(cnt, 0);
		ans = 0;
		fr(i, 4) {
			fr(j, 4) {
				si(a);
				if(i == n)
					cnt[a]++;
			}
		}
		si(m);
		--m;
		fr(i, 4) {
			fr(j, 4) {
				si(a);
				if(i == m)
					cnt[a]++;
			}
		}
		fr(i, 17) {
			if(cnt[i] == 2)
				ans++;
		}
		if(ans == 0) 
			printf("Case #%d: Volunteer cheated!\n", u - t);
		else if (ans > 1) 
			printf("Case #%d: Bad magician!\n", u - t);
		else {
			fr(i, 17)
				if(cnt[i] == 2)
					printf("Case #%d: %d\n", u - t, i);
		}
	}
	return 0;
}

