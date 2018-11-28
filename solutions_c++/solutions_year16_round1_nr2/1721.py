#include <iostream>
using namespace std;

int main(void)
{
	int cnt[3000];
	int res[50];
	int t, n, h;
	cin >> t;
	for (int k = 1; k <= 2500; ++k)
	{
		cnt[k] = 0;
	}

	for (int i = 1; i <= t; ++i)
	{
		cin >> n;
		int iterCnt = (2 * n - 1) * n;
		for (int k = 0; k < iterCnt; ++k)
		{
			cin >> h;
			cnt[h]++;
		}

		int resCnt = 0;
		for (int k = 1; k <= 2500; ++k)
		{
			if (cnt[k] % 2 == 1)
			{
				res[resCnt++] = k;
			}
			cnt[k] = 0;
		}


		cout << "Case #" << i << ":";
		for (int k = 0; k < resCnt; ++k)
		{
			cout << " " << res[k];
		}
		cout << endl;
	
	}
	

	return 0;
}