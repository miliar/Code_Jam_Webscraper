#include<cstdio>
#include<cstdlib>
char s[4][4];
int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int T,i,j,ca=1;
	bool fx,fo,fp;
	scanf("%d",&T);
	while(T--){
		for(i=0;i<4;i++)scanf("%s",s[i]);
		printf("Case #%d: ",ca++);
		fp=1;
		for(i=0;i<4;i++){
			fx=1,fo=1;
			for(j=0;j<4;j++){
				if(s[i][j]=='.'){fp=0,fx=0,fo=0;break;}
				else if(s[i][j]=='X')fo=0;
				else if(s[i][j]=='O')fx=0;
			}
			if(fx){puts("X won");break;}
			if(fo){puts("O won");break;}
		}
		if(fx||fo)continue;
		for(i=0;i<4;i++){
			fx=1,fo=1;
			for(j=0;j<4;j++){
				if(s[j][i]=='.'){fp=0,fx=0,fo=0;break;}
				else if(s[j][i]=='X')fo=0;
				else if(s[j][i]=='O')fx=0;
			}
			if(fx){puts("X won");break;}
			if(fo){puts("O won");break;}
		}
		if(fx||fo)continue;
		fx=1,fo=1;
		for(i=0;i<4;i++){
			if(s[i][i]=='.'){fp=0,fx=0,fo=0;break;}
			else if(s[i][i]=='X')fo=0;
			else if(s[i][i]=='O')fx=0;
		}
		if(fx){puts("X won");continue;}
		if(fo){puts("O won");continue;}
		fx=1,fo=1;
		for(i=0;i<4;i++){
			if(s[3-i][i]=='.'){fp=0,fx=0,fo=0;break;}
			else if(s[3-i][i]=='X')fo=0;
			else if(s[3-i][i]=='O')fx=0;
		}
		if(fx){puts("X won");continue;}
		if(fo){puts("O won");continue;}
		if(fp)puts("Draw");
		else puts("Game has not completed");
	}
	return 0;
}