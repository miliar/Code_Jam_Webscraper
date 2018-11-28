#include<iostream>
#include<cstring>
using namespace std;
int row_check(char a[][5],char ch)
{
	int i=0,j=0,flaag=0;
	for(i=0;i<=3;i++)
	{
		flaag=0;
		for(j=0;j<=3;j++)
			if(a[i][j]!=ch && a[i][j]!='T')
			{
				flaag=1;
				break;
				
			}	
		if(flaag==0)	
			break;
	}
	return !flaag;
}
int column_check(char a[][5],char ch)
{
	int i=0,j=0,flaag;
	for(i=0;i<4;i++)
	{
		flaag=0;
		for(j=0;j<4;j++)
		{
			if(a[j][i]!=ch && a[j][i]!='T')
			{
				flaag=1;
				break;
				
			}	
		}
		if(flaag==0)	
			break;
		
		}
	return !flaag;	
}
int diagonal_check(char a[][5],char ch)
{
	int i=0,j=0,flaag=0;
	for(;i<4;i++)
		if(a[i][i]!=ch && a[i][i]!='T')
		{
			flaag=1;
			break;
			}	
	if(flaag==0)		
		return !flaag;
	int count=0;	
	for(i=0;i<4;i++)	
		for(j=0;j<4;j++)
		{
			if(j+i ==3)
				//printf("a %c\n",a[i][j]);
			if(j!=i && (j+i)==3 && (a[i][j]==ch )||(a[i][j]=='T'))
			count++;
		}
	//printf("diagonal %d\n",count);
	return (count==4);
}
main()

{
	int t,count=1;
	
	scanf("%d",&t);
	while(t--)
	{
	
	char a[5][5]={{'x','o','o','o','\0'},{'o','o','o','x','\0'},{'x','o','x','x','\0'},{'o','o','o','x','\0'}};
	/*printf("%d",row_check(a,'x'));
	printf("%d",column_check(a,'o'));
	printf("%d",diagonal_check(a,'o'));*/
	int i=0,j=0;
	for(;i<4;i++)
		scanf("%s",a[i]);
	printf("Case #%d: ",count++);
	int flag1=row_check(a,'X');
	int flag2=row_check(a,'O');
	int flag3=column_check(a,'X');
	int flag4=column_check(a,'O');
	int flag5=diagonal_check(a,'X');
	int flag6=diagonal_check(a,'O');
	if(flag1==1||flag3||flag5)
		printf("X won\n");
	else if(flag2==1||flag4||flag6)	
		printf("O won\n");
	else
	{	
	
	int flaag=0;
	for(i=0;i<4;i++)	
		for(j=0;j<4;j++)
		if(a[i][j]=='.')
		{
			flaag=1;
			break;
			}
	if(flaag!=1)		
		printf("Draw\n");
	else
		printf("Game has not completed\n");
	}
}}
