#include <bits/stdc++.h>

using namespace std;

const int NOD = 10;
bool used[NOD];

void initUsed()
{
	for (int i=0;i<NOD;i++)
	{
		used[i] = false;
	}
}

void processNumber(long long n)
{
	while (n != 0)
	{
		used[n%10] = true;
		n = n/10;
	}
}

bool isDoneProcessing()
{
	bool ret = true;
	for (int i=0;i<NOD;i++)
	{
		ret = ret && used[i];
	}
	return ret;
}

int main()
{
	int T;
	cin>>T;
	for (int i=0;i<T;i++)
	{
		long long n;
		cin>>n;
		if (n==0)
		{
			printf("Case #%d: INSOMNIA\n", i+1);
			continue;
		}
		long long x = 0;
		initUsed();
		do
		{
			x += n;
			processNumber(x);
		} while (!isDoneProcessing());
		printf("Case #%d: %lld\n", i+1, x);
	}
	return 0;
}