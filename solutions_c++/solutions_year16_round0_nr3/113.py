#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <vector>
#include <iostream>
#define MAXN 100050
#define LL long long
using namespace std;
int n;
int m;
int a[33];
LL p[15][33];
LL ans[12];
int cnt=0;
bool check(int bas){
	LL val=0;
	for(int i=1;i<=n;++i){
		if(a[i]==1)
			val+=p[bas][i-1];
	}
//	printf("--%d ",bas);
//	for(int i=n;i>=1;--i)
//		printf("%d",a[i]);
//	printf(" %I64d\n",val);
	for(LL j=2;j*j<=val;++j){
		if(val%j==0){
			ans[bas]=j;
			return false;
		}
	}
	return true;
}
void dfs(int cur){
	if(cnt==m)return;
	if(cur==n){
		int flag=1;
		for(int i=2;i<=10;++i){
			if(check(i)){
				flag=0;
				break;
			}
		}

		if(flag){
			cnt++;
			for(int j=n;j>0;--j)
				printf("%d",a[j]);
			for(int j=n;j>0;--j)
				printf("%d",a[j]);
			for(int i=2;i<=10;++i)
				printf(" %I64d",ans[i]);
			puts("");
		}
		return;
	}
	a[cur]=0;
	dfs(cur+1);
	a[cur]=1;
	dfs(cur+1);
	a[cur]=0;

}
int main() {

	freopen("output2.txt","w",stdout);
	for(int i=1;i<=10;++i){
		p[i][0]=1;
		for(int j=1;j<=16;++j)
			p[i][j]=p[i][j-1]*i;
	}
	int tt,ri=0;
	scanf("%d",&tt);
	while(tt--){
		cnt=0;
		scanf("%d%d",&n,&m);
		printf("Case #%d:\n",++ri);
		a[1]=a[n]=1;
		dfs(2);
	}
	return 0;
}
