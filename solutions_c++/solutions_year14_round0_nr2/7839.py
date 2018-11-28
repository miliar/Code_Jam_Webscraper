#include<iostream>
#include<cstdio>
#include<cstdlib>
using namespace std;

FILE* in;
FILE* out;

void  test(int n)
{
	register double C,F,X;
	fscanf(in,"%lf %lf %lf",&C, &F, &X);
	register double rate=2;  // the rate of increment
	register double time=0;   //the current time
	register double time_completion_final=0; //time of completion without final inc.
	register double tmp;
	time_completion_final=X/rate;
	while(1)
	{
		time+=C/rate;
		rate+=F;
		tmp=X/rate;
		if( (tmp+time) >time_completion_final)
		{ break; }
		time_completion_final=time+tmp;
	}
	fprintf(out,"Case #%d: %.7f\n",n,time_completion_final);
}

int main()
{
	char file[100];
	cin>>file;
	in=fopen(file,"r");
	out=fopen("out.txt","w");
	int T;
	fscanf(in,"%d",&T);
	int n;
	for(n=0;n<T;n++)
		test(n+1);
	return 0;
}
