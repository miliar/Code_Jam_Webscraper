#include <bits/stdc++.h>

using namespace std;
#define MAX 1010

int t,d,x;
vector<int> v;

int main(void)
{
	cin >> t;

	int cases = 0;
	while (t--)
	{
		cin >> d;
		
		v.clear();

		int maior = 0;
		for (int i = 0; i < d; ++i)
		{
			cin >> x;
			maior = max(maior, x);
			v.push_back(x);
		}

		int ans = 0x3f3f3f3f;

		for (int i = 1; i <= maior; ++i)
		{
			int sum = 0;
			for (int j = 0; j < v.size(); ++j)
			{
				int k = (v[j] + i - 1)/i;
				if (v[j] == i)
					continue;
				sum += k - 1;
			}
			ans = min(ans, sum + i);
		}
		cout << "Case #" << ++cases << ": " << ans << "\n";
	}
	return 0;
}