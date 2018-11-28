#include <bits/stdc++.h>
using namespace std;

#define ll long long int

int main()
{
	ll i,j,t,s,n,cnt,ans;

	scanf("%lld", &t);

	for(i=1;i<=t;i++) {
		scanf("%lld", &s);
		char shy[s+5];

		scanf(" %s", shy);

		n = strlen(shy);

		cnt = 0;
		ans = 0;

		for(j=0;j<n;j++) {
			if(shy[j]!='0') {
				if(cnt>=j) {
					cnt = cnt +  (shy[j]-'0');
				} else {
					ans = ans + j-cnt;
					cnt = j + (shy[j]-'0');
				}
			}
		}
		printf("Case #%lld: %lld\n", i,ans);
	}
	return 0;
}
