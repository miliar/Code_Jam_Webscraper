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
ifstream in("C:\\Users\\Casa\\Desktop\\GOOGLE CODE JAM\\A-large.in", ios_base::in);
ofstream out("C:\\Users\\Casa\\Desktop\\GOOGLE CODE JAM\\A-large_out.in", ios_base::out);

void pre_process()
{
	return;
}
void case_solve()
{
	ll N;
	in >> N;
	if (N == 0)
	{
		out << "INSOMNIA";
		return;
	}
	ll i;
	bool visto[10];
	for (i = 0; i <= 9; i++) visto[i] = 0;
	vector<int> dig;
	ll mult = 1;
	while (true)
	{
		dig.clear();
		int aux;
		ll N2 = N*mult;
		while (true)
		{
			aux = N2 % 10;
			N2 /= 10;
			dig.push_back(aux);
			if (N2 == 0) break;
		}
		for (i = 0; i <= dig.size() - 1; i++) visto[dig[i]] = 1;
		bool fim = 1;
		for (i = 0; i <= 9; i++)
		{
			if (!visto[i]) fim = 0;
		}
		if (fim) break;
		mult++;
	}

	out << N*mult;
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
	for (i = 1; i <= cases; i++)
	{
		if (i == 2)
		{
			i = i;
		}
		out << "Case #" << i << ": ";
		case_solve();
		cout << "Caso " << i << " de " << cases << " --> OK\n";
		out << "\n";
	}
}