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
void case_solve()
{
	string s;
	getline(in, s);
	int i;
	int c[10];
	for (i = 0; i <= 9; i++) c[i] = 0;
	for (i = 0; i <= s.size() - 1; i++) if (s[i] == 'Z') c[0]++;
	for (i = 0; i <= s.size() - 1; i++) if (s[i] == 'W') c[2]++;
	for (i = 0; i <= s.size() - 1; i++) if (s[i] == 'U') c[4]++;
	for (i = 0; i <= s.size() - 1; i++) if (s[i] == 'X') c[6]++;
	for (i = 0; i <= s.size() - 1; i++) if (s[i] == 'G') c[8]++;
	int aux = 0;
	for (i = 0; i <= s.size() - 1; i++) if (s[i] == 'O') aux++;
	c[1] = aux - c[0] - c[2]-c[4];
	if (c[1] < 0) c[1] = 0;
	
	aux = 0;
	for (i = 0; i <= s.size() - 1; i++) if (s[i] == 'H') aux++;
	c[3] = aux - c[8];
	if (c[3] < 0) c[1] = 0;
	
	aux = 0;
	for (i = 0; i <= s.size() - 1; i++) if (s[i] == 'F') aux++;
	c[5] = aux - c[4];
	if (c[5] < 0) c[1] = 0;
	
	aux = 0;
	for (i = 0; i <= s.size() - 1; i++) if (s[i] == 'V') aux++;
	c[7] = aux - c[5];
	if (c[7] < 0) c[1] = 0;
	
	aux = 0;
	for (i = 0; i <= s.size() - 1; i++) if (s[i] == 'N') aux++;
	c[9] = (aux - c[7] - c[1]) / 2;
	if (c[9] < 0) c[1] = 0;

	vector<int> o;
	o.clear();
	int j;
	for (i = 0; i <= 9; i++)
	{
		if (c[i] != 0)
		{
			for (j = 1; j <= c[i]; j++) o.push_back(i);
		}
	}
	for (i = 0; i <= o.size() - 1; i++)
	{
		out << o[i];
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
	string linha;
	getline(in, linha);
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