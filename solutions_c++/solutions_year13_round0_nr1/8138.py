#include<stdio.h>
#include<string.h>
char a[10][10];
int checkx()
{
	int i,j,flag=0;
	for(i=0;i<4;i++)	
	{
		if((a[i][0]=='X'||a[i][0]=='T')&&(a[i][1]=='X'||a[i][0]=='T')&&(a[i][2]=='X'||a[i][2]=='T')&&(a[i][3]=='X'||a[i][3]=='T'))
			flag=1;
		if((a[0][i]=='X'||a[0][i]=='T')&&(a[1][i]=='X'||a[1][i]=='T')&&(a[2][i]=='X'||a[2][i]=='T')&&(a[3][i]=='X'||a[3][i]=='T'))
			flag=1;
}
		if((a[0][0]=='X'||a[0][0]=='T')&&(a[1][1]=='X'||a[1][1]=='T')&&(a[2][2]=='X'||a[2][2]=='T')&&(a[3][3]=='X'||a[3][3]=='T'))
			flag=1;
		if((a[0][3]=='X'||a[0][3]=='T')&&(a[1][2]=='X'||a[1][2]=='T')&&(a[2][1]=='X'||a[2][1]=='T')&&(a[3][0]=='X'||a[3][0]=='T'))
			flag=1;
		return flag;
}
int checky()
{
	int i,j,flag=0;
	for(i=0;i<4;i++)	
	{
		if((a[i][0]=='O'||a[i][0]=='T')&&(a[i][1]=='O'||a[i][0]=='T')&&(a[i][2]=='O'||a[i][2]=='T')&&(a[i][3]=='O'||a[i][3]=='T'))
			flag=1;
		if((a[0][i]=='O'||a[0][i]=='T')&&(a[1][i]=='O'||a[1][i]=='T')&&(a[2][i]=='O'||a[2][i]=='T')&&(a[3][i]=='O'||a[3][i]=='T'))
			flag=1;
}
		if((a[0][0]=='O'||a[0][0]=='T')&&(a[1][1]=='O'||a[1][1]=='T')&&(a[2][2]=='O'||a[2][2]=='T')&&(a[3][3]=='O'||a[3][3]=='T'))
			flag=1;
		if((a[0][3]=='O'||a[0][3]=='T')&&(a[1][2]=='O'||a[1][2]=='T')&&(a[2][1]=='O'||a[2][1]=='T')&&(a[3][0]=='O'||a[3][0]=='T'))
			flag=1;
		return flag;
}
int checkgam()
{
int i,j;
for(i=0;i<4;i++)
for(j=0;j<4;j++)
if(a[i][j]=='.')
return 1;
return 0;
}
int main()
{
freopen("in.txt","r",stdin);
int t,i,k,cas;
scanf("%d",&t);
for(cas=1;cas<=t;cas++)
{
	for(i=0;i<4;i++)
		scanf("%s",a[i]);
		if(checkx())printf("Case #%d: X won\n",cas);
		else if(checky())printf("Case #%d: O won\n",cas);
		else if(checkgam())printf("Case #%d: Game has not completed\n",cas);
		else printf("Case #%d: Draw\n",cas);	

}
return 0;
}

