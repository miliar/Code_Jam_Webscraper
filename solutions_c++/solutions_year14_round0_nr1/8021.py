/*a.cpp
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

using namespace std;

#define For(i,m,n) for(int i = m; i < n; i++)
#define Fori(i,m,n) for(int i = m; i > n; i--)
#define pb push_back
#define all(v) v.begin(), v.end()
#define LL long long

int main()
{
	ios_base::sync_with_stdio(false);
	ifstream fin("A-small-attempt0.in");
	ofstream fout("A-small-attempt0.out");
	int n, a, b, t, m;
	int s1[5][5], s2[5][5];
	fin >> n;
	For(i, 0, n)
	{
		fin >> a;
		a--;
		For(j, 0, 4)
		{
			For(k, 0, 4)
			{
				fin >> t;
				s1[j][k] = t;
			}
		}
		fin >> b;
		b--;
		For(j, 0, 4)
		{
			For(k, 0, 4)
			{
				fin >> t;
				s2[j][k] = t;
			}
		}
		t = 0;
		For(j, 0, 4)
		{
			For(k, 0, 4)
			{
				if(s1[a][j] == s2[b][k])
				{
					t++;
					m = s1[a][j];
					break;
				}
			}
			if(t > 1)
				break;
		}
		if(t == 0)
			fout << "Case #" << (i + 1) << ": " << "Volunteer cheated!" << endl;
		else if(t == 1)
			fout << "Case #" << (i + 1) << ": " << m << endl;
		else
			fout << "Case #" << (i + 1) << ": " << "Bad magician!" << endl;
	}
	return 0;
}

