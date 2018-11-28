#include <iostream>
#include <ctime>
#include <iomanip>
#include <stdio.h>
#include <string.h>
#include <fstream>
#pragma warning(disable : 4996)
#define _CRT_SECURE_NO_WARNINGS
using namespace std;

int main()
{
	ofstream fout("2.txt");
	ifstream fin("test1.txt");
	int A[10] = { 0 };
	int n, m = 0, digit, j, l = 0, h = 0;
	fin >> n;
	while (n != 0)
	{
		l = 0;
		for (int i = 0; i < 10; i++)
			A[i] = 0;
		m++;
		fin >> digit;
		if (digit==0)
			fout << "Case #" << m << ": INSOMNIA" << endl;
		else{
			int no = digit;
			h = 2;
			while (l < 10)
			{
				while (digit != 0)
				{
					j = digit % 10;
					if (A[j] == 0)
					{
						A[j] = 1;
						l++;
					}
					digit /= 10;
				}
				digit = no* h;
				h++;
			}
			fout << "Case #" << m << ": " << no*(h - 2) << endl;
		}
		n--;
	}
	return 0;
}