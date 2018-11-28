#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <set>
#include <list>
#include <map>
#include <deque>
#include <string>

using namespace std;

int t,T;

#define ULL unsigned long long

void runtestcase()
{	
	string S;
	ULL K;
	ULL r = 0;
	cin >> S >> K;
	for (ULL k = 0; k < S.size(); k++)
	{
		if (S[k] == '-')
		{
			if (k + K - 1 >= S.size())
			{
				cout << "IMPOSSIBLE";
				return;
			}
			for (ULL kk = 0; kk < K; kk++)
			{
				if (S[k+kk] == '-')
					S[k+kk] = '+';
				else
					S[k+kk] = '-';
			}
			r++;
		}
	}
	cout << r;
}

void main()
{	
	cin >> T;
	for (t = 1; t <= T; t++)
	{
		cerr << t;
		cout << "Case #" << t << ": ";
		runtestcase();
		cout << endl;
	}	
}