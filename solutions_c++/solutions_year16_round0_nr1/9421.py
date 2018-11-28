#include<bits/stdc++.h>

using namespace std;

int numbers[10];

bool check()
{
	for(int i = 0;i <= 9;i++)
	{
		if(numbers[i] != 1)
		{
			return false;
		}
	}
	return true;
}

bool fill(long long int n)
{
	while(n != 0)
	{
		int x = n%10;
		numbers[x] = 1;
		n = n/10;
	}

	if(check() == true)
	{
		return true;
	}
	else
	{
		return false;
	}
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("output.out", "w",stdout);
	int t;
	cin >> t;
	int county = 0;
	while(t--)
	{
		county++;
		bool flag = false;
		long long int n;
		long long int num;
		cin >> n;
		memset(numbers,0,sizeof(numbers));
		for(int i = 1;i <= 100000;i++)
		{
			num = i*n;
			if(fill(num) == true)
			{
				flag = true;
				break;
			}
		}

		if(flag == true)
		{
			cout << "Case #" << county<< ": " << num << endl;
		}
		else
		{
			cout << "Case #" << county << ": " << "INSOMNIA" << endl;
		}
	}
	return 0;
}
