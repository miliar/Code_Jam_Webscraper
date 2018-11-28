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
		long long N;
		fin >> N;

		if (N == 0)
		{
			fout << "Case #" << tt + 1 << ": " << "INSOMNIA" << "\n";
			continue;
		}

		bool a[10] = {};
		for (int i = 0; i < 10; i++)
			a[i] = false;

		long long curN = N;

		int num = 0;
		while (num < 10)
		{
			long long t = curN;
			while (t > 0)
			{
				int r = t % 10;
				if (!a[r])
				{
					a[r] = true;
					num++;
				}
				t = (t - r) / 10;
			}
			curN = curN + N;
		}

	    fout << "Case #" << tt + 1 << ": " << (curN - N) << "\n";
	}

	return 0;
}

