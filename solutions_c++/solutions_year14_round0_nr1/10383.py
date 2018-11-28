#include<string.h>
#include<conio.h>
#include<stdio.h>
void main()
{
clrscr();
FILE *fp,*fo;
int flag=0;
int j,m;
int x,c1,i,c2;
int x1,x2,x3,x4;
int z1,z2,z3,z4;
int a1,a2,a3,a4;
fp=fopen("input.in","r");
fo=fopen("output.txt","w");
if(fp==NULL)
{
}else
{
   fscanf(fp,"%d",&x);
   for(j=0;j<x;j++)
   {

	fscanf(fp,"%d",&c1);

	for(i=0;i<c1;i++)
	{
		fscanf(fp,"%d %d %d %d",&x1,&x2,&x3,&x4);
	}
	for(i=c1;i<4;i++)
	{
		fscanf(fp,"%d %d %d %d",&z1,&z2,&z3,&z4);
	}
		fscanf(fp,"%d",&c2);

	for(i=0;i<c2;i++)
	{
		fscanf(fp,"%d %d %d %d",&z1,&z2,&z3,&z4);
	}
	for(i=c2;i<4;i++)
	{
		fscanf(fp,"%d %d %d %d",&a1,&a2,&a3,&a4);
	}

	printf("%d \n%d \n%d %d %d %d\n",x,c1,x1,x2,x3,x4);

	printf("%d\n",c2);

	printf("%d %d %d %d\n",z1,z2,z3,z4);

	//Checking logic
	flag=0;
	m=-1;
	if(x1==z1||x1==z2||x1==z3||x1==z4)
	{
	flag++;
	m=x1;
	}
	if(x2==z1||x2==z2||x2==z3||x2==z4)
	{
	flag++;
	m=x2;
	}
	if(x3==z1||x3==z2||x3==z3||x3==z4)
	{
	flag++;
	m=x3;
	}
	if(x4==z1||x4==z2||x4==z3||x4==z4)
	{
	flag++;
	m=x4;
	}

	if(flag==0)
	{
		fprintf(fo,"Case #%d: Volunteer cheated!\n",j+1);
	}
	if(flag==1)
	{
		fprintf(fo,"Case #%d: %d\n",j+1,m);
	}
	if(flag>1)
	{
		fprintf(fo,"Case #%d: Bad magician!\n",j+1);
	}



  }

}
getch();
}