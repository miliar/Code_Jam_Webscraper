#include <bits/stdc++.h>
using namespace std;
#define FOR(i,n) for(int i=0;i<n;++i)


int main(int argc, char** argv) {
	int t;
	scanf("%d\n",&t);
	for(int tt=1;tt<=t;++tt) {
		char s[1000];
		scanf("%s\n",s);
		int l = strlen(s);
		s[l]='+';
		int ans = 0;
		for(int i=l;i>0;--i) ans+=s[i]!=s[i-1]?1:0;
		printf("Case #%d: %d\n",tt,ans);
	}
		
	
	
}