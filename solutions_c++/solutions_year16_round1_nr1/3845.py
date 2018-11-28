#include "stdafx.h"
#include <fstream>
#include <string>
#include <cstdlib>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>
#include <stdio.h>

#include <math.h>

using namespace std;

ofstream fout("OUT111.txt");
ifstream fin("INP111.txt");

int main() 
{
	int TT;
	fin >> TT;

	for (int tt = 0; tt < TT; tt++)
	{
		string s;
		fin >> s;

		string res = "";
		res.append(s, 0, 1);
		for (int i = 1; i < s.size(); i++)
		{
			char c = s[i];
			for (int j = 0; j < i; j++)
			{
				if (res[j] < c)
				{
					res = c + res;
					break;
				}
				else if (res[j] > c)
				{
					res = res + c;
					break;
				}
			}
			if (res.size() != i + 1)
				res = res + c;
		}

	    fout << "Case #" << tt + 1 << ": " << res << "\n";
	}

	return 0;
}

