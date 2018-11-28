// ConsoleApplication3.cpp : main project file.

#include "stdafx.h"
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <fstream>
#include <algorithm>

using namespace std;

int main()
{
	int t;
	ifstream fcin;
	fcin.open("A-large.in");
	ofstream fcout;
	fcout.open("outl.txt");
	fcin >> t;
	for (int i = 0; i < t; i++) 
	{
		int a;
		fcin >> a;
		if (a==0)
		{
			fcout << "Case #" << i + 1 << ": " << "INSOMNIA" << endl;
			continue;
		}
		int* c;
		c = new int[10];
		for (int j = 0; j < 10; j++)
		{
			c[j] = 0;
		}
		int masolat = 0;
		while (c[1] == 0 || c[2] == 0 || c[3] == 0 || c[4] == 0 || c[5] == 0 || c[6] == 0 || c[7] == 0 || c[8] == 0 || c[9] == 0 || c[0] == 0)
		{
			masolat += a;
			int masolat2;
			masolat2 = masolat;
			while (masolat2 != 0)
			{
				c[masolat2 % 10] = 1;
				masolat2 /= 10;

			}


		}
		fcout <<"Case #" << i+1 << ": " << masolat<<endl;

		delete[] c;
	}
	fcout.close();
    return 0;
}
