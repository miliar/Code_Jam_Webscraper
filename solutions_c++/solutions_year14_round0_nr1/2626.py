#include<iostream>
#include<cmath>
#include<cstdio>
#include<algorithm>
#include<cstring>
#include<cstdlib>
using namespace std;

typedef unsigned long long ull;

#define mod 1000000007
#define findmax(a,b) (a)>(b)?a:b
#define findmin(a,b) (a)<(b)?a:b
#define sz 4
int main()
{
	int t;
	
	FILE *in,*out;
	in=fopen("A-small-attempt0.in","r");
	out=fopen("A-small-attempt0.out","w");
	fscanf(in,"%d",&t);
	for(int z=1;z<=t;z++)
	{
		int r1,match=0,data,i,j,x;
		int a[17]={0};
		
		fscanf(in,"%d",&r1);
		
		for(i=1;i<=sz;i++)
		for(j=1;j<=sz;j++)
		{
			fscanf(in,"%d",&x);
			if(i==r1)
			a[x]++;
		}
		
		fscanf(in,"%d",&r1);
		
		for(i=1;i<=sz;i++)
		for(j=1;j<=sz;j++)
		{
			fscanf(in,"%d",&x);
			if(i==r1&&a[x])
			{match++;data=x;}
			
		}
		if(match==1)
		fprintf(out,"Case #%d: %d\n",z,data);
		else if(match>1)
		fprintf(out,"Case #%d: Bad magician!\n",z);
		else
		fprintf(out,"Case #%d: Volunteer cheated!\n",z);
			
	}//end of while
	
	return 0;
}