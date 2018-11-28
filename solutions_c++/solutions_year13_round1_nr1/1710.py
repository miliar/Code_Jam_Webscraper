// 1Aa.cpp : Defines the entry point for the console application.
//


#include "stdafx.h"
#include <fstream>

using namespace std;

long int solve(unsigned long long r, unsigned long long t);

int main()
{
	int T;
	char strBuff[50];
	unsigned long long r, t;
	


	ifstream fin;
	fin.open("A.txt", ifstream::in);

	ofstream fout;
	fout.open("Output.txt", ofstream::out);

	fin.getline(strBuff, 50);

	sscanf(strBuff, "%d", &T);

	for (int i = 0; i < T; i++)
	{
		fout << "Case #" << (i+1) << ": ";

		fin.getline(strBuff, 50);

		sscanf(strBuff, "%llu %llu", &r, &t);

		fout << solve(r, t) << "\n";

	}
	fout.close();
	
	fin.close();

//	cin.get();
}

long int solve (unsigned long long r, unsigned long long t)
{
	unsigned long long irad, orad;
	unsigned long long paint_used;
	long int rings;

	irad = r * r;

	r++;

	orad = r * r;

	paint_used = orad - irad;

	rings = 1;

	while (paint_used <= t)
	{
		r++;
		irad = r*r;
		r++;
		orad = r*r;
		paint_used += (orad - irad);
		rings++;
	}

	return rings-1;
}