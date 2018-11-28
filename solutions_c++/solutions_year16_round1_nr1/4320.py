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
bool compara(string s1, string s2)
{
	int ult = s1.size()-1;
	int i;
	for (i = 0; i <= ult; i++)
	{
		if (s1[i] < s2[i]) return 0;
		if (s1[i] > s2[i]) return 1;
	}
	return 0;
}
void case_solve()
{
	string s;
	getline(in, s);
	if (s.size() == 1)
	{
		out << s;
		return;
	}
	int i;
	string atual,s1,s2;
	atual.push_back(s[0]);
	for (i = 1; i <= s.size() - 1; i++)
	{
		s1 = atual;
		s2 = atual;
		s1.push_back(s[i]);
		string aux;
		aux.clear();
		aux.push_back(s[i]);
		s2.insert(0, aux);
		if (compara(s1,s2))   atual = s1;
		else                  atual = s2;
	}
	out << atual;
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