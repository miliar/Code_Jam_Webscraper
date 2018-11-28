#include <iostream>
#include <cstdio>
using namespace std;

int main()
{
	int ncase;
	
	freopen("1.txt", "r", stdin);
	freopen("2.txt", "w", stdout);
	cin >> ncase;

	for(int icase = 0;icase < ncase;icase++)
	{
		int n;
		cin >> n;
		int arr[1005];
		int maxP = 0;
		int res = 1005;
		for(int i = 0;i < n;i++)
		{
			cin >> arr[i];
			maxP = max(arr[i], maxP);
		}
		
		for(int baseP = 1;baseP <= maxP;baseP++)
		{
			int tempRes = baseP;
			for(int i = 0;i < n;i++)
				tempRes += (arr[i] + baseP - 1) / baseP - 1;

			res = min(res, tempRes);
		}

		cout << "Case #" << icase + 1 << ": " << res << endl;
	}

	return 0;
}
