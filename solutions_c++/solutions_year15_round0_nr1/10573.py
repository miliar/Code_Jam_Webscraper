#include <bits/stdc++.h>
using namespace std;

int main() {
	int ans, sum, t, k,i, cnt=0;
	char a[1003];
	scanf("%d", &t);
	while(t--){
		++cnt;
		ans = 0;
		scanf("%d",&k);
		scanf(" %s",a);
		sum = a[0] - '0';
		for(i = 1; i <= k; ++i){
			if(a[i]!='0'){
				if(i > sum){
					ans+=i-sum;
					sum+=ans;
				}
				sum+=a[i]-'0';
			}
		}
		printf("Case #%d: %d\n",cnt,ans);
	}
	return 0;
}