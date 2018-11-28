#include<bits/stdc++.h>
using namespace std;
int main()
{
	int t,n;
	FILE *fpr=fopen("input.txt","r");
	FILE *fpw=fopen("output.txt","w");
	fscanf(fpr,"%d",&t);
	for(int igh=1;t-->0;igh++)
	{
		fscanf(fpr,"%d",&n);
		long long int a[n];
		for(int i=0;i<n;i++)
		fscanf(fpr,"%lld",&a[i]);
		long long int rate=0;
		long long int choice1=0,choice2=0;
		for(int i=0;i<n-1;i++)
		{
			if(a[i]>a[i+1])
			{
				if(rate<(a[i]-a[i+1]))
				rate=a[i]-a[i+1];
			}
		}
		for(int i=0;i<n-1;i++)
		{
			if(a[i]>a[i+1])
			choice1+=(a[i]-a[i+1]);
			
			choice2+=min(rate,a[i]);
		}
		fprintf(fpw,"Case #%d: %lld %lld\n",igh,choice1,choice2);
	}
	return 0;
}
