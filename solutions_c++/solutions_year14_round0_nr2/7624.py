//Google code jam qestion B
#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{
	int T;
	double C, F, X;
	FILE *p1,*p2;
	p1=fopen("B-small-attempt0.txt","r+");
	p2=fopen("B-small-attemptout.txt","w+");
	fscanf(p1,"%d",&T);
	for(int z=1;z<=T;z++)
	{
		fscanf(p1,"%lf %lf %lf",&C,&F,&X);
		double t1=0,t2=0;
		t1=X/2;
		t2=C/2+X/(2+F);
		int i=0;
		while(t1>t2)
		{
			i++;
			t1=t2;
			t2-=X/(2+(i*F));
			t2+=C/(2+(i*F))+X/(2+((i+1)*F));
		}
		fprintf(p2,"Case #%d: %lf\n",z,t1);
	}
	return 0;
} 
