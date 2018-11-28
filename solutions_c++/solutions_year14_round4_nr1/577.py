#include <stdio.h>
#include <algorithm>
#include <string.h>
int n,su[10001];
bool check[10001];
int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int test,testt,n,m,i,j,print;
	scanf("%d",&testt);
	for(test=1;test<=testt;test++){
		scanf("%d %d",&n,&m);
		print=0;
		for(i=0;i<n;i++)
			scanf("%d",&su[i]);
		std::sort(su,su+n);
		memset(check,0,sizeof(check));
		for(i=n-1;i>=0;i--){
			if(check[i]) continue;
			for(j=i-1;j>=0;j--){
				if(!check[j] && su[i]+su[j]<=m)
					break;
			}
			print++;
			check[j]=1;
		}
		printf("Case #%d: %d\n",test,print);
	}
	return 0;
}
