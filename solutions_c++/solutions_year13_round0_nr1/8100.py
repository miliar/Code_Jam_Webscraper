#include<cstdio>
int mat[4][4];
int T;
int tx,ty;
char c;
int won;
int completed=0;
void finish_it(){
	//row
	for(int i=0;i<4;i++){
		int mul=1;
		for(int k=0;k<4;k++)
			mul*=mat[i][k];
		if(mul==1){
			won=1;
			completed=1;
			return;
		}
		if(mul==16){
			won=2;
			completed=1;
			return;
		}
		if(mul==0)
			completed=0;
	}
	//col
	for(int i=0;i<4;i++){
		int mul=1;
		for(int k=0;k<4;k++)
			mul*=mat[k][i];
		if(mul==1){
			won=1;
			completed=1;
			return;
		}
		if(mul==16){
			completed=1;
			won=2;
			return;
		}
		if(mul==0)
			completed=0;
	}
	//diag
	int mul=1;
	for(int i=0;i<4;i++){
		mul*=-mat[i][i];
	}
	if(mul==1){
			completed=1;
		won=1;
		return;
	}
	if(mul==16){
			completed=1;
		won=2;
		return;
	}
	if(mul==0)
		completed=0;
	mul=1;
	for(int i=0;i<4;i++){
		mul*=mat[i][3-i];
	}
	if(mul==1){
			completed=1;
		won=1;
		return;
	}
	if(mul==16){
			completed=1;
		won=2;
		return;
	}
	if(mul==0)
		completed=0;
	return;
}
int main(){
	int T;
	scanf(" %d",&T);
	for(int i=0;i<T;i++){
		//inp
		for(int j=0;j<4;j++)
			for(int k=0;k<4;k++){
				scanf(" %c",&c);
				if(c=='X')
					mat[j][k]=1;
				else if(c=='T'){
					mat[j][k]=-1;
					tx=j;ty=k;
				}
				else if(c=='.')
					mat[j][k]=0;
				else if(c=='O')
					mat[j][k]=2;
			}
			/*
		for(int j=0;j<4;j++,printf("\n"))
			for(int k=0;k<4;k++)
				printf("%d ",mat[j][k]);
			*/
		won=-2;
		completed=1;
		mat[tx][ty]=1;
		finish_it();
		if(won==-2){
			completed=1;
			mat[tx][ty]=2;
			finish_it();
		}
		printf("Case #%d: ",i+1);
		if(completed){
			if(won==1)
				printf("X won\n");
			if(won==2)
				printf("O won\n");
			if(won==-2)
				printf("Draw\n");
		}
		else{
			printf("Game has not completed\n");
		}

	}
	return 0;
}