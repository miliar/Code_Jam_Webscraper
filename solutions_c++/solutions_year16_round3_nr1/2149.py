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
ofstream out("C:\\Users\\Casa\\Desktop\\GOOGLE CODE JAM\\A-large_sol.in", ios_base::out);

void pre_process()
{
	return;
}
bool valido(int sen[], int N)
{
	int i;
	int soma = 0;
	for (i = 0; i <= N - 1; i++) soma += sen[i];
	int maior = 0;
	for (i = 1; i <= N - 1; i++)
	{
		if (sen[i] > sen[maior]) maior = i;
	}
	if (maior > soma - maior) return 0;
	else return 1;
}
void case_solve()
{

	int N;
	in >> N;

	int i;
	int sen[30];
	for (i = 0; i <= N - 1; i++)
	{
		in >> sen[i];
	}
	int maior, soma;

	while (true)
	{
		//Remove 1
		maior = 0;
		for (i = 1; i <= N - 1; i++)
		{
			if (sen[i] > sen[maior]) maior = i;
		}
		char o = maior + 65;
		out << o ;
		sen[maior]--;
		//ver fim
		soma = 0;
		for (i = 0; i <= N - 1; i++) soma += sen[i];
		if (soma == 0) break;


		//Remove 2
		maior = 0;
		for (i = 1; i <= N - 1; i++)
		{
			if (sen[i] > sen[maior]) maior = i;
		}
		o = maior + 65;
		sen[maior]--;
		//Continua valido?
		if (valido(sen, N))
		{
			out << o;
			//ver fim
			soma = 0;
			for (i = 0; i <= N - 1; i++) soma += sen[i];
			if (soma == 0) break;
		}
		else sen[maior]++;
		out << ' ';
		
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