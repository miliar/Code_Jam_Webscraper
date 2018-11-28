#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int f,a,e,v,i,j;
	int firstanswer,secondanswer;
	int first[4][4],second[4][4];
	int number,count=0;
	scanf("%d",&f);
	for(a=0;a<f;a++){
		count=0;
		scanf("%d",&firstanswer);
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
			scanf("%d",&first[i][j]);
			}
		}
		scanf("%d",&secondanswer);
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
			scanf("%d",&second[i][j]);
			}
		}
		/*
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
			printf("%d",second[i][j]);
			}
			printf("\n");
		}*/
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				if(first[firstanswer-1][i]==second[secondanswer-1][j])
				{
					//printf("lalla");
					//printf("%d",first[firstanswer-1][i]);
					number=first[firstanswer-1][i];
					count++;
					//printf("%d",number);
				}
			}
		}
		if(count==1){
			printf("Case #%d: %d\n",a+1,number);
		}
		else if(count>1){
			printf("Case #%d: Bad magician!\n",a+1);
		}
		else if(count==0){
			printf("Case #%d: Volunteer cheated!\n",a+1);
		}
	}

	return 0;
}