#include<cstdio>
#include<iostream>
using namespace std;

#define fin(a) fscanf(input,"%d",&a)
#define ffl(a) fscanf(input,"%lf",&a)

int main()
{
	FILE *input,*output;
	input=fopen("B-large.in","r");
	output=fopen("output.txt","w");
	int z,t;
	fin(t);
	for (z=0;z<t;z++)
	{
		int i;
		double c,f,x;
		ffl(c);
		ffl(f);
		ffl(x);
		double time[250001];
		time[0]=x/2;
		//printf("0 : %lf\n",time[0]);
		double min=time[0];
		for (i=1;;i++)
		{
			time[i]=time[i-1]-(x/(2+((i-1)*f)))+(c/(2+((i-1)*f)))+(x/(2+(i*f)));
			//printf("%d : %lf\n",i,time[i]);
			//if (time[i]<min)
//			{
//				min=time[i];
//			}
			if (time[i]>time[i-1])
				break;
		}
		fprintf(output,"Case #%d: %0.7lf\n",z+1,time[i-1]);
	}
	return 0;
}
