#include "stdio.h"
#include "conio.h"

void fill(int prevRow[4],int arr[][4],int row){
	
	for(int i=0;i<4;i++)
		prevRow[i]=arr[row][i];
	
}

int search(int arr[][4],int prevRow[],int r){
	int count=0,n;
	printf("\nr:%d",r);
	for(int i=0;i<4;i++){
		for(int j=0;j<4;j++){
			printf("\n%d %d",arr[r][i],prevRow[i]);
			if(arr[r][j]==prevRow[i]){
				count++;
				n=prevRow[i];
			}
		}
	}
	if(count>1)
		return -1;
	else if(count==0)
		return -2;
	return n;
}

int main(){
	int t=0,arr[4][4],prevRow[4],firstRow=0, secondRow=0, Case[100],i,j;
	
	scanf_s("%d",&t);
	int cases=0;
	while(cases<t){
		scanf_s("%d",&firstRow);
		fflush(stdin);
		for( i=0;i<4;i++)
			for( j=0;j<4;j++)
				scanf_s("%d",&arr[i][j]);
		fill(prevRow,arr,firstRow-1);
		scanf_s("%d",&secondRow);
		for( i=0;i<4;i++)
			for( j=0;j<4;j++)
				scanf_s("%d",&arr[i][j]);
		Case[cases]=search(arr,prevRow,secondRow-1);
		cases++;
	}

	for(int i=0;i<t;i++){
		if(Case[i]==-1)
			printf("Case #%d: Bad magician!",i+1);
		else if(Case[i]==-2)
			printf("Case #%d: Volunteer cheated!",i+1);
		else
			printf("Case #%d: %d",i+1,Case[i]);
	}
	getch();
}