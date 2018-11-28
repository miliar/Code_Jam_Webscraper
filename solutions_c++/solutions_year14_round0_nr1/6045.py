#include <stdio.h>
#include <string.h>

int grid1[4][4];
int grid2[4][4];
int T;
int Ans1,Ans2;

int TestCase=0;
void make()
{
	scanf("%d", &Ans1); 
	for(int y=0;y<4;y++)
		for(int x=0;x<4;x++) { 
			scanf("%d",&grid1[y][x]);
		}
	
	scanf("%d", &Ans2);
	for(int y=0;y<4;y++)
		for(int x=0;x<4;x++){
			scanf("%d",&grid2[y][x]);
		}
	int cnt=0; //count 
	int num=0; // output num
	for(int i=0;i<4;i++) {
		for(int j=0;j<4;j++) {
			if(grid1[Ans1-1][i] == grid2[Ans2-1][j]) {
				cnt++;
				num=grid1[Ans1-1][i];
			}
		}
	}
	char str[30];
	if(cnt==0){
		sprintf(str,"%s","Volunteer cheated!");
	}
	else if(cnt==1) {
		sprintf(str,"%d",num);
	}
	else{
		sprintf(str,"%s","Bad magician!");
	}
	

	printf("Case #%d: %s\n",++TestCase,str);
}

int main() {
	scanf("%d",&T);
	for(int i=0;i<T;i++)
	{
		make();
	}
	return 0;
}
