#include<stdio.h>
#include<algorithm>
using namespace std;

int main(){
	FILE *f=fopen("A-large.in","r");
	FILE *fo=fopen("output.txt","w+");

	int t,sum1,sum2,ma;
	int n,m[1010];
	fscanf(f,"%d",&t);
	for(int k=1;k<=t;k++)
	{
		sum1=sum2=0;
		fscanf(f,"%d",&n);
		for(int i=1;i<=n;i++)
		{
			fscanf(f,"%d",&m[i]);
		}

		for(int i=1;i<n;i++)
		{
			if(m[i]-m[i+1]>0)
			{
				sum1+=(m[i]-m[i+1]);
			}
		}
		ma=0;
		for(int i=1;i<n;i++)
		{
			if(m[i]-m[i+1]>0)
			{
				ma=max(m[i]-m[i+1],ma);
			}
		}
		for(int i=1;i<n;i++)
		{
			sum2+=min(ma,m[i]);
		}

		fprintf(fo,"Case #%d: %d %d\n",k,sum1,sum2);
	}
}