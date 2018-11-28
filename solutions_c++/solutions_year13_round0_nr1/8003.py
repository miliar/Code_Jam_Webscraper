#include<stdio.h>
#include<math.h>
#include<stdlib.h>
#include<iostream.h>
#include<conio.h>
int suma=348,sumb=321,flag=0,count=0;
char arr[4][4];
void main()
{
	int n,i,j,m;
	clrscr();
		FILE *f1=fopen("def.txt","r");
	//int arr[4][4];
	//int ch=getc(f1);
	//m=atoi(ch);
	scanf("%d",&n);
	//fflush(stdin);
	//getc(f1);
	for(m=0;m<n;m++)
	{

		//fflush(stdin);
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				arr[i][j]=getc(f1);
				//printf("%d",arr[i][j]);
				if(arr[i][j]=='X' || arr[i][j]=='O' || arr[i][j]=='T')
				count++;
			}
			char ch=getc(f1);
		}
		char ch=getc(f1);
	for(i=0;i<4;i++)
	{
		for(j=0;j<4;j++);
	  //	printf("%c",arr[i][j]);
	}
	getchar();
	for(i=0;i<4;i++)
	{int sum=arr[i][0]+arr[i][1]+arr[i][2]+arr[i][3];
	if(sum==352)
	{
	//if(arr[i][0]==arr[i][1]==arr[i][2]==arr[i][3])
	//{
		//flag=1;
		flag=1;
		//if(arr[i][0]=='X')
		printf("Case #%d: X won",m+1);
	}
	if(sum==316)
	{	//else
	flag=1;
	printf("Case #%d: O won",m+1);}

	}
	for(i=0;i<4;i++)
	{//if(arr[0][j]==arr[1][j]==arr[2][j]==arr[3][j])
	//{
	int sum=arr[0][i]+arr[1][i]+arr[2][i]+arr[3][i];

	//	flag=1;
	  ///	if(arr[0][j]=='X')
	     //	printf("Case #%d: X won",m+1);
	       //	else
		//printf("Case #%d: O won",m+1);
	if(sum==352)
	{
	//if(arr[i][0]==arr[i][1]==arr[i][2]==arr[i][3])
	//{
		//flag=1;
		flag=1;
		//if(arr[i][0]=='X')
		printf("Case #%d: X won",m+1);
	}
	if(sum==316)
	{	//else
	flag=1;
	printf("Case #%d: O won",m+1);}





	}

	int sum=arr[0][0]+arr[1][1]+arr[2][2]+arr[3][3];
	if(sum==352)
	{

		flag=1;
		printf("Case #%d: X won",m+1);
	}
	if(sum==316)
	{
		flag=1;
		printf("Case #%d: O won",m+1);
	}

	sum=arr[0][3]+arr[1][2]+arr[2][1]+arr[3][0];
	if(sum==352)
	{

		flag=1;
		printf("Case #%d: X won",m+1);
	}
	if(sum==316)
	{
		flag=1;
		printf("Case #%d: O won",m+1);
	}

	for(i=0;i<4;i++)
	{
	int sum=arr[i][0]+arr[i][1]+arr[i][2]+arr[i][3];
	if(sum==suma)
	{
		//if(arr[i][0]=='X')
		flag=1;
		printf("Case #%d: X won",m+1);
	}
	//else

	if(sum==sumb)
	{flag=1;
	printf("Case #%d: O won",m+1);
	}
	}
	for(i=0;i<4;i++)
	{
	int sum=arr[0][i]+arr[1][i]+arr[2][i]+arr[3][i];
	if(sum==suma)
	{
		if(arr[0][j]=='X')
		{flag=1;
		printf("Case #%d: X won",m+1);
		//else
		}
	}
	if(sum==sumb)
	{flag=1;
	printf("Case #%d: O won",m+1);
	}
	}
	sum=arr[0][0]+arr[1][1]+arr[2][2]+arr[3][3];
	if(sum==348)
	{
		flag=1;
		printf("Case #%d: X won",m+1);
	}
	if(sum==321)
	{
	flag=1;
		printf("Case #%d: O won",m+1);
	}
	sum=arr[0][3]+arr[1][2]+arr[2][1]+arr[3][0];
	if(sum==348)
	{
		flag=1;
		printf("Case #%d: X won",m+1);
	}
	if(sum==321)
	{
	flag=1;
		printf("Case #%d: O won",m+1);
	}
	if(flag!=1)
	{
		if(count<16)
		{
			printf("Case #%d: Game has not completed",m+1);
		}
		else
		printf("Case #%d: Draw",m+1);
	}
	count=0;
	flag=0;
	printf("\n");
	}
	getch();
}