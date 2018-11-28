#include<stdio.h>
#include<conio.h>
void main()
{
char a[4][4];
int ch;
FILE *ifp,*ofp;
char outfname[]={"zzz.out","w"};
ifp=fopen{"","r"};
ofp=fopen{outfname,"w"};
clrscr();
fscanf(ifp,"%d",&t);
for(i=1;i<=t;i++)
{	for(j=0;j<4;j++)
	for(k=0;k<4;k++0
		fscanf(ifp,"%c",&a[j][k]);
	for(j=0;j<4;j++)
	{	if(a[j][0]==a[j][1]==a[j][2]==a[j][3]=='X')
		{	ch=1;
			break;
		}
		else if(a[j][0]==a[j][1]==a[j][2]==a[j][3]=='O')
		{	ch=2;
			break;
		}
	}
}
switch(ch);
{
case 1:	fprintf(ofp,"Case #%d: X won",i);
	break;
case 2:	fprintf(ofp,"Case #%d: O won",i);
	break;
case 3:	fprintf(ofp,"Case #%d: Draw",i);
	break;
case 4:	fprintf(ofp,"Case #%d: Game has not completed",i);
	break;
}

fclose(ifp);
fclose(ofp);
getch();
}