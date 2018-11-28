#include <iostream>
#include <string>
#include <vector>
#include <iomanip>    
#include <algorithm>
using namespace std;

int main()
{
	int T;
	cin >> T;
	for (int t = 0; t < T; ++t)
	{
		int C, D, V;
		cin >> C >> D >> V;
		vector<char> possible(V + 1, false);
		vector<int> coins;
		for (int i = 0; i < D; ++i)
		{
			int c;
			cin >> c;
			coins.push_back(c);
		}
		sort(coins.begin(), coins.end());
		
		possible[0] = true;
		for (int i = 0; i < coins.size(); ++i)
		{
			for (int j = V; j >= 0; --j)
				if (possible[j] && j + coins[i] <= V)
					possible[j + coins[i]] = true;
		}

	//	for (int i = 0; i <= V; ++i)
//			cout << char(possible[i] + '0');
//		cout << endl;
		
		int answer = 0;
		for (int i = 0; i < possible.size(); ++i)
		{
			if (possible[i] == false)
			{
				answer ++;
				for (int j = V; j >= 0; --j)
					if (possible[j] && j + i <= V)
						possible[j + i] = true;
			}
		}
		cout << "Case #" << t + 1 << ": " << answer << endl;
	}
	return 0;
}