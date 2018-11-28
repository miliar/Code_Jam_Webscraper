#include<stdio.h>
using namespace std;
int p[1000];

int min(int a,int b){return a<b?a:b;}

int main(){
	int dn;
	scanf("%d",&dn);
	for(int di=0;di<dn;di++){
		int n,i;
		scanf("%d",&n);
		for(i=0;i<n;i++)scanf("%d",&p[i]);
		int ans=1000;
		for(int m=1;m<=1000;m++){
			int s=0;
			for(i=0;i<n;i++)if(p[i]>m)s+=(p[i]-m-1)/m+1;
			ans=min(ans,m+s);
		}
		printf("Case #%d: %d\n",di+1,ans);
	}
	return 0;
}