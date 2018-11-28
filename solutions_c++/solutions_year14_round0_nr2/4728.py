#include <stdio.h>
#include <limits.h>

FILE *in=fopen("input.txt","r");
FILE *out=fopen("output.txt","w");

int n;
double c,f,x;
double dab;

int main()
{
	fscanf(in,"%d",&n);

	for(int i=0;i<n;i++)
	{
		fscanf(in,"%lf %lf %lf",&c,&f,&x);

		dab=INT_MAX;

		int tcnt;
		int cnt=0;
		int boost;
		double sec=0;

		while(1)
		{
			boost=0;
			tcnt=cnt;
			while(1)
			{
				if(tcnt==0)
				{
					sec+=x/(2+(f*boost));
					break;
				}
				sec+=c/(2+(f*boost));
				tcnt--;
				boost++;
			}

			cnt++;
			if(sec>dab)
				break;
			dab=sec;
			sec=0;
		}

		fprintf(out,"Case #%d: %.7lf\n",i+1,dab);
	}

	return 0;
}