// ConsoleApplication1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include<fstream>
using namespace std;

int verificare(int v[], int n) {
	int i;
	for (i = 0; i < n; i++)
		if (v[i] != 1) return 0;
	return 1;
}

int main()
{
	int n, i, j;
	int cases;
	ifstream f("file2.in");
	ofstream g("file3.out");

	

	f >> cases;

	for (j = 1; j <= cases; j++)
	{

		f >> n;

		if (n == 0) {
			g << "Case #" << j << ": " << "INSOMNIA" << '\n';
		}
		else
		{
			int ok = 1, v[10], aux;
			for (i = 0; i <= 9; i++)
				v[i] = 0;
			for (i = 1; ok == 1; i++)
			{
				aux = n*i;
				while (aux != 0) {
					v[aux % 10] = 1;
					aux /= 10;
				}
				if (verificare(v, 10)) ok = 0;
			}
			g << "Case #" << j << ": " << (i - 1)*n << '\n';
		}
	}
	
	return 0;
}

