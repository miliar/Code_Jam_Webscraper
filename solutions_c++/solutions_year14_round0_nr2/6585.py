#include "iostream"
#include "cstdio"

using namespace std;

double c,f,x;
double speed;
int test()
{
	if(c/speed+x/(speed+f)<x/speed)
		return 1;
	else
		return 0;
}

int main()
{
	int t;
	
	double time;
	int k;
	FILE *fpin=fopen("B-large.in","r");
	FILE *fpout=fopen("out.txt","w");
	fscanf(fpin,"%d",&t);
//	scanf("%d",&t);
	for(k=0;k<t;k++)
	{
	//	scanf("%lf %lf %lf",&c,&f,&x);
	//	printf("%lf %lf %lf",c,f,x);
	//	getchar();
		fscanf(fpin,"%lf %lf %lf",&c,&f,&x);
		time=0;
		speed=2;
		while(test())
		{
			time+=c/speed;
			speed+=f;
		}
		time+=x/speed;
		fprintf(fpout,"Case #%d: %.7lf\n",k+1,time);
	}
	
}