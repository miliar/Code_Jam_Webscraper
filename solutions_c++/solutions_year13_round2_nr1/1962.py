#include "stdafx.h"
#include <iostream>
#include <vector>
#include <set>
#include <string>
#include <algorithm>

using namespace std;

int tryAdd(int A, const vector<int>& motes, int offset)
{
	for(; offset<motes.size(); ++offset)
	{
		if(A > motes[offset])
			A += motes[offset];
		else
			break;
	}	
	if(offset < motes.size())
	{
		int o_offset = offset;
		int n = 0;
		int limit = motes.size() - offset;
		while(A <= motes[offset] && n < limit)
		{
			n ++;
			A += A - 1;
		}
		if(A <= motes[offset])
			return limit;
		else
		{
			A += motes[offset];
			++offset;
			int r = tryAdd(A, motes, offset);
			return min(r + n, (int)(motes.size() - o_offset));
		}
	}
	return 0;
}

int _tmain(int argc, _TCHAR* argv[])
{
	int T;
	cin >> T;
	for(int c=0; c<T; ++c)
	{
		int A, N;
		cin >> A >> N;
		vector<int> motes, sum(N);
		copy_n(istream_iterator<int>(cin), N, back_inserter(motes));
		sort(motes.begin(), motes.end());
		int operations = tryAdd(A, motes, 0);
		/*
		int inc = A;
		for(int j=0; j<N; ++j)
		{
			int prev = inc;
			for(int i=0; i<N;++i)
			{
				prev = sum[i] += prev + motes[i];
			}
			int counter =  N - 1;
			for(; counter>0;--counter)
			{
				if(motes[counter] < 2 * sum[counter-1] - 1)
					break;
			}
			if(A <= motes[j] && (A == 1 || j >= counter))
			{
				operations += N - j;
				break;
			}
			operations += tryAdd(A, motes[j], inc);
		}
			*/
		cout << "Case #" << c+1 << ": " << abs(operations) << endl;
	}
	return 0;
}


