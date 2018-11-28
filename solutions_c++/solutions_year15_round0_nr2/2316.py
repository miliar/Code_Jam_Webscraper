#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
using namespace std;

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("b.out", "w", stdout);
	int T;
	int der[1010];
	while(cin >> T)
	{
		for(int j = 1; j <= T; j++)
		{
			int d;
			cin >> d;
			for(int i = 0; i < d; i++)
			{
				cin >> der[i];
			}
			int flag = 0, rst = 1010;
			for(int i = 1; i < 1010; i++)
			{
				flag = i;
				for(int k = 0; k < d; k++)
				{
					if(der[k] > i)
					{
						flag += der[k] / i;
						if(der[k] % i == 0)
							flag--;
					}
				}
				rst = min(rst, flag);
			}
			cout << "Case #" << j << ": " << rst << endl;
		}
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}
