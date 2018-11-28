#include<cstdio>
#include<cstdlib>
#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

int main(void){
	int cases;
	int board[4][4];
	int vec1[4];
	int vec2[4];
	scanf("%d",&cases);
	int count=1;
	for(int i=0;i<cases;i++){
	
		int row1,row2;
		
		scanf("%d",&row1);
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				scanf("%d",&board[i][j]);
			}
		}
		for(int i=0;i<4;i++){
			vec1[i]=board[row1-1][i];
		}
		
		scanf("%d",&row2);
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				scanf("%d",&board[i][j]);
			}
		}
		for(int i=0;i<4;i++){
			vec2[i]=board[row2-1][i];
		}
		int card;
		int times=0;
		
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				if(vec1[i]==vec2[j]){
					times++;
					if(times==1)card=vec1[i];
				}
			}	
		}
		printf("Case #%d: ",count);
		if(times>1){
			printf("Bad magician!\n");
		}else if (times==1){
			printf("%d\n",card);
		}else if (times==0){
			printf("Volunteer cheated!\n");
		}
		count++;
		}
	}
	
	
	


