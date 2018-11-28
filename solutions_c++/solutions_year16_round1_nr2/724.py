#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <iostream>
#define LL long long
using namespace std;
int a[105][55];
int ans[55];
int q[5555];
int n;

int main() {
	freopen("B-large.in","r",stdin);
	freopen("output1.txt","w",stdout);
	int tt,ri=0;
	scanf("%d",&tt);
	while(tt--){
		scanf("%d",&n);
		int tail=0;
		for(int i=1;i<n*2;++i){
			for(int j=1;j<=n;++j){
				int x;
				scanf("%d",&x);
				q[tail++]=x;
			}
		}
		sort(q,q+tail);
		int k=0,m=0;
		for(int i=0;i<tail;++i){
			k++;
			if(i==tail-1||q[i]!=q[i+1]){
				if(k&1)
					ans[m++]=q[i];
				k=0;
			}
		}
		sort(ans,ans+m);
		printf("Case #%d:",++ri);
		for(int i=0;i<m;++i)
			printf(" %d",ans[i]);
		puts("");
	}
	return 0;
}
