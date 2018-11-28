#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <set>
using namespace std;

int main()
{
	int caseN;
	cin >> caseN;
	for (int caseI = 1; caseI <= caseN; caseI++)
	{
		int n, m;
		cin >> n >> m;
		
		multiset<int> sizes;
		for (int i = 0; i < n; i++)
		{
			int x;
			cin >> x;
			sizes.insert(x);
		}
		
		int ans = 0;
		while (sizes.size())
		{
			ans++;

			int a = *sizes.begin();
			sizes.erase(sizes.begin());
			
			if (sizes.size())
			{
				multiset<int>::iterator it = sizes.upper_bound(m - a);
				if (it != sizes.begin())
					sizes.erase(--it);
			}
		}
		
		cout << "Case #" << caseI << ": " << ans << endl;
	}
	
	return 0;
}
