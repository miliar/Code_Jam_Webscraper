#include<stdio.h>
#include<string.h>
int main(){
	int N;
	while(scanf("%d",&N)!=EOF)
		for(int z=1;z<=N;z++){
			int quest;
			scanf("%d",&quest);
			int array[4][4];
			int check[20];
			memset(check,0,sizeof(check));
			for(int i=0;i<4;i++)
				for(int j=0;j<4;j++){
					scanf("%d",&array[i][j]);
					if(i==quest-1)
						check[array[i][j]]=1;
				}
			int temp=0;
			scanf("%d",&quest);
			for(int i=0;i<4;i++)
				for(int j=0;j<4;j++){
					scanf("%d",&array[i][j]);
					if(i==quest-1)
						if(check[array[i][j]]==1){
							check[array[i][j]]=2;
							temp++;
						}
				}
			printf("Case #%d: ",z);
			if(temp==1){
				for(int i=1;i<17;i++)
					if(check[i]==2)
						printf("%d\n",i);
			}
			else if(temp>1)
				puts("Bad magician!");
			else
				puts("Volunteer cheated!");
		}
	return 0;
}