#include<stdio.h>
int N,M;
char s[111][111];
bool chk(int x,int y,char c){
//	fprintf(stderr,"chk %d %d %c\n",x,y,c);
	int dx,dy;
	if(c=='^'){
		dx=-1; dy=0;
	}else
	if(c=='v'){
		dx=1; dy=0;
	}else
	if(c=='<'){
		dx=0; dy=-1;
	}else
	if(c=='>'){
		dx=0; dy=1;
	}
	while(true){
		x+=dx;
		y+=dy;
		if(x<0 || x>=N || y<0 || y>=M)
			return false;
		if(s[x][y]!='.'){
//			fprintf(stderr,"%d %d\n",x,y);
			return true;
		}
	}
}
bool check(){
	int res=0;
	for(int i=0; i<N; i++)
		for(int j=0; j<M; j++)
			if(s[i][j]!='.'){
				if(!chk(i,j,'^') && !chk(i,j,'v')
				&& !chk(i,j,'<') && !chk(i,j,'>'))
					return false;
				if(!chk(i,j,s[i][j]))
					res++;
			}
	printf("%d\n",res);
	return true;
}
int main(){
	int _,T;
	scanf("%d",&_);
	for(T=1; T<=_; T++){
		scanf("%d%d",&N,&M);
		for(int i=0; i<N; i++)
			scanf("%s",s[i]);
		printf("Case #%d: ",T);
		if(!check())
			puts("IMPOSSIBLE");
//		fprintf(stderr,"===\n");
	}
	return 0;
}
