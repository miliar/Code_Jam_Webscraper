#include<stdio.h>
int x,y,A[5][5],B[5][5];
int main()
{
	int t,count,who,test;
	scanf("%d",&t);
	for(test=1;test<=t;test++){
	count=0;
	scanf("%d",&x);	
	for(int i=1;i<=4;i++)for(int j=1;j<=4;j++)	scanf("%d",&A[i][j]);
	scanf("%d",&y);
	for(int i=1;i<=4;i++)for(int j=1;j<=4;j++)	scanf("%d",&B[i][j]);
	for(int i=1;i<=4;i++){
		for(int j=1;j<=4;j++){
			if(A[x][i]==B[y][j]){
				who=A[x][i];
				count++;
				break;
			}
		}
	}	
	if(count==0){
		printf("Case #%d: Volunteer cheated!\n",test);
	}
	else if(count==1){
		printf("Case #%d: %d\n",test,who);
	}
	else{
		printf("Case #%d: Bad magician!\n",test);
	}
	}
	return 0;
}
