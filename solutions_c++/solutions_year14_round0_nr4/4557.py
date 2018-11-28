#include <stdio.h>
#include <algorithm>
using namespace std;

FILE *in=fopen("input.txt","r");
FILE *out=fopen("output.txt","w");

int n,m;
double a[1050];
double b[1050];

int main()
{
	fscanf(in,"%d",&n);

	for(int i=0;i<n;i++)
	{
		fscanf(in,"%d",&m);

		for(int j=0;j<m;j++)
			fscanf(in,"%lf",&a[j]);
		for(int j=0;j<m;j++)
			fscanf(in,"%lf",&b[j]);

		sort(a,a+m);
		sort(b,b+m);

		int q1,q2;
		int dab1=0;
		int dab2=0;

		q1=q2=m-1;

		while(1)
		{
			if(q1<0 || q2<0)	break;
			if(a[q1]>b[q2])
			{
				dab1++;
				q1--;
				q2--;
			}
			else
				q2--;
		}

		q1=q2=m-1;

		while(1)
		{
			if(q1<0 || q2<0)	break;
			if(a[q1]<b[q2])
			{
				dab2++;
				q1--;
				q2--;
			}
			else
				q1--;
		}

		fprintf(out,"Case #%d: %d %d\n",i+1,dab1,m-dab2);
	}


	return 0;
}
