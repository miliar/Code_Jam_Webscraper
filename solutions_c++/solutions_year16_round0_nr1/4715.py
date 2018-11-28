#include <vector>
#include <map>
#include <cstring>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <sstream>
#include <complex>
#include <queue>
#include <stack>
#include <map>
#include <bitset>
#include <iomanip>
#include <set>
#include <stack>
#include <stdio.h>

using namespace std;

bool check(int i, long long a)
{
	while(a > 0)
		if(a % 10 == i)
			return 1;
		else
			a /= 10;
	return 0;
}

int main()
{
	//freopen("A-large.in", "r", stdin);
	//freopen("outA2.out", "w", stdout);
	int T;
	cin >> T;

	for(int i = 1; i <= T; ++i)
	{
		int N;
		cin >> N;
		cout << "Case #" << i << ":";
		if(N == 0)
			cout << " INSOMNIA";
		else
		{
			vector<int> D;
			for(int j = 0; j < 10; ++j)
				D.push_back(j);
			long long P = 0;
			while(D.size() > 0)
			{
				P += N;
				for(int j = 0; j < D.size(); ++j)
					if(check(D[j], P))
					{
						D.erase(D.begin() + j);
						--j;
					}
			}
			cout << " " << P;
		}
		cout << endl;
	}

	return 0;
}