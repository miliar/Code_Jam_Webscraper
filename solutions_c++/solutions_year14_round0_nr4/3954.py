#include<stdio.h>
#include<stdlib.h>
#include<algorithm>
using namespace std;
main()
{
	int t,x,i,n,j,war,dwar;
	float a1[1000],a2[1000],temp;
	FILE *in = fopen("D-large.in","r");
	FILE *out = fopen("out.txt","w");
	fscanf(in,"%d",&t);
	x=t;
	while(t--)
	{
		fscanf(in,"%d",&n);
		for(i=0;i<n;i++)
		fscanf(in,"%f",&a1[i]);
		for(i=0;i<n;i++)
		fscanf(in,"%f",&a2[i]);
		sort(a1,a1+n);
		sort(a2,a2+n);
		if(n==1)
		{
			 if(a1[0]>a2[0])
			 {
			 	war=1;
			 	dwar=1;
			 }
			 else
			 {
			 	war=0;
			 	dwar=0;
			 }
		}
		else
		{
			i=0;
			j=0;
			while(1)
			{
				if(a1[i]<a2[j])
				{
					i++;
					j++;
				}
				else
				j++;
				if(i==n || j==n)
				break;
			}
			war=n-i;
			i=0;
			j=0;
			while(1)
			{
				if(a1[i]>a2[j])
				{
					i++;
					j++;
				}
				else
				i++;
				if(i==n)
				break;
			}
			dwar=j;
			
		}
		fprintf(out,"Case #%d: %d %d\n",x-t,dwar,war);
	}
}
