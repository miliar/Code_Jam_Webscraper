// Problema_code_jam.cpp : Defines the entry point for the console application.
//
#include "stdafx.h"
#include <time.h>
#include <limits.h>
//ULLONG_MAX
#include <cstdlib>
#include <iostream>
#include <stdio.h>
#include <math.h>
#include <windows.h>
#include <fstream>
#include "math.h"
#include <vector>
#include <string>
#include <iomanip>
using namespace std;
typedef unsigned long long int ll;
typedef signed long long int sll;
double PI = 3.141592653589793;
//Problema
ifstream in("C:\\Users\\Casa\\Desktop\\GOOGLE CODE JAM\\C-sample-practice.in", ios_base::in);
ofstream out("C:\\Users\\Casa\\Desktop\\GOOGLE CODE JAM\\C-small.in", ios_base::out);

void pre_process()
{
	return;
}
void case_solve()
{
	int N = 16;
	int J = 50;
	int impressos = 0;
	int a, b, c, d;
	int i;
	for (a = 1; a <= 14; a++)
	{
		if (a % 2 != 0) continue;
		for (b = 1; b <= 14; b++)
		{
			if (b == a) continue;
			if (b < a) continue;
			if (b % 2 != 0) continue;
			for (c = 1; c <= 14; c++)
			{
				if (c % 2 == 0) continue;
				for (d = 1; d <= 14; d++)
				{
					if (d == c) continue;
					if (c < d) continue;
					if (d % 2 == 0) continue;
					//Processar
					//out << impressos + 1 << " ";
					for (i = 0; i <= N-1; i++)
					{
						if (i == 0 || i == N-1 || i == a || i == b || i == c || i == d)	out << "1";
						else														    out << "0";
					}
					out << " 3 2 5 2 7 2 9 2 11" << endl;
					impressos++;
					if (impressos == J) return;
				}
			}
		}
	}

	



	//in >> L >> X;
	//getline(in, linha);
	//out << fixed << setprecision(6);   escreve  0.123456
	//cout << setfill('0') << setw(5) << 25;    output: 00025
	//out << "YES";


}
int _tmain(int argc, _TCHAR* argv[])
{

	ll i, cases;
	pre_process();
	in >> cases;
	cases = 1;
	for (i = 1; i <= cases; i++)
	{
		if (i == 2)
		{
			i = i;
		}
		out << "Case #" << i << ": ";
		out << endl;
		case_solve();
		cout << "Caso " << i << " de " << cases << " --> OK\n";
		//out << "\n";
	}
}