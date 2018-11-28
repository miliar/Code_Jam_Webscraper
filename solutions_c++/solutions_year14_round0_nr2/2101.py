// codejamQualB.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

inline double TimeToGetX(double income, double X)
{
	return X/income;
}

int _tmain(int argc, _TCHAR* argv[])
{
	FILE* in = fopen("inputB.in","r");
	FILE* out = fopen("outputB.out","w");
	int caseCount = 0;
	double C=0, F=0, X=0, time=0, income;
	fscanf(in,"%d",&caseCount);
	for(int i=0;i<caseCount;i++)
	{
		time = 0.0; income = 2.0;
		fscanf(in,"%lf %lf %lf",&C,&F,&X);
		while(true)
		{
			if((TimeToGetX(income,X)) <= (TimeToGetX(income,C) + TimeToGetX(income + F, X)))
			{
				time += TimeToGetX(income,X);
				break;
			}
			time+=TimeToGetX(income,C); income+=F;
		}
		fprintf(out,"Case #%d: %lf\n",i+1, time);
	}
	fclose(in); fclose(out);
	return 0;
}

