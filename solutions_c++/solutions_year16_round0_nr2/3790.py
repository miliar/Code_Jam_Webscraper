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

		int num = 1;
		int n = s.size();
		for (int i = 1; i < n; i++)
		{
			if (s[i] != s[i - 1])
				num++;
		}

		if (s[n - 1] == '+')
			num--;

	    fout << "Case #" << tt + 1 << ": " << num << "\n";
	}

	return 0;
}

