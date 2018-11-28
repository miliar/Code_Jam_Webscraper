/*
 * Problem B. Lawnmower.cpp
 *
 *  Created on: Apr 13, 2013
 *      Author: sara
 */

#include <algorithm>
#include <cmath>
#include <complex>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <memory.h>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <stdio.h>
#include <utility>
#include <vector>

using namespace std;

int main()
{

	freopen("B-large.in", "rt", stdin);
	freopen("B-large.out", "wt", stdout);
	int t;
	scanf("%d", &t);

	int c = 1;
	int n, m;

	while ( c<=t )
	{
		scanf("%d%d", &n, &m);
		vector<int> maxRow(n);
		vector<int> maxCol(m);

		vector<vector<int> > lawn(n, vector<int>(m));
		for(int i = 0 ; i < n; i++)
			for(int j = 0; j < m; j++)
			{
				scanf("%d", &lawn[i][j]);
				if(lawn[i][j] > maxRow[i])
					maxRow[i] = lawn[i][j];
				if(lawn[i][j] > maxCol[j])
						maxCol[j] = lawn[i][j];
			}

		bool valid = true;

		for(int i = 0 ; i < n; i++)
			for(int j = 0; j < m; j++)
			{
				if(lawn[i][j] < maxRow[i] && lawn[i][j] < maxCol[j])
				{
					valid = false;
					break;
				}
			}

		if(valid)
			printf("Case #%d: YES\n", c);
		else
			printf("Case #%d: NO\n", c);

		c++;
	}

	return 0;
}	
	













