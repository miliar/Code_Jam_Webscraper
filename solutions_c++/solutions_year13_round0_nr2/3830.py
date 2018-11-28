#include<iostream>
#include<cstring>
#include<cstdio>
#include<string>
using namespace std;





bool check(){

	int board[110][110],rows,columns,i,j;


	scanf("%d%d",&rows,&columns);

	int minX[110]={100},minY[110]={100};
	int maxX[110]={0},maxY[110]={0};



	for(j=0;j<rows;j++){
		for(i=0;i<columns;i++){
			scanf("%d",&board[j][i]);

			minX[j]=(minX[j]>board[j][i])? board[j][i] : minX[j];
			maxX[j]=(maxX[j]<board[j][i])? board[j][i] : maxX[j];

			minY[i]=(minY[i]>board[j][i])? board[j][i] : minY[i];
			maxY[i]=(maxY[i]<board[j][i])? board[j][i] : maxY[i];
			
		}

	}


	for(j=0;j<rows;j++){
		for(i=0;i<columns;i++){
			if(
				(board[j][0]>board[j][i] && board[j][columns-1]>board[j][i])
				&&
				(board[0][i]>board[j][i] && board[rows-1][i]>board[j][i])
				){
				return false;
			}

			if(maxY[i]>board[j][i] && maxX[j]>board[j][i]){
				return false;
			}
			
			
		}
	}


	return true;
}

int main(){

	int cases,i;

	freopen("in.in","r",stdin);
	freopen("out.txt","w",stdout);

	scanf("%d",&cases);

	for(i=1;i<=cases;i++){

		if(check()){
			printf("Case #%d: YES\n",i);
		}else{
			printf("Case #%d: NO\n",i);
		}
	}



	return 0;
}