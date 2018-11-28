#include <stdio.h>
#include <string.h>
#define ZERO 0
#define EX 1
#define T 2
#define EMPTY 3

int getNextChar(){
	char c=0;
	while(c!='X' && c!='O' && c!='T' && c!='.')
		scanf("%c",&c);
	if(c=='X') return EX;
	if(c=='O') return ZERO;
	if(c=='.') return EMPTY;
	if(c=='T') return T;
}

int a[4][4],nrt;

int analyze(){

	int totalZero=0,totalX=0;
	bool complete=true;
	for(int i=0;i<4;i++){
		int z=0,x=0;
		for(int j=0;j<4;j++){
			if(a[i][j]==ZERO)
				z++;
			if(a[i][j]==EX)
				x++;
			if(a[i][j]==T){
				z++;x++;
			}
			if(a[i][j]==EMPTY)
				complete=false;
		}
		if(x==4) totalX++;
		else if(z==4) totalZero++;
		z=0,x=0;
		for(int j=0;j<4;j++){
			if(a[j][i]==ZERO)
				z++;
			if(a[j][i]==EX)
				x++;
			if(a[j][i]==T){
				z++;x++;
			}
		}
		if(x==4) totalX++;
		else if(z==4) totalZero++;
	}
	int z=0,x=0;
	for(int i=0;i<4;i++){
		if(a[i][i]==ZERO)
			z++;
		if(a[i][i]==EX)
			x++;
		if(a[i][i]==T){
			z++;x++;
		}
	}
	if(x==4) totalX++;
		else if(z==4) totalZero++;

	z=0,x=0;
	for(int i=0;i<4;i++){
		if(a[i][3-i]==ZERO)
			z++;
		if(a[i][3-i]==EX)
			x++;
		if(a[i][3-i]==T){
			z++;x++;
		}
	}
	if(x==4) totalX++;
		else if(z==4) totalZero++;
		if(totalZero>0) return ZERO;
		if(totalX>0) return EX;
	if(complete)
		return T;
	return EMPTY;
}

int main(){
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d",&nrt);
	for(int it=0;it<nrt;it++){
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				a[i][j]=getNextChar();
		int rez = analyze();
		printf("Case #%d: ",it+1);
		if(rez==ZERO) printf("O won\n");
		if(rez==EX) printf("X won\n");
		if(rez==T) printf("Draw\n");
		if(rez==EMPTY) printf("Game has not completed\n");
	}
	return 0;
}