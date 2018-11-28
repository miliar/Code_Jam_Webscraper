#include<stdio.h>
int test,Case,first[4][4],second[4][4],R1,R2,count,i,j,ans;
int main(){
//	freopen("A-small-attempt1.in","r",stdin);
//	freopen("out.txt","w",stdout);
	scanf("%d",&test);
	for(Case=1;Case<=test;Case++){
		printf("Case #%d: ",Case);
		scanf("%d",&R1);
		for(i=0;i<4;i++)for(j=0;j<4;j++)scanf("%d",&first[i][j]);
		scanf("%d",&R2);
		R1--,R2--;
		for(i=0;i<4;i++)for(j=0;j<4;j++)scanf("%d",&second[i][j]);
		for(i=0;i<4;i++){
			for(j=0;j<4;j++)
				if(first[R1][i]==second[R2][j]){
					ans=first[R1][i];
					count++;
					if(count>1)goto done;
				}
		}
done:
		if(count==0)printf("Volunteer cheated!\n");
		else if(count==1)printf("%d\n",ans);
		else printf("Bad magician!\n");
		count=0;
	}
}