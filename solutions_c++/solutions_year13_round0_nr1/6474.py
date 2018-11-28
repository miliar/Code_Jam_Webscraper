#include<stdio.h>
#include<iostream>
#include<string.h>
#include<stdlib.h>
#include<math.h>
#include<stack>
#include<queue>
#include<algorithm>
#define mem(a,b) memset(a,b,sizeof(a))
#define Max(a,b) ((a)>(b)?(a):(b))
#define Min(a,b) ((a)<(b)?(a):(b))
#define INF 0x3f3f3f3f
#define MAX 5
struct Point{
	int x,y;
}wellposition;
using namespace std;

char map[MAX][MAX];

int main(){
#ifndef ONLINE_JUDGE
	freopen("G:\\study\\programs\\test\\in.txt","r",stdin);
	freopen("G:\\study\\programs\\test\\out.txt","w",stdout);
#endif
	int num_text;
	int Xwin,Owin,win;
	int complete;
	int temp,temp2;
	int i,j,k = 0;
	scanf("%d",&num_text);
	getchar();
	while(k < num_text){
		k ++;
		printf("Case #%d: ",k);
		Xwin = Owin = 0;
		win = 1;
		complete = 1;
		for(i = 0;i < 4;++ i){
			for(j = 0;j < 4;++ j){
				scanf("%c",&map[i][j]);
				if(map[i][j] == '.') complete = 0;
			}
			getchar();
		}
		getchar();
		for(j = 0;j < 4;++ j){
			win = 1;
			if(map[0][j] != '.'){
				temp = map[0][j];
				for(i = 1;i < 4;++ i){
					if(map[i][j] == '.') {win = 0; break;}
					if(map[i][j] == 'T'){
						continue;
					}else if(map[i][j] != temp && temp != 'T'){
						win = 0;
						break;
					}
					temp = map[i][j];
				}
				if(win == 1){
					if(map[0][j] != 'T'){
						if(map[0][j] == 'X') Xwin = 1;
						else Owin = 1;
					}else if(map[0][j] == 'T'){
						if(map[1][j] == 'X') Xwin = 1;
						else Owin = 1;
					}
				}
			}
		}
		for(i = 0;i < 4;++ i){
			win = 1;
			if(map[i][0] != '.'){
				temp = map[i][0];
				for(j = 1;j < 4;++ j){
					if(map[i][j] == '.') {win = 0; break;}
					if(map[i][j] == 'T'){
						continue;
					}else if(map[i][j] != temp && temp != 'T'){
						win = 0;
						break;
					}
					temp = map[i][j];
				}
				if(win == 1){
					if(map[i][0] != 'T'){
						if(map[i][0] == 'X') Xwin = 1;
						else Owin = 1;
					}else if(map[i][0] == 'T'){
						if(map[i][1] == 'X') Xwin = 1;
						else Owin = 1;
					}
				}
			}
		}
		win = 1;
		if(map[0][0] != '.'){
			temp = map[0][0];
			for(i = 1;i < 4;++ i){
				if(map[i][i] == '.') {win = 0; break;}
				if(map[i][i] == 'T'){
					continue;
				}else if(map[i][i] != temp && temp != 'T'){
					win = 0;
					break;
				}
				temp = map[i][i];
			}
			if(win == 1){
				if(map[0][0] != 'T'){
					if(map[0][0] == 'X') Xwin = 1;
					else Owin = 1;
				}else if(map[0][0] == 'T'){
					if(map[1][1] == 'X') Xwin = 1;
					else Owin = 1;
				}
			}
		}
		win = 1;
			if(map[0][3] != '.'){
				temp = map[0][3];
				for(i = 1;i < 4;++ i){
					if(map[i][3 - i] == '.') {win = 0; break;}
					if(map[i][3 - i] == 'T'){
						continue;
					}else if(map[i][3 - i] != temp && temp != 'T'){
						win = 0;
						break;
					}
					temp = map[i][3 - i];
				}
			if(win == 1){
				if(map[0][3] != 'T'){
					if(map[0][3] == 'X') Xwin = 1;
					else Owin = 1;
				}else if(map[0][3] == 'T'){
					if(map[1][2] == 'X') Xwin = 1;
					else Owin = 1;
				}
			}
		}
		if(Xwin && Owin){
			printf("Draw\n");
		}else if(Xwin && !Owin){
			printf("X won\n");
		}else if(!Xwin && Owin){
			printf("O won\n");
		}else if(!Xwin && !Owin && complete){
			printf("Draw\n");
		}else printf("Game has not completed\n");
	}
	return 0;
}
