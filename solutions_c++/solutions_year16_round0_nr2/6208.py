#include <iostream>
#include <ctime>
#include <iomanip>
#include <stdio.h>
#include <string.h>
#include <fstream>
#include <string>
#pragma warning(disable : 4996)
#define _CRT_SECURE_NO_WARNINGS
using namespace std;

int main()
{
	ofstream fout("2.txt");
	ifstream fin("test1.txt");
	int A[100] = { 0 };
	string line;
	int n, m = 0, digit, j, l = 0, h = 0;
	fin >> n;
	getline(fin, line);
	while (n != 0)
	{
		l = 0;
		for (int i = 0; i < 100; i++)
			A[i] = 0;
		m++;		
		getline(fin, line);
		for (int i = 0; i < line.size();i++)
		if (line[i] == '+')
			A[i] = 1;
		for (int i = line.size() - 1; i >= 0; i--)
		{
			if (A[i] == 0)
			{
				l++;
				for (int j = i; j >= 0; j--)
				{
					if (A[j] == 0)
						A[j] = 1;
					else
						A[j] = 0;
				}
			}
		}
		fout << "Case #" << m << ": " << l << endl;
		n--;
	}
	return 0;
}