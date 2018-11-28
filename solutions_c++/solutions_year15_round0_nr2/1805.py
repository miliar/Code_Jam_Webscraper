#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int main()
{
	int T;
	cin >> T;
	for (int i = 0; i < T; ++i)
	{
		int D,max1=INT_MIN,res,sum;
		cin >> D;
		vector<int> P(D);
		for (int j = 0; j < D; ++j)
		{
			cin >> P[j];
			max1 = max(max1, P[j]);
		}
		res = max1;
		for (int j = 1; j <= max1; j++) 
		{
			sum = j;
			for (int k = 0; k < D; k++)
			{
				if (P[k] > j) 
				{
					if (P[k] % j == 0)
						sum += (P[k] / j - 1);
					else
						sum += (P[k] / j);
				}
			}
			res = min(res, sum);
		}
		cout << "case #" << i + 1 << ": " << res << endl;
	}
	return 0;
}