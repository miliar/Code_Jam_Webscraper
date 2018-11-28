#include <bits/stdc++.h>
using namespace std;

#define ll long long int
#define pb(x) push_back(x)
#define mp(i,j) make_pair(i,j)
#define MAXN 100010
#define MOD 1000000007

int main()
{
	ll i,j,k,n,t,num;
	ll cnt[10];

	scanf("%lld", &t);

	for(i=1;i<=t;i++) {
		scanf("%lld", &n);
		memset(cnt,0,sizeof(cnt));
		for(j=n;j>0;j+=n) {
			num = j;
			while(num!=0) {
				cnt[(num%10)]++;
				num/=10;
			}
			for(k=0;k<10;k++) {
				if(cnt[k]==0) break;
			}

			if(k==10) {
				printf("Case #%lld: %lld\n", i,j);
				break;
			}
		}
		if(j<=0) {
			printf("Case #%lld: INSOMNIA\n", i);
		}
	}

	return 0;
}
