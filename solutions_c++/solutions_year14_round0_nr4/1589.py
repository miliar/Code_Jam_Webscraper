#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
	int caseN;
	cin >> caseN;
	for (int caseI = 1; caseI <= caseN; caseI++)
	{
		int n;
		double alice[1000], bob[1000];
		cin >> n;
		for (int i = 0; i < n; i++)
			cin >> alice[i];
		for (int i = 0; i < n; i++)
			cin >> bob[i];
		
		sort(alice, alice + n);
		sort(bob, bob + n);
		
		int ans1 = 0;
		for (int i = 0; i < n; i++)
		{
			bool flag = true;
			for (int j = i; j < n; j++)
				if (alice[j] < bob[j - i])
					flag = false;
			if (flag)
			{
				ans1 = n - i;
				break;
			}
		}
		
		int ans2 = 0;
		bool taken[1000];
		fill(taken, taken + n, false);
			
		for (int i = 0; i < n; i++)
		{
			int take = -1;
			for (int j = 0; j < n; j++)
				if (bob[j] > alice[i] && !taken[j])
				{
					take = j;
					break;
				}
			if (take == -1)
			{
				for (int j = 0; j < n; j++)
					if (!taken[j])
					{
						take = j;
						break;
					}
				ans2++;
			}
			taken[take] = true;
		}
			
		cout << "Case #" << caseI << ": " << ans1 << " " << ans2 << endl;
	}
	
	return 0;
}
