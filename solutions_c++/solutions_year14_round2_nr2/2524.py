#include <stdio.h>
#include <math.h>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
	int t;
	cin >> t;
	int caseid = 0;
	while(t--)
	{
		int ans = 0;
		int A,B,K;
		cin >> A >> B >> K;
		vector<int> v(K);
		for(int i = 0; i < K; i++)
			v[i] = i+1;
		
		for(int i = 0; i < A; i++)
		{
			for(int j = 0; j < B; j++)
			{
				if( (i&j) < K )
					ans++;
			}
		}
		cout << "Case #" << caseid+1 << ": " << ans << endl;
		caseid++;
	}		
	return 0;
}
