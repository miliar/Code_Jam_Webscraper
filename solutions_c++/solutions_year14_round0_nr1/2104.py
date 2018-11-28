#include<stdio.h>
int main(){
	int t,r1,r2,i,j,z,ans,c;
	scanf("%d",&t);
	for(z=1;z<=t;z++){
		int a[4][4]={0},b[4][4]={0};
		scanf("%d",&r1);
		r1--;
		for(i=0;i<4;i++)
			for(j=0;j<4;j++)
				scanf("%d",&a[i][j]);
		scanf("%d",&r2);
		r2--;
		for(i=0;i<4;i++)
			for(j=0;j<4;j++)
				scanf("%d",&b[i][j]);
		c=0;
		ans=0;
		for(i=0;i<4;i++)
			for(j=0;j<4;j++)
				if(a[r1][i]==b[r2][j]){
					c++;
					ans=a[r1][i];
				}
		if(!c)
			printf("Case #%d: Volunteer cheated!\n",z);
		else if(c==1)
			printf("Case #%d: %d\n",z,ans);
		else
			printf("Case #%d: Bad magician!\n",z);
	}
	return 0;
}
