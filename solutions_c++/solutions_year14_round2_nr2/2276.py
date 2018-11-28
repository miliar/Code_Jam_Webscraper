#include <iostream>
#include<stdio.h>
using namespace std;

int main() {
	// your code goes here
	int a,b,k,count,i,j,c=1;
	int t;
	FILE *fp1,*fp2;
	fp1=fopen("akhi1.in","r");
	fp2=fopen("out.txt","w");
	fscanf(fp1,"%d",&t);
//	printf("%d",(7&11));
	while(t--)
	{
		fscanf(fp1,"%d%d%d",&a,&b,&k);
	//	int x[1002][1002]={0};
		count=0;
		for(i=0;i<a;i++)
		{
			for(j=0;j<b;j++)
			{
			if((i&j)<k)
			{
			count++;
			//printf("%d %d\n",i,j);
			}
			}
		}
	
		fprintf(fp2,"Case #%d: %d\n",c,count);
		c++;
	}
	return 0;
}
