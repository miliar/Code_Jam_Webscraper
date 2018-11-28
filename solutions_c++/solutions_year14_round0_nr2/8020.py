/*b.cpp
 *  Created on: Apr 12, 2014
 *      Author: omar */


#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <string.h>
#include <vector>
#include <map>
#include <set>
#include <bitset>
#include <algorithm>
#include <stdio.h>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <cmath>
#include <iomanip>

using namespace std;

#define For(i,m,n) for(int i = m; i < n; i++)
#define Fori(i,m,n) for(int i = m; i > n; i--)
#define pb push_back
#define all(v) v.begin(), v.end()
#define LL long long

int main()
{
	ios_base::sync_with_stdio(false);
	ifstream fin("B-large.in");
	ofstream fout("B-large.out");
	int n;
	long double c, f, x, t, r;
	fin >> n;
	For(i, 0, n)
	{
		t = 0;
		r = 2;
		fin >> c >> f >> x;
		while(true)
		{
			if(x / r <= ((c / r) + (x / (f + r))))
			{
				t += (x / r);
				break;
			}
			else
			{
				t += (c / r);
				r += f;
			}
		}

		fout << "Case #" << (i + 1) << ": ";
		fout << std::fixed << std::setprecision(7) << t << endl;
	}
	return 0;
}

