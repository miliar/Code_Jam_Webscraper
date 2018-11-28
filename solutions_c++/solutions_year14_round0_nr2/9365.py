// app.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "math.h"
#include <Windows.h>  //#include <stdio.h>


double time_to_buy(int total_farms, double rate, double C, double F, double X)
{
	double total_time = 0.0;
	for (int farms = 0; (farms < total_farms); farms++)
	{
		total_time += (C / rate);
		rate += F;
	}
	return (total_time + (X / rate));
}

void find_em(double rate, double C, double F, double X)
{
	double previous_time = time_to_buy(0, rate, C, F, X);
	for (int total_farms = 1; (true); total_farms++)
	{
		double new_time = time_to_buy(total_farms, rate, C, F, X);
		if (previous_time < new_time) break;
		previous_time = new_time;
	}

	_tprintf(TEXT("%.7f"), previous_time);
}

int _tmain(int argc, _TCHAR* argv[])
{
	int T_test_cases = 0;

	FILE *fp = stdin;
	if (argc > 1) fp = _tfopen(argv[1], TEXT("r"));
	if (NULL == fp) return 1;

	double rate = 2.0;

	//float C, F, X;  //double C, F, X;
	TCHAR CC[512], FF[512], XX[512];

	_ftscanf(fp, TEXT("%d"), &T_test_cases);
	for (int i = 1; i <= T_test_cases; i++)
	{
		_tprintf(TEXT("Case #%d: "), i);
		
		/*
		_ftscanf(fp, TEXT("%f %f %f"), &C, &F, &X);

		//double CC = floor (C * 100000) / 100000;
		//double FF = floor (F * 100000) / 100000;
		//double XX = floor (X * 100000) / 100000;

		find_em(rate, C, F, X);
		*/
		
		_tcsnset(CC, '\0', 512);  _tcsnset(FF, '\0', 512);  _tcsnset(XX, '\0', 512);
		_ftscanf(fp, TEXT("%s %s %s"), &CC, &FF, &XX);		
		find_em(rate, _ttof(CC), _ttof(FF), _ttof(XX));

		
		_tprintf(TEXT("\n"));
	}

	if (stdin == fp) fclose(fp);
	return 0;
}