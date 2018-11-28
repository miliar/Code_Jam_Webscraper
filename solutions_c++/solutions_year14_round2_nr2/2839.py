#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
	int t,h=1;
	FILE *f1,*f2;
    f1=fopen("B-small-attempt0.in","r");
    f2=fopen("output.txt","w");
    fscanf(f1,"%d\n",&t);
	while(t--)
	{
		long a,b,k,i,j,n;
		long long ans=0;
		fscanf(f1,"%ld%ld%ld",&a,&b,&k);
		for(i=0;i<a;i++)
			for(j=0;j<b;j++)
			{
				if((i&j) < k)
					ans++;
			}
		fprintf(f2,"Case #%d: %lld\n",h,ans);
		h++;
	}
}