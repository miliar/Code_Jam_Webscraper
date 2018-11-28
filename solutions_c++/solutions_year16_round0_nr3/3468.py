#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;
#define LL long long

int n,J,cnt;
int a[20];
LL ans[60][12];
int test(int base){
	LL sum=0;
	for (int i=n;i>=1;i--){
		sum=sum*base + a[i];
	}
	LL Min=min(1000LL,sum-1);
	for (int i=2;i<=Min;i++){
		if (sum%i==0) return i;
	}
	return 0;
}

void dfs(int i){
	if (i==n){
		a[i]=1;
		dfs(i-1);

		return ;
	}
	if (i==1){
		a[i]=1;
		int k=0;
		for (int j=2;j<=10;j++){
			k=test(j);
			if (k==0) break;
			ans[cnt][j]=k;
		}
		if (k!=0){
			for (int j=n;j>=1;j--){	
				ans[cnt][0]=ans[cnt][0]*10+a[j];
			}
			cnt++;
		}
		return ;
	}

	if (1<i && i<n){
		a[i]=1;
		dfs(i-1);

		if (cnt==J) return ;

		a[i]=0;
		dfs(i-1);

	}
	return ;
}

int main(){
	int cases;
	scanf("%d",&cases);
	for (int cas=1;cas<=cases;cas++){
		scanf("%d%d",&n,&J);

		cnt=0;
		dfs(n);
		printf("Case #%d:\n",cas);
		if (cnt==J){
			for (int i=0;i<J;i++){
				printf("%lld ",ans[i][0]);
				for (int j=2;j<=10;j++){
					printf("%lld%c",ans[i][j],j==10?'\n':' ');
				}
			}
		}
		else puts("I am wrong");
	}
	return 0;
}