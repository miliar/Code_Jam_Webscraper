
#ifndef VC_SOLUTION_USED
#include "A.h"
#endif

#include <iostream>
#include <string>
#include <vector>

using namespace std;

void A()
{
	int T = 0;
	cin >> T;
	
	for(int t=1; t<=T; ++t)
	{
		int N=0;
		cin >> N;

		string pattern[100];
		bool stop = false;
		
		int counter[100][100];
		for(int i=0; i<100; ++i)
		{
			for(int j=0; j<100; ++j)
			{
				counter[i][j] = 0;
			}
		}

		int max_idx = -1;

		for(int n=0; n<N; ++n)
		{
			string tmp;
			cin >> tmp;

			if(stop)
				continue;

			int idx = -1;

			for(int i=0; i<tmp.length(); ++i)
			{
				if(i==0 || tmp[i] != tmp[i-1] )
				{
					pattern[n] += char(tmp[i]);
					counter[n][++idx] = 1;

					if(idx>max_idx)
						max_idx = idx;
				}
				else
				{
					++counter[n][idx];
				}
			}
			
			if(n>0 && pattern[n] != pattern[n-1])
			{
				stop = true;
			}
		}

		cout << "Case #" << t << ": " ;

		if(stop)
		{
			cout << "Fegla Won";
		}
		else
		{
			int step = 0;
			for(int j=0; j<=max_idx; ++j)
			{
				int average = 0;
				for(int i=0; i<N; ++i)
				{
					average += counter[i][j];
				}
				average = int ( (float)average/N + 0.5 );

				for(int i=0; i<N; ++i)
				{
					int d = average - counter[i][j];
					step += (d>=0)?d:-d;
				}
			}
			cout << step;
		}
		cout << endl;
	}
}

#ifndef VC_SOLUTION_USED
int main()
{
	A();
	return 0;
}
#endif