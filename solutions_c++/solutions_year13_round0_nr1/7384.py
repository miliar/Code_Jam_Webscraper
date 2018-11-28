#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
class gato{
	public:
	char mat[5][5];
	gato(){
		memset(mat,0,sizeof(mat));
	}
	void read(){
		for(int i=0;i<4;i++){
			scanf("%s",mat[i]);
		}
	}
	bool empate(){
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				if(mat[i][j]=='.')
					return false;
			}
		}
		return true;
	}
	bool gana(char a){
		for(int i=0;i<4;i++){
			for(int j=0;j<=4;j++){
				if(j==4) return true;
				if(mat[i][j]!=a && mat[i][j]!='T') break; 
			}
			for(int j=0;j<=4;j++){
				if(j==4) return true;
				if(mat[j][i]!=a && mat[j][i]!='T') break; 
			}
		}
		for(int i=0;i<=4;i++){
			if(i==4) return true;
			if(mat[i][i]!=a && mat[i][i]!='T') break; 
		}
		for(int i=0;i<=4;i++){
			if(i==4) return true;
			if(mat[3-i][i]!=a && mat[3-i][i]!='T') break; 
		}
		return false;
	}
	void print(){
		for(int i=0;i<4;i++){
			fflush(stdin);
			for(int j=0;j<4;j++){
				printf("%c",mat[i][j]);
			}
			printf("\n");
		}
	}
};
int main(){
	int t;
	char otro[10];
	scanf("%d",&t);
	for(int i=1;i<=t;i++){
		gato g;
		printf("Case #%d: ",i);
		g.read();
		//g.print();
		if(g.gana('X'))
			printf("X won");
		else
			if(g.gana('O'))
				printf("O won");
			else
				if(g.empate())
					printf("Draw");
				else
					printf("Game has not completed");
		if(i!=t){
			printf("\n");
		}
		while('\n'!=getchar());
	}
	return 0;
}