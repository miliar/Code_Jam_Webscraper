#include <iostream>
#include <stdio.h>
#include <string>
using namespace std;


int main()
{
	FILE *f1, *f2;
	freopen_s(&f1, "in.txt", "r+",stdin);
	freopen_s(&f2, "out.txt", "w+", stdout);
	int T;
	cin >> T;
	for (int i = 1; i <= T; i++)
	{
		bool ns[10];
		for (int k = 0; k < 10; k++)
		{
			ns[k] = false;
		}
		bool flag = false;
		long long N;
		cin >> N;
		long long buf;
		if (N == 0)
		{
			printf("Case #%d: INSOMNIA\n", i);
			continue;
		}
		long long j = 1;
		for (; !flag; j++)
		{
			buf = j*N;
			while (buf)
			{
				ns[buf % 10] = true;
				buf /= 10;
			}
			flag = true;
			for (int k = 0; k < 10; k++)
			{
				if (!ns[k])
				{
					flag = false;
					break;
				}
			}
		}
		printf("Case #%d: %llu\n", i, N*(j-1));
	}
return 0;
}

