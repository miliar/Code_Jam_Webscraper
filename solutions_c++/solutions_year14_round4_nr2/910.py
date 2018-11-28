#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
const int inf=1000000000;
int i,j,k,n,m,a[111],b[111],c[111],tests,cc,ans,p;
int check(){
	int res,i,j;
	for (i=1;i<=n;i++) b[i]=a[c[i]];
	for (res=0,i=2;i<=n;i++)
	 for (j=1;j<i;j++)
	  if (c[j]>c[i]) res++;
	for (i=1;b[i]!=p;i++)
	 if (i>1&&b[i-1]>=b[i]) return inf;
	for (;i<n;i++)
	 if (b[i+1]>=b[i]) return inf;
//	if (res==6){
//		for (i=1;i<=n;i++) printf("%d ",b[i]);
//		puts("");
//	}
	return res;
}
int main(){
	scanf("%d",&tests);
	for (cc=1;cc<=tests;cc++){
		scanf("%d",&n);ans=inf;
		for (i=1,p=0;i<=n;i++) c[i]=i,scanf("%d",&a[i]),p=max(p,a[i]);
		while (1){
			ans=min(ans,check());
			if (!next_permutation(c+1,c+1+n)) break;
		}
		printf("Case #%d: %d\n",cc,ans);
	}
	return 0;
}
