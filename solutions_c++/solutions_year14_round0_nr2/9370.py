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
#include <iomanip>
#include <sstream>
#include <cctype>
#include <climits>

using namespace std;

typedef pair<double,double> p;
#define mp make_pair

ifstream fin ("B-small.in");
ofstream fout ("B-small.out");

int i, j, k, cc;
double c, f, x, sum, sol;

int main()
{	
	fin >> cc;
	for(k=1;k<=cc;k++)
	{
		fin >> c >> f >> x;
		sol = x / 2.0;
		for(i=1;true;i++)
		{
			sum = 0;
			for(j=0;j<i;j++)
			{
				sum += c / (2.0 + j * f);
			}
			if(sum > sol)
				break;
			sum += x / (2.0 + i * f);
			if(sum < sol)
				sol = sum;
		}
		fout << "Case #" << k << ": " << fixed << setprecision(7) << sol;
		if(k < cc)
			fout << endl;			
	}

	//Close Files
    fin.close();
    fout.close();
	return 0;
}