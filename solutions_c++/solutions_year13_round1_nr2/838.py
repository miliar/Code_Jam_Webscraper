// CJR1_1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <fstream>
#include <vector>
#include <algorithm>
#define ull unsigned long long int
#define ui unsigned int
using namespace std;

int main()
{
	fstream fsin("C:\\Users\\basu_lucifer\\Downloads\\B-small-attempt0 (1).in", ios::in), fsout("C:\\Users\\basu_lucifer\\Downloads\\output.out", ios::out | ios::trunc);
	int t;
	ui e,r,n;
	fsin >> t;
	for(int ts = 1; ts <=t; ++ts)
	{
		fsin >> e >> r >> n;
		vector<ui> v(n+1);
		for(int i = n; i > 0; --i)
			fsin >> v[i];
		vector<vector<ui>> dp(n+1, vector<ui>(e+1, 0));
		
		for(ui i = 1; i <= n; ++i)
		{
			for(ui j = 1; j <=e ; ++j)
			{
				for(ui k = 0; k <= e;++k)
				{
					if(j >= k)
					{
						dp[i][j] = max(dp[i][j], dp[i-1][min(j-k+r,e)] + k*v[i]);
					}

				}
			}
		}
		fsout <<"Case #" << ts << ": " <<  dp[n][e] << endl;  
	}
	fsin.close();
	fsout.close();
	return 0;
}



