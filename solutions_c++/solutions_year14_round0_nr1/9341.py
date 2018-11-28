#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cassert>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <utility>
#include <numeric>
#include <algorithm>
#include <bitset>
#include <complex>
#include <fstream>
using namespace std;

typedef pair<double,double> p;
#define mp make_pair

int c, a[5], b[5], c1, c2, temp, i, j, k, sol;

ifstream fin ("A-small.in");
ofstream fout ("A-small.out");

int main()
{	
	fin >> c;
	for(k=1;k<=c;k++)
	{
		fin >> c1;
		for(i=1;i<=4;i++)
		{
			for(j=1;j<=4;j++)
			{
				if(i != c1)
					fin >> temp;
				else
					fin >> a[j];
			}
		}
		fin >> c2;
		for(i=1;i<=4;i++)
		{
			for(j=1;j<=4;j++)
			{
				if(i != c2)
					fin >> temp;
				else
					fin >> b[j];
			}
		}
		sol = 0;
		for(i=1;i<=4;i++)
			for(j=1;j<=4;j++)
			{
				if(a[i] == b[j])
				{
					sol ++;
					temp = a[i];
					break;
				}
			}

		fout << "Case #" << k << ": ";
		if(sol == 1)
			fout << temp;
		else if(sol == 0)
			fout << "Volunteer cheated!";
		else 
			fout << "Bad magician!";

		if(k < c)
			fout << endl;
			
	}

	//Close Files
    fin.close();
    fout.close();
	return 0;
}