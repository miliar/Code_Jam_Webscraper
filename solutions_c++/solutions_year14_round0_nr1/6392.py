#include<stdio.h>
#include<iostream>

using namespace std;

int main(int argc,char *argv[])
{
FILE *fp,*fp2;
fp=fopen(argv[1],"r+");
fp2=fopen(argv[argc-1],"w+");
int test=0,row1=0,row2=0,arr1[5][5]={0},arr2[5][5]={0},flag,temp[17],res,num;
fscanf(fp,"%d",&test);
num=test;
while(test--)
{
	flag=res=0;
	fscanf(fp,"%d",&row1);
	for(int i=0;i<4;i++)
	{
		for(int j=0;j<4;j++)
		{
			fscanf(fp,"%d",&arr1[i][j]);
		}
	}
	fscanf(fp,"%d",&row2);
	for(int i=0;i<4;i++)
	{
		for(int j=0;j<4;j++)
		{
			fscanf(fp,"%d",&arr2[i][j]);
		}
	}
	for(int i=0;i<=16;i++)
		temp[i]=0;
	for(int i=0;i<4;i++){
		temp[arr1[row1-1][i]]=1;
	}
	for(int i=0;i<4;i++)
	{
		if(temp[arr2[row2-1][i]]==1 && flag==0)
		{
			flag=1;
			res=arr2[row2-1][i];
		}
		else if(temp[arr2[row2-1][i]]==1 && flag==1)
		{
			flag=2;
			break;
		}
	}
	if(flag==0)
		fprintf(fp2,"Case #%d: Volunteer cheated!\n",num-test);
	if(flag==1)
		fprintf(fp2,"Case #%d: %d\n",num-test,res);
	if(flag==2)
		fprintf(fp2,"Case #%d: Bad magician!\n",num-test);
}
fclose(fp);
return 0;
}

