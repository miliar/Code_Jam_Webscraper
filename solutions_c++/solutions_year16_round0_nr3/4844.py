#include <iostream>
#include <vector>
#include <set>
#include <algorithm>
#include <cmath>
using namespace std;

vector < long long int > v;

long long int converttobase(long long int number, long long int b)
{
	long long int res = 0;
	long long int mult = 1;
	while (number)
	{
		res += (number%10)*mult;
		number/=10;
		mult*=b;
	}
	return res;
}

long long int atoi(string str)
{
	long long int res = 0;
	for (long long int i=0; str[i]; ++i)
		res = (res*10)+(str[i]-'0');
	return res;
}

int check(long long int n)
{
	for (long long int i=2; i<=10; ++i)
	{
		int factorfound = 0;
		long long int convert = converttobase(n, i);

		for (long long int j=2; j<=sqrt(convert); ++j)
		{
			if (convert%j == 0)
			{
				factorfound++;
				v.push_back(j);
				break;
			}
		}
		if (factorfound == 0)
			return 0;
	}
	if (v.size() == 9)
		return 1;
	else
		return 0;
}

void jamcoins(long long int n, long long int j)
{
	long long int found = 0, limit = pow(2, n-2);
	long long int curr, num;

	for (long long int i=0; i<limit && found!=j; ++i)
	{
		curr = i;
		string res = "";
		while (curr)
		{
			res = ((char)(curr%2 + '0')) + res;
			curr >>= 1;
		}
		while (res.length() != n-2)
			res = "0" + res;
		res = "1" + res + "1";
		num = atoi(res);

		v.clear();
		int result = check(num);
		if (result == 1)
		{
			found++;
			cout << num;
			for (long long int i=0; i<v.size(); ++i)
				cout << " " << v[i];
			cout << endl;
		}
	}
}

int main()
{
	int t; cin >> t;
	long long int n, j;
	while (t--)
	{
		cin >> n >> j;
		cout << "Case #1:\n";
		jamcoins(n, j);
	}
	return 0;
}