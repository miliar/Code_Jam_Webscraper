#include<stdio.h>

int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("output.txt","w",stdout);
	int t,t2,p,n,i,j;
	int cnt[16]={0},c2=0;
	scanf("%d",&t);
	for(t2=1;t2<=t;t2++){
		scanf("%d",&n);
		for(i=0;i<4;i++){
			for(j=0;j<4;j++){
				if(i==n-1){
					scanf("%d",&p);
					cnt[p-1]++;
				}
				else scanf("%*d");
			}
		}
		scanf("%d",&n);
		for(i=0;i<4;i++){
			for(j=0;j<4;j++){
				if(i==n-1){
					scanf("%d",&p);
					cnt[p-1]++;
					if(cnt[p-1]==2){
						if(!c2) c2 = p;
						else c2 = 100;
					}
				}
				else scanf("%*d");
			}
		}
		if(!c2)	printf("Case #%d: Volunteer cheated!\n",t2);
		else if(c2<=16)	printf("Case #%d: %d\n",t2,c2);
		else printf("Case #%d: Bad magician!\n",t2);

		for(i=0;i<16;i++) cnt[i] = 0;
		c2=0;
	}
	return 0;
}