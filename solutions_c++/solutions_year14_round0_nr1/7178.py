#include<stdio.h>
#include<stdlib.h>

int main()
{
	int t,a1,a2,i,j,c,a[4][4],b[4][4];
	scanf("%d",&t);
	for(c=1;c<=t;c++)
	{
		scanf("%d",&a1);
		for(i=0;i<4;i++){
			for(j=0;j<4;j++)
			scanf("%d",&a[i][j]);
		}
		
		scanf("%d",&a2);
		for(i=0;i<4;i++){
			for(j=0;j<4;j++)
			scanf("%d",&b[i][j]);
		}
		int match = 0;
		int num;
		for(i=0;i<4;i++){
			for(j=0;j<4;j++){
			if(a[a1-1][i]==b[a2-1][j]){
			num=a[a1-1][i];
			match++;              
			}
			}
		}
		
		if(match==0)
		printf("Case #%d: Volunteer cheated!\n",c);
		else if(match==1)
		printf("Case #%d: %d\n",c,num);
		else if(match>1 && match <=4)
		printf("Case #%d: Bad magician!\n",c);
	}
return 0;
}

