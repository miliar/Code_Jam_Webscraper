//Google code jam question 1 
#include<iostream>
#include<stdio.h>
using namespace std;
int cmp(int a1[4], int a2[4],int* n);
int a;
int main()
{	
	int T,r,ar1[4],ar2[4];
	FILE *p1,*p2;
	p1=fopen("A-small-attempt1.txt","r+");
	p2=fopen("A-small-attemptout.txt","w+");
	fscanf(p1,"%d",&T);
	for(int k=1;k<=T;k++)
	{
		fscanf(p1,"%d",&r);
		for(int i=0;i<4;i++)
		{
			if(i>=r)
				for(int j=0;j<4;j++)
					fscanf(p1,"%d",&a);
			else
				for(int j=0;j<4;j++)
					fscanf(p1,"%d",&ar1[j]);
		}
		fscanf(p1,"%d",&r);
		for(int i=0;i<4;i++)
		{
			if(i>=r)
				for(int j=0;j<4;j++)
					fscanf(p1,"%d",&a);
			else
				for(int j=0;j<4;j++)
					fscanf(p1,"%d",&ar2[j]);
		}
		int num=0;
		int ans=cmp(ar1,ar2,&num);
		if(ans==0)
			fprintf(p2,"Case #%d: Volunteer cheated!\n",k);
		else if(ans>=2)
			fprintf(p2,"Case #%d: Bad magician!\n",k);
		else
			fprintf(p2,"Case #%d: %d\n",k,num);
	}
	return 0;
}
int cmp(int a1[4], int a2[4],int* n)
{
	int ans=0;
	for(int i=0;i<4;i++)
		for(int j=0;j<4;j++)
			if(a1[i]==a2[j])
			{	
				ans++;
				*n=a1[i];
			}
	return ans;
}
	
