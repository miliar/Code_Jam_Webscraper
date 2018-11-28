#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{
	int t,i,j,a1,a2,flag,c,ans;
	int arr1[4][4];
	int arr2[4][4];
	FILE *inf=fopen("A-small-attempt0.in","r");
	FILE *opf=fopen("output1.in","w+");
	fscanf(inf,"%d",&t);
	for(c=0;c<t;c++)
	{
		flag=0;
		fscanf(inf,"%d",&a1);
		for(i=0;i<4;i++)
		for(j=0;j<4;j++)
		fscanf(inf,"%d",&arr1[i][j]);
		fscanf(inf,"%d",&a2);
		for(i=0;i<4;i++)
		for(j=0;j<4;j++)
		fscanf(inf,"%d",&arr2[i][j]);
		
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			if(arr1[a1-1][i]==arr2[a2-1][j])
			{
				flag++;
				ans=arr1[a1-1][i];
			}
		}
		if(flag==1)
		fprintf(opf,"Case #%d: %d\n",c+1,ans);
		else if(flag>1)
		fprintf(opf,"Case #%d: Bad magician!\n",c+1);
		else if(flag<1)
		fprintf(opf,"Case #%d: Volunteer cheated!\n",c+1);
	}
	return 0;
}
