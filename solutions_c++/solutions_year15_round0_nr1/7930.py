#include<iostream>
#include<string>
#include<math.h>
#include<vector>
#include<queue>
#include<algorithm>
#include<cstdio>
#include<cstdlib>
#include<string.h>
#include<map>

using namespace std;


int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t;
	cin >> t;
	for (int ii = 1; ii <= t; ii++)
	{
		int result = 0,aud,n;
		char x;
		cin >> n>>x;
		aud = x - '0';
		for (int i = 1; i <= n; i++)
		{
			int cur;
			cin >> x;
			cur = x - '0';
			if (cur == 0)
				continue;
			if (i>aud)
			{
				result += (i - aud);
				aud += (i - aud);
			}
			aud += cur;
			

		}


		cout << "Case #" << ii << ": " << result << endl;
	}
	return 0;
}

