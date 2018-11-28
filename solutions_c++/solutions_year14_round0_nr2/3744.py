// Cookie_Clicker_Alpha.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

int main(int argc, char* argv[])
{
	int n;
	int i;
	FILE *IN1, *OUT1;
	double c,f,x;
	double pro;
	double tem_x,tem_c;
	double t;

	IN1 = fopen ("B-large.in" , "rb");
    OUT1 = fopen ("B-large.out" , "wb");
    fscanf(IN1,"%d",&n);
	for(i=0;i<n;i++)
	{
		fscanf(IN1,"%lf %lf %lf",&c,&f,&x);
		pro = 2;
		t = 0;
		while(1)
		{
			tem_x = (x / pro) - (x / (pro+f));
			tem_c = (c / pro);
			if(tem_x > tem_c)
			{
				t = t + tem_c;
				pro = pro + f;
			}
			else
			{
				t = t + (x / pro);
				break;
			}
		}
		fprintf(OUT1,"Case #%d: %.7f\r\n",i+1,t);
	}
	return 0;
}

