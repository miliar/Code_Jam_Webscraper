#include <stdio.h>
#include<iostream>
#include<algorithm>
#include<cstring>
#include<cstdlib>
using namespace std;
struct pp{
	int id,num;
}cnt[3000];
int cmp(pp a,pp b){
	if((a.num&1)&&(b.num&1)){
		return a.id<b.id;
	}
	return a.num&1;
}
int main(void)
{
	int t,cas=0;
	freopen("B-large.in","r",stdin);
	freopen("large.out","w",stdout);
	scanf("%d",&t);
	int n;
	while(t--){
		scanf("%d",&n);
		for(int i=1;i<=2900;i++){
			cnt[i].id=i;
			cnt[i].num=3000;
		}
		int a;
		for(int i=1;i<=2*n-1;i++){
			for(int j=1;j<=n;j++){
			scanf("%d",&a);
			if(cnt[a].num==5)cnt[a].num=0;
			cnt[a].num++;
			}
		}
		sort(cnt+1,cnt+1+2500,cmp);
		printf("Case #%d:",++cas);
		for(int i=1;i<=n;i++){
			printf(" %d",cnt[i].id);
		}
		puts("");
	}
	return 0;
}
