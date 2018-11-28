//#include<iostream.h>
#include<conio.h>
#include<stdio.h>
#include<stdlib.h>
int main()
{
	//clrscr();
	int number=0;
	int n,p,flag=0,z,s;
	int a[4][4],b[4][4];
	char ch[50];
    FILE *fp,*fp2;
    fp=fopen("input.in","r");
	fp2=fopen("output.txt","w");
    fscanf(fp,"%d",&s);

while(number<s)
{

    fscanf(fp,"%d",&n);
	for(int i=0;i<4;i++)
	{
		for(int j=0;j<4;j++)
		{
			fscanf(fp,"%d",&a[i][j]);
		}
	}
	fscanf(fp,"%d",&p);
	for(int i=0;i<4;i++)
	{
		for(int j=0;j<4;j++)
		{
			fscanf(fp,"%d",&b[i][j]);
		}


	}


    flag=0;
	for(int j=0;j<4;j++)
	{
		for(int k=0;k<4;k++)
		{

			if(a[n-1][j]==b[p-1][k])
			{
				z=j;
				flag++;
			}
		}
	}
	if(flag>=2)
  fprintf(fp2,"Case #%d: Bad magician!\n",number+1);
	else if(flag==1)
	fprintf(fp2,"Case #%d: %d\n",number+1,a[n-1][z]);
	else
    fprintf(fp2,"Case #%d: Volunteer cheated!\n",number+1);



number++;

}

	getch();
	return 0;
}
