#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int T;
int N=4;
char map[10][10];

char isCheck(char a, char b,char c,char d){

	char aA;

	if(a != 'T') aA=a;
	if(b != 'T') aA=b;
	if(c != 'T') aA=c;
	if(d != 'T') aA=d;

	if(a == 'T') a=aA;
	if(b == 'T') b=aA;
	if(c == 'T') c=aA;
	if(d == 'T') d=aA;

	if(a==b && a==c && a==d && a!='.' && a!='T') return aA;
	return 0;
}

int main()
{
	int t,i,j;
	char ans;
	FILE *in=fopen("input.txt","r");
	FILE *out=fopen("output.txt","w");
	fscanf(in,"%d",&T);
	for(t=1;t<=T;t++){
		ans=0;
		for(i=0;i<4;i++) fscanf(in,"%s",map[i]);

		for(i=0;i<4;i++){
			if( isCheck(map[i][0],map[i][1],map[i][2],map[i][3]) ) {
				ans = isCheck(map[i][0],map[i][1],map[i][2],map[i][3]);
			}
		}
		
		for(i=0;i<4;i++){
			if( isCheck(map[0][i],map[1][i],map[2][i],map[3][i]) ) {
				ans = isCheck(map[0][i],map[1][i],map[2][i],map[3][i]);
			}
		}
		if(!ans) ans = isCheck(map[0][0],map[1][1],map[2][2],map[3][3]);
		if(!ans) ans = isCheck(map[0][3],map[1][2],map[2][1],map[3][0]);
		
		fprintf(out,"Case #%d: ",t);
		if(!ans){
			bool f=0;
			for(i=0;i<4;i++)
				for(j=0;j<4;j++){
					if(map[i][j]=='.') f=1;
				}
			if(f) fprintf(out,"Game has not completed\n");
			else fprintf(out,"Draw\n");
		}
		else{
			fprintf(out,"%c won\n",ans);
		}



	}
	return 0;
}