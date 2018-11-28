#include <stdio.h>

int main(void)
{
	freopen("D-small-attempt0.in","r",stdin);
	freopen("d.out","w",stdout);
	int t,k,s,c;
	int cas=0;
	scanf("%d",&t);
	while(t--){
		scanf("%d%d%d",&k,&c,&s);
		printf("Case #%d:",++cas);
		for(int i=1;i<=s;i++){
			printf(" %d",i);
		}
		puts("");
	}
	return 0;
}
