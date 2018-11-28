#include<iostream>
#include<cstdio>

using namespace std;

main(){
	int i,T,x,o,caso = 1;
	char c,m[5][5];
	bool win,ponto;
	scanf("%d",&T);
	while(T--){
		x = o = 0;
		win = false;ponto = false;
		for(i=0;i<4;++i){
			for(int j=0;j<4;++j){
				scanf(" %c",&c);
				if(c != '.'){
					if(c == 'X'){
						x++;
					}else if(c == 'O'){
						o++;
					}else{
						x++;
						o++;
					}
				}else{
					ponto = true;
				}
				m[i][j] = c;
			}
			if(x == 4 || o == 4){
				win = true;
				break;
			}
			x = o = 0;
		}
		if(win){
			i++;
			for(int j=0;j<(4-i)*4;++j){
				scanf(" %*c");
			}
			if(x==4){
				c = 'X';
			}else{
				c = 'O';
			}
			printf("Case #%d: %c won\n",caso++,c);
			continue;
		}

		//diagonal
		x = o = 0;
		for(int j=0;j<4;++j){
			//printf("-%c- ", m[j][j]);
			if(m[j][j] == '.'){
				break;
			}else{
				if(m[j][j] == 'X'){
					x++;
				}else if(m[j][j] == 'O'){
					o++;
				}else{
					x++;
					o++;
				}
			}
		}
		//printf("\n");
		if(x == 4 || o == 4){
			if(x==4){
				c = 'X';
			}else{
				c = 'O';
			}
			printf("Case #%d: %c won\n",caso++,c);
			continue;
		}
		/////
		x = o = 0;
		for(int j=0;j<4;++j){
			//printf("-%c- ", m[j][j]);
			if(m[j][3-j] == '.'){
				break;
			}else{
				if(m[j][3-j] == 'X'){
					x++;
				}else if(m[j][3-j] == 'O'){
					o++;
				}else{
					x++;
					o++;
				}
			}
		}
		//printf("\n");
		if(x == 4 || o == 4){
			if(x==4){
				c = 'X';
			}else{
				c = 'O';
			}
			printf("Case #%d: %c won\n",caso++,c);
			continue;
		}
		/////
		x = o = 0;
		for(i=0;i<4;++i){
			for(int j=0;j<4;++j){
				if(m[j][i] == '.'){
					break;
				}else{
					if(m[j][i] == 'X'){
						x++;
					}else if(m[j][i] == 'O'){
						//printf("%c ",m[j][i]);
						o++;
					}else{
						x++;
						o++;
					}
				}


			}
			if(x == 4 || o ==4)
				break;
			x = o = 0;
		}
		//printf("\n");
		if(x == 4 || o == 4){
			if(x==4){
				c = 'X';
			}else{
				c = 'O';
			}
			printf("Case #%d: %c won\n",caso++,c);
			continue;
		}
		/////

		if(ponto){
			printf("Case #%d: Game has not completed\n",caso++);
		}else{
			printf("Case #%d: Draw\n",caso++);
		}
		/*
		for(i=0;i<4;++i){
			for(int j=0;j<4;++j){
				printf("%c",m[i][j]);
			}
			printf("\n");
		}
		printf("\n");
		*/






	}




}
