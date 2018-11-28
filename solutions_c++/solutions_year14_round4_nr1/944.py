#include <cstdio>
#include <cstring>
#include <iostream>
#include <set>
#include <functional>
#include <algorithm>

using namespace std;

int n,sum,ans;
multiset<int,greater<int> > c;

int main() {
	int t,tt,i,x;
	scanf("%d",&t);
	for (tt=1;tt<=t;tt++) {
		scanf("%d%d",&n,&sum);
		c.clear();
		ans=0;
		for (i=0;i<n;i++) {
			scanf("%d",&x);
			c.insert(x);
		}
		//for (multiset<int,greater<int> >::iterator it=c.begin();it!=c.end();it++) printf("%d\n",*it);
		while (c.size()!=0) {
			int tmp=sum-*(c.begin());
			c.erase(c.begin());
			ans++;
			if (c.lower_bound(tmp)!=c.end()) {
				c.erase(c.lower_bound(tmp));
			}
		}
		printf("Case #%d: %d\n",tt,ans);
	}
	return 0;
}
