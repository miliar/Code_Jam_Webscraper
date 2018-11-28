#include<cstdio>
#include<cstring>
#include<algorithm>
#include<vector>
#include<queue>
#define INF 2000000000
#define x first
#define y second
using namespace std;

int t;
char table[5][5];

int main(){
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d",&t);
	for(int q=1;q<=t;q++){
		bool Game_ncp = false,XWIN = false,YWIN = false;
		for(int i=0;i<4;i++){
			scanf("%s",table[i]);
		}
		for(int i=0;i<4;i++){
			int X_h = 0,Y_h = 0,T_h = 0;
			int X_v = 0,Y_v = 0,T_v = 0;
			for(int j=0;j<4;j++){
				if(table[i][j]=='X')
					X_h++;
				else if(table[i][j]=='O')
					Y_h++;
				else if(table[i][j]=='T')
					T_h++;
			}
			//printf("%d %d\n",X_h,Y_h);
			if(X_h==4 || (X_h==3&&T_h==1)){
				XWIN = true;
				break;
			}
			if(Y_h==4 || (Y_h==3&&T_h==1)){
				YWIN = true;
				break;
			}
			for(int j=0;j<4;j++){
				if(table[j][i]=='X')
					X_v++;
				else if(table[j][i]=='O')
					Y_v++;
				else if(table[j][i]=='T')
					T_v++;
			}
			if(X_v==4 || (X_v==3&&T_v==1)){
				XWIN = true;
				break;
			}
			if(Y_v==4 || (Y_v==3&&T_v==1)){
				YWIN = true;
				break;
			}
		}
		if(!XWIN && !YWIN){
			int X=0,Y=0,T=0;
			for(int i=0;i<4;i++){
				if(table[i][i]=='X')
					X++;
				else if(table[i][i]=='O')
					Y++;
				else if(table[i][i]=='T')
					T++;
			}
			if(X==4 || (X==3&&T==1)){
				XWIN = true;
			}
			else if(Y==4 || (Y==3&&T==1)){
				YWIN = true;
			}
			else{
				X = 0; Y=0; T=0;
				for(int i=0;i<4;i++){
					if(table[i][3-i]=='X')
						X++;
					else if(table[i][3-i]=='O')
						Y++;
					else if(table[i][3-i]=='T')
						T++;
				}
				//printf("DDD%d %d %d\n",X,Y,T);
				if(X==4 || (X==3&&T==1)){
					XWIN = true;
				}
				else if(Y==4 || (Y==3&&T==1)){
					YWIN = true;
				}
			}
		}
		printf("Case #%d: ",q);
		if(XWIN){
			printf("X won\n");
		}
		else if(YWIN){
			printf("O won\n");
		}
		else{
			bool CP = true;
			for(int i=0;i<4;i++){
				if(!CP)
					break;
				for(int j=0;j<4;j++){
					if(table[i][j]=='.'){
						CP = false;
						break;
					}
				}
			}
			if(CP == true)
				printf("Draw\n");
			else
				printf("Game has not completed\n");
		}
		//printf("%d %d\n",XWIN,YWIN);
	}
}
