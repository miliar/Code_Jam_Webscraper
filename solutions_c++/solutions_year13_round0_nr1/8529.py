#include<stdio.h>
int main(void){
char Tab[4][4],car;
int i,j,k,n,O,OO,O2,O3,X,XX,X2,X3,B;
freopen("A-small-attempt1.in","r",stdin);
freopen("A-small-attempt1.out","w",stdout);
scanf("%d\n",&n);
for(k=1;k<=n;k++){
	////////LEE
	for(i=0;i<4;i++)
		scanf("%s",Tab[i]);
		
	////////BUSCA
	B=16;
	O2=0;X2=0;O3=0;X3=0;
	for(i=0;i<4;i++){
		for(j=0,O=0,X=0,OO=0,XX=0;j<4;j++){
			if(Tab[i][j]=='X')X++;
			else if(Tab[i][j]=='O')O++;
			else if(Tab[i][j]=='T'){X++;O++;}
			else B-=1;
			if(Tab[j][i]=='X')XX++;
			else if(Tab[j][i]=='O')OO++;
			else if(Tab[j][i]=='T'){XX++;OO++;}
			else B-=1;
			
			if((X==4)||(XX==4)){printf("Case #%d: X won",k);break;}
			if((O==4)||(OO==4)){printf("Case #%d: O won",k);break;}
		}
		
		if(Tab[i][i]=='X')X2++;
		else if(Tab[i][i]=='O')O2++;
		else if(Tab[i][i]=='T'){X2++;O2++;}
		
		if(Tab[i][3-i]=='X')X3++;
		else if(Tab[i][3-i]=='O')O3++;
		else if(Tab[i][3-i]=='T'){X3++;O3++;}
		
		
		if((X2==4)||(X3==4)){printf("Case #%d: X won",k);break;}
		if((O2==4)||(O3==4)){printf("Case #%d: O won",k);break;}
		
		if(j<4)break;
	}
	if(j==4&&i==4){
		if(B==16)printf("Case #%d: Draw",k);
		else printf("Case #%d: Game has not completed",k);
	}
	if(k<n)printf("\n");
}
return 0;
}
