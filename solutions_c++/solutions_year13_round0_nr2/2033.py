#include "stdafx.h"
#include <iostream>
#include <vector>
#include <set>
#include <string>
#include <algorithm>

using namespace std;

bool isvalid(const vector<vector<int>>& field, int r, int c, int N, int M)
{
	int value = field[r][c];
	bool valid = true;
	for(int i=0; i<M && valid; ++i)
		if(field[r][i] > value)
			valid = false;
	if(!valid)
	{
		valid = true;
		for(int i=0; i<N && valid; ++i)
			if(field[i][c] > value)
				valid = false;
	}
	return valid;
}

int _tmain(int argc, _TCHAR* argv[])
{
	int T;
	cin >> T;
	for(int t=0; t<T; ++t)
	{
		int N, M;
		cin >> N >> M;
		vector<vector<int>> field(N);
		for(int i=0;i<N; ++i)
		{
			copy_n(istream_iterator<int>(cin), M, back_inserter(field[i]));
		}
		bool valid = true;
		for(int r=0; r<N && valid; ++r)
			for(int c=0; c<M && valid; ++c)
			{
				valid = isvalid(field, r, c, N, M);
			}
		cout << "Case #" << t+1 << ": " << (valid ? "YES" : "NO") << endl;
	}
	return 0;
}

