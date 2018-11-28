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
ifstream in("C:\\Users\\Casa\\Desktop\\GOOGLE CODE JAM\\B-large.in", ios_base::in);
ofstream out("C:\\Users\\Casa\\Desktop\\GOOGLE CODE JAM\\B-large_out.in", ios_base::out);

void pre_process()
{
	return;
}
ll para_mais(string s);
ll para_menos(string s);
ll para_mais(string s)
{
	if (s.size() == 2)
	{
		if (s[0] == '-' && s[1] == '-') return 1;
		if (s[0] == '+' && s[1] == '-') return 2;
		if (s[0] == '-' && s[1] == '+') return 1;
		if (s[0] == '+' && s[1] == '+') return 0;
	}
	string s2 = s.substr(0, s.size() - 1);
	if (s[s.size() - 1] == '+') return para_mais(s2);
	else                        return para_menos(s2) + 1;
}
ll para_menos(string s)
{
	if (s.size() == 2)
	{
		if (s[0] == '-' && s[1] == '-') return 0;
		if (s[0] == '+' && s[1] == '-') return 1;
		if (s[0] == '-' && s[1] == '+') return 2;
		if (s[0] == '+' && s[1] == '+') return 1;
	}
	string s2 = s.substr(0, s.size() - 1);
	if (s[s.size() - 1] == '+') return para_mais(s2)+1;
	else                        return para_menos(s2);
}
void case_solve()
{
	string s;
	getline(in, s);
	if (s.size() == 1)
	{
		if (s[0] == '+') out << "0";
		else             out << "1";
		return;
	}
	ll resp = para_mais(s);
	out << resp;

	
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
	string s;
	getline(in, s);
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