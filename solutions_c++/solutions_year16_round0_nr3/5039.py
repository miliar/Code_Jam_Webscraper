#include <iostream>
#include <algorithm>
#include <cmath>
#include <stack>
#include <vector>

using namespace std;

long long isNotPrime(long long n)
{
	for (long long i = 2; i * i <= n; i++) if (n % i == 0) return i;

	return 0;
}

long long toBinary(long long n)
{
	long long temp = 0;

	stack<bool> num;

	while (n > 0)
	{
		num.push(n % 2);

		n /= 2;
	}

	while (!num.empty())
	{
		temp = (temp * 10) + num.top();
		
		num.pop();
	}

	return temp;
}

long long ok(long long num, double base, long long n)
{
	long long temp = 0;

	for (long long i = 0; i < n; i++)
	{
		temp += ((long long)pow(base, i) * (num % 10));

		num /= 10;
	}

	return temp;
}

int main()
{
	ios::sync_with_stdio(0);

	long long n, jam, t, counter = 1;

	cin >> t;

	while (t--)
	{
		cin >> n >> jam;

		vector<long long> divids;

		vector <vector < long long > > result;

		long long start = (long long)pow(2.0, n - 1);

		long long end = (long long)pow(2.0, n);

		for (long long i = start + 1; i < end && jam > 0; i += 2)
		{
			long long temp = toBinary(i);

			divids.clear();

			if(temp % 10 == 1)
			{
				for (double j = 2; j <= 10; j++)
				{
					long long div = isNotPrime(ok(temp, j, n));
	
					if (div) divids.push_back(div);
	
					else break;
				}
	
				if (divids.size() == 9)
				{
					divids.push_back(temp);
	
					result.push_back(divids);
	
					jam--;
				}
			}
		}

		cout << "Case #" << counter << ":" << endl;

		for (long long i = 0; i < result.size(); i++)
		{
			vector<long long> temp = result[i];

			cout << temp[temp.size() - 1] ;

			for (long long j = 0; j < temp.size() - 1; j++)
			{
				cout << " " << temp[j];
			}

			cout << endl;
		}

		counter++;
	}
}
