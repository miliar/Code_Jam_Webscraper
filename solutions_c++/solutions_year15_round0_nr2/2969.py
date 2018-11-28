#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cstring>
using namespace std;
#define maxn 1010
int a[maxn];
int main(){
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	int n,T;
	scanf("%d",&T);
	for (int _=1;_<=T;_++) {
		scanf("%d",&n);
		int mx=0;
		for (int i=1;i<=n;i++) {
			scanf("%d",a+i);
			mx=max(a[i],mx);
		}
		int ans=0x7fffffff;
		for (int i=1;i<=mx;i++) {
			int sum=0;
			for (int j=1;j<=n;j++) sum+=a[j]%i?a[j]/i:a[j]/i-1;
			ans=min(sum+i,ans);
		}	
		printf("Case #%d: %d",_,ans);
		if (_!=T) printf("\n");
	}
	return 0;
}
