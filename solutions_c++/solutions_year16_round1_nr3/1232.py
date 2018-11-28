/*
By Tianyi Chen. All rights reserved.
Date: 2016-04-16
*/
#include<bits/stdc++.h>
using namespace std;
int T,n,bff[11],ans;
vector<int>perm;
int main() {
	freopen("D:/publish/GCJ/2016-1A/C.in","r",stdin);
	freopen("D:/publish/GCJ/2016-1A/C.out","w",stdout);
	scanf("%d",&T);for (int _=1;_<=T;++_) {
		ans=2;
		printf("Case #%d: ",_);
		scanf("%d",&n);for (int i=1;i<=n;++i)scanf("%d",bff+i);
		for (int i=1;i<1<<n;++i) {
			perm.clear();
			for (int j=0;j<n;++j)if (i>>j&1)perm.push_back(j+1);
			if (perm.size()<=ans)continue;
			do {
				if (bff[perm.front()]!=perm.back()&&bff[perm.front()]!=perm[1])continue;
				if (bff[perm.back()]!=perm.front()&&bff[perm.back()]!=perm[perm.size()-2])continue;
				for (int i=1;i<perm.size()-1;++i) {
					if (bff[perm[i]]!=perm[i+1]&&bff[perm[i]]!=perm[i-1])goto ntry;
				}
				ans=max(ans,(int)perm.size());
				break;
			ntry:;
			} while (next_permutation(perm.begin(),perm.end()));
		}
		printf("%d\n",ans);
	}
}