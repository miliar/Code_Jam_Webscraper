#include <iostream>
#include <cstring>
#include <cstdio>
#include <queue>
#include <vector>
using namespace std;
#define Maxn 1050
#define Maxp 1000
int a[Maxn];
int main(){
	int cases,n;
	scanf("%d",&cases);
	for (int cas=1;cas<=cases;cas++){
		scanf("%d",&n);
		for (int i=1;i<=n;i++){
			scanf("%d",&a[i]);
		}
		int ans=Maxp;
		for (int i=1;i<=Maxp;i++){
			int sum=i;
			for (int j=1;j<=n;j++){
				if (a[j]<=i) continue;
				if ((a[j]-i)%i==0) sum+=(a[j]-i)/i;
				else sum+=(a[j]-i)/i+1;
			}
			ans=min(ans,sum);
		}
		printf("Case #%d: %d\n",cas,ans);
	}
	return 0;
}