// CJ13_LawnMover.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <fstream>
#include <vector>
#include <string>

using namespace std;

int main()
{
	fstream fsin("C:\\Users\\basu_lucifer\\Downloads\\B-small-attempt1.in", ios::in), fsout("C:\\Users\\basu_lucifer\\Downloads\\output.out", ios::out | ios::trunc);
	int t,n,m;
	fsin >> t;
	for(int ts = 1; ts <=t; ++ts)
	{
		bool poss = true;
		fsin >> n >> m;
		vector<vector<int>> mat(n, vector<int>(m));
		for(int i = 0; i < n; ++i)
			for(int j = 0; j < m; ++j)
				fsin >> mat[i][j];

		for(int i = 0; i < n; ++i)
		{
			for(int j = 0; j < m; ++j)
			{
				if(mat[i][j] == 1)
				{
					int k1 = -1;
					while(++k1 < m)
					{
						if(mat[i][j] != mat[i][k1])
							break;
					}
					int k2 = -1;
					while(++k2 < n)
					{
						if(mat[i][j] != mat[k2][j])
							break;
					}
					if((k1 < m) && (k2 < n))
					{
						poss = false;
						break;
					}
				}
			}
			if(!poss)
				break;
		}

		fsout <<"Case #" << ts << ": " << (poss ? "YES" : "NO") << endl;  
	}
	fsin.close();
	fsout.close();
	return 0;
}

