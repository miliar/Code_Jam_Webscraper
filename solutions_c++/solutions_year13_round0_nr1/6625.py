//============================================================================
// Name        : CodeJam2013.cpp
// Author      : Gaurav
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include<iostream>
#include<stdio.h>
#include<algorithm>

#include<vector>
#include<stack>
#include<math.h>
using namespace std;

void eval(char arr[4][4]){
	int i,j,k,ti,tj;
	bool check=false;
	for(i=0;i<4;i++)for(j=0;j<4;j++){
		if(arr[i][j]=='T'){
			ti=i;tj=j;arr[i][j]='X';
			check=true;
			goto out;
		}
	}
	out:;
	for(i=0;i<4;i++){
		if(arr[i][0]==arr[i][1] && arr[i][1]==arr[i][2] && arr[i][2]==arr[i][3] && arr[i][3]=='X')
		{
			printf("X won\n");
			return;
		}
	}
	for(i=0;i<4;i++)
		if(arr[0][i]==arr[1][i] && arr[1][i]==arr[2][i] && arr[2][i]==arr[3][i] && arr[3][i]=='X')
		{
			printf("X won\n");
			return;
		}
	if(arr[0][0]==arr[1][1] && arr[1][1]==arr[2][2] && arr[2][2]==arr[3][3] && arr[3][3]=='X')
	{
		printf("X won\n");
		return;
	}
	if(arr[0][3]==arr[1][2] && arr[1][2]==arr[2][1] && arr[2][1]==arr[3][0] && arr[3][0]=='X')
	{
		printf("X won\n");
		return;
	}

	if(check==true)
	arr[ti][tj]='O';

	for(i=0;i<4;i++){
		if(arr[i][0]==arr[i][1] && arr[i][1]==arr[i][2] && arr[i][2]==arr[i][3] && arr[i][3]=='O')
		{
			printf("O won\n");
			return;
		}
	}
	for(i=0;i<4;i++)
		if(arr[0][i]==arr[1][i] && arr[1][i]==arr[2][i] && arr[2][i]==arr[3][i] && arr[3][i]=='O')
		{
			printf("O won\n");
			return;
		}
	if(arr[0][0]==arr[1][1] && arr[1][1]==arr[2][2] && arr[2][2]==arr[3][3] && arr[3][3]=='O')
	{
		printf("O won\n");
		return;
	}
	if(arr[0][3]==arr[1][2] && arr[1][2]==arr[2][1] && arr[2][1]==arr[3][0] && arr[3][0]=='O')
	{
		printf("O won\n");
		return;
	}

	for(i=0;i<4;i++)for(j=0;j<4;j++){
		if(arr[i][j]=='.'){
			printf("Game has not completed\n");
			return;
		}
	}
	printf("Draw\n");

}

int main() {
	char arr[4][4],c;
	int i,j,k,T;
	scanf("%d",&T);

	for(i=0;i<T;i++){
		scanf("%c",&c);
		for(j=0;j<4;j++){
			for(k=0;k<4;k++){
				scanf("%c",&arr[j][k]);
			}
			scanf("%c",&c);
		}
		printf("Case #%d: ",i+1);
		eval(arr);
	}
}
