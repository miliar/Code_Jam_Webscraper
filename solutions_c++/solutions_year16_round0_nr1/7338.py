#include <iostream>
using namespace std;
int nums[10];
void process(long long int n)
{
	int len = 0;
	for (int i = 1; n%i != n; i *= 10)
	{
		len++;
	}
	for (int i = 0; i < len; i++)
	{
		nums[n - ((n/10)*10)] = 1;
		n = n/10;
	}
}
int check()
{
	for (int i = 0; i < 10; i++)
		if (nums[i] == 0)
			return 0;
	return 1;
}
int main()
{
	long long int n, t;
	cin>>t;
	for (int i = 1; i <= t; i++)
	{
		cin>>n;
		for (int j = 0; j < 10; j++)
			nums[j] = 0;
		if (n == 0)
			cout<<"Case #"<<i<<": INSOMNIA"<<endl;
		else
		{
			for (int k = 1; ;k++)
			{
				process(n*k);
				if (check())
				{
					cout<<"Case #"<<i<<": "<<n*k<<endl;
					break;
				}
			}
		}
	}
}
