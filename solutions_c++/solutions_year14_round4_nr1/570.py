#include<cstdio>
#include<algorithm>
using namespace std;
int main(){
	int t,c,n,x,i,j,ans;
	int a[20000];
	scanf("%d",&t);
	for(c=1;c<=t;c++){
		scanf("%d%d",&n,&x);
		for(i=0;i<n;i++) scanf("%d",&a[i]);
		sort(a,a+n);
		j=n-1;
		ans=n;
		for(i=0;i<j;i++){
			while(a[i]+a[j]>x&&j>i) j--;
			if(j==i) break;
			j--;
			ans--;
		}
		printf("Case #%d: %d\n",c,ans);
	}
	return 0;
}