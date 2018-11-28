#include "stdafx.h"
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

int GetNumOfOps(vector<int> const & motes, int n, int startValue)
{
	int ops = 0;
	int pos = 0;
	while (pos < n)
	{
		while (pos < n && startValue > motes[pos]) 
			startValue += motes[pos++];

		if (pos != n)
		{
			if (startValue == 1)
				return motes.size() + 1;
			while (startValue <= motes[pos])
			{
				startValue += startValue - 1;
				++ops;
			}
		}
	}

	return ops;
}

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream ifstr("A-large.in");
	ofstream ofstr("A-large.out");

	int T;
	ifstr >> T;
	for (int t = 0; t < T; ++t)
	{
		long long A, N;
		ifstr >> A >> N;
		vector<int> motes(N);
		for (int n = 0; n < N; ++n)
			ifstr >> motes[n];

		sort(motes.begin(), motes.end());

		int count = N;
		for (int n = 0; n < N; ++n)
		{
			count = min(count, n + GetNumOfOps(motes, N - n, A));
		}

		ofstr << "Case #" << t + 1 << ": " << count << endl;
	}

	return 0;
}

