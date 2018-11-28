#include <iostream>
#include <string>
#include <stdio.h>
using namespace std;

int main ()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);

	int TC;
	cin >> TC;
	int CC = 1;
	while (TC--)
	{
		long long N;
		cin >> N;
		if (N == 0)
		{
			printf("Case #%d: INSOMNIA\n",CC++);
			continue;
		}

		long long cur = N;
		bool arr[10] = {0};
		while (1)
		{
			long long x = cur;
			while (x)
			{
				arr[x%10] = 1;
				x /= 10;
			}
			bool ok = 1;
			for (int i=0 ; i<10 ; i++)
				if (!arr[i]) ok = 0;

			if (ok) break;
			cur += N;
		}
		
		printf("Case #%d: %lld\n",CC++,cur);

	}
}