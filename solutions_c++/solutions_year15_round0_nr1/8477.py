#include <bits/stdc++.h>
using namespace std;

int main(){
	long tc,n,cs=1; scanf("%ld",&tc);
	while(tc--){
		scanf("%ld%*c",&n);
		long tmp=0,ans=0;
		for(long i=0; i<=n; i++){
			char ch; scanf("%c",&ch);
			long now = ch-'0';
			if(tmp>=i) tmp += now;
			else ans += i-tmp, tmp = i+now;
		}
		printf("Case #%ld: %ld\n",cs++,ans);
	}
	return 0;
}