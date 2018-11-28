#include <iostream>
#include <vector>

using namespace std;

int D;
int p[1100];

int main()
{
	int T, x;
	cin >> T;
	for (int ncase = 1; ncase <= T; ncase++)
	{
		cin >> D;

		int max_p = -1;
		for (int i = 0; i < D; i++)
		{			
			cin >> p[i];
			max_p = max(max_p, p[i]);
		}

		int min_ans = max_p;
		for (int i = 1; i <= max_p; i++)
		{
			int ans = i;
			for (int j = 0; j < D; j++)
				if (p[j] > i)
					ans += (p[j] / i - (p[j] % i == 0));
			min_ans = min(min_ans, ans);
		}

		cout << "Case #" << ncase << ": " << min_ans << endl;
	}
}