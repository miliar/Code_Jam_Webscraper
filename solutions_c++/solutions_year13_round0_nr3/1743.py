#include <iostream>
#include <string>
#include <vector>
#include <stdio.h>

using namespace std;

unsigned long long lsqrt(unsigned long long a)
{
	unsigned long long low = 0LL;
	unsigned long long high = a+1;
	unsigned long long mid;

	while(high-low > 1)
	{
		mid = (low+high)/2;

		if(mid*mid <= a)
			low = mid;
		else
			high = mid;
	}

	return low;
}

bool isPalindrome(unsigned long long a)
{
	char m[15];
	sprintf(m, "%llu",a);
	int len = strlen(m);
	if (m[len-1] == 0)
	{
		return false;
	}
	for (int i=0;i<len/2;i++)
	{
		if(m[i] != m[len-i-1])
			return false;
	}
	return true;
}

int main()
{
	freopen("int.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int n = 0;
	cin >> n;
	
	vector<unsigned long long> m;

	for(unsigned long long i = 1;i<=10000000;i++)
	{
		if(isPalindrome(i))
		{
			if (isPalindrome(i*i))
			{
				m.push_back(i*i);
			}
		}
	}

	unsigned long long r,l;
	int sum = 0;

	for(int i=0;i<n;i++)
	{
		cin >> l;
		cin >> r;

		for (int j=0;j<m.size();j++)
		{
			if(m[j] >= l && m[j] <= r)
			{
				sum++;
			}
		}

		cout << "Case #" << i+1 << ": " << sum << endl;
		sum = 0;
	}

	return 0;
}