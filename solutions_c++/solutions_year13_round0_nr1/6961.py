#include <iostream>
#include <cstdio>
#include <algorithm>

using namespace std;

int main() {
	int T;
	char a[4][4];
	int stat;
	int x,y,f;
	scanf("%d", &T);
	FILE *fp;
	fp = fopen("A-small.out","w");
	//fp = fopen("A.in","r");
	
	for(int t=1; t<=T; t++) {
		stat=3;
		f=0;
		for(int i=0; i<4; i++)
			scanf("%s", a[i]);
		for(int i=0; i<4; i++)
			for(int j=0; j<4; j++)
				if(a[i][j]=='T') {
					x=i;
					y=j;
					f=1;
				}
		if(f==1)
			a[x][y]='X';
		for(int i=0;i<4;i++) {
			if((a[i][0]=='X')&&(a[i][1]=='X')&&(a[i][2]=='X')&&(a[i][3]=='X'))
				{ stat=0; break; }
			if((a[0][i]=='X')&&(a[1][i]=='X')&&(a[2][i]=='X')&&(a[3][i]=='X'))
				{ stat=0; break; }
		}
		int c1=0,c2=0;
		for(int i=0;i<4;i++) {
			if(a[i][i]=='X')
				c1++;
			if(a[i][4-i-1]=='X')
				c2++;
		}
		if((c1==4)||(c2==4))
			stat=0;
		//printf("checked x");
		if(f==1)
			a[x][y]='O';
		for(int i=0;i<4;i++) {
			if((a[i][0]=='O')&&(a[i][1]=='O')&&(a[i][2]=='O')&&(a[i][3]=='O'))
				{ stat=1; break; }
			if((a[0][i]=='O')&&(a[1][i]=='O')&&(a[2][i]=='O')&&(a[3][i]=='O'))
				{ stat=1; break; }
		}
		c1=c2=0;
		for(int i=0;i<4;i++) {
			if(a[i][i]=='O')
				c1++;
			if(a[i][4-i-1]=='O')
				c2++;
		}
		if((c1==4)||(c2==4))
			stat=1;
		
		
		if(stat==3) {
			for(int i=0; i<4; i++)
				for(int j=0; j<4; j++)
					if(a[i][j]=='.') {
						stat=2;
						break;
					}
		}
				
		fprintf(fp,"Case #%d: ", t);
		switch(stat) {
			case 0:
				fprintf(fp,"X won\n");
				break;
			case 1:
				fprintf(fp,"O won\n");
				break;
			case 3:
				fprintf(fp,"Draw\n");
				break;
			case 2:
				fprintf(fp,"Game has not completed\n");
				break;
		}
	}
	return 0;
}
