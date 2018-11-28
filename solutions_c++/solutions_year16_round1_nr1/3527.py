#include <bits/stdc++.h>
using namespace std;

#define FOR(i,n) for(int i=0;i<n;++i)



int main(void) {
	int t;
	scanf("%d\n",&t);
	for(int tt=1;tt<=t;++tt) {
		char s[5000];
		scanf("%s\n",s);
		//printf("%s\n",s);
		vector<pair<char,int> > v;
		int l = strlen(s);
		FOR(i,l) v.push_back({s[i],i});
		sort(v.rbegin(),v.rend());
		char ans[5000];
		ans[l] = 0;
		int cur = l;
		int b = 0;
		int e = l-1;
		for(auto x:v) {
			//printf("%d\n",x.second);
			if(x.second <= cur) {
				ans[b] = x.first;
				++b;
				//printf("set %c to %d\n",ans[b-1],b-1);
				for(int j=cur-1;j>=x.second+1;--j,--e) {
					//printf("copy %c to %d\n",s[j],j);
					ans[e] = s[j];
				}
				cur = x.second;
			}
		}
		printf("Case #%d: %s\n",tt,ans);
	}
	
	
	
	
}
