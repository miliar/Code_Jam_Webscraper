#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

typedef long long ll;
int T;
int s[1100],smax;
char in[1100];

int main() {
	scanf("%d",&T);
	for(int tt=1; tt<=T; tt++) {
		scanf("%d %s",&smax,in);
		for(int i=0; i<=smax; i++)
			s[i] = in[i] - '0';
		ll ans=0,sum=s[0];
		for(int i=1; i<=smax; i++) {
			if(ans+sum >= smax) break;
			if(s[i] && ans+sum < i)
				ans+=i-sum-ans;
			sum+=s[i];
		}
		printf("Case #%d: %lld\n",tt,ans);
	}
	return 0;
}
