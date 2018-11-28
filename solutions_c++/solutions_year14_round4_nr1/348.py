#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<set>
using namespace std;

int bo[1000];

int main(){
		freopen("a.in","r",stdin);
		freopen("a.out","w",stdout);
	int T,ca=0;
	scanf("%d",&T);
	while (T--){
		int ans=0;
		int n,X;
		scanf("%d%d",&n,&X);
		for (int i=1; i<=n; ++i){
			int x;
			scanf("%d",&x);
		        ++bo[x];
		}
		for (int i=X; i; --i){
			if (!bo[i]) continue;
			++ans;
			--bo[i];
			for (int j=min(X-i,i); j;--j)
				if (bo[j]){
					--bo[j];
					break;
				}
			if (bo[i]) ++i;
		}
		printf("Case #%d: %d\n",++ca,ans);
	}
	return 0;
}
