#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
using namespace std;

int main()
{
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++)
	{
		int Smax, toI = 0;
		cin >> Smax;
		vector<int> S;
		int sum = 0;
		for (int i = 0; i <= Smax; i++)
		{
			char c;
			cin >> c;
			S.push_back(c - '0');
			sum += (c - '0');
		}
		int m = 0, g = 0;
		while (sum > 0)
		{
			for (; m < min(g+1, (int)S.size()); m++)
			{
				sum -= S[m];
				g += S[m];
			}
			if (sum > 0){
				toI++;
				g++;
			}
		}
		cout << "Case #" << t << ": " << toI << endl;
	}
	return 0;
}