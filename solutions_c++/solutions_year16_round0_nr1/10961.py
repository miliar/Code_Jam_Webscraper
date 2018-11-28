#include <iostream>
#include <cmath>
#include <map>
#include <string>
#include <cstdlib>
#include <cstdio>
#include <vector>
#include <set>
#include <iomanip>
#include <algorithm>

using namespace std;

typedef long double LD;
typedef long long int LL;

bool arr[10] = {false};

bool status()
{
	for (int i = 0; i < 10; ++i)
	{
		if (false == arr[i])
		{
			return false;
		}
	}
	return true;
}

int main()
{
	freopen("A-large.in","r",stdin);freopen("A-large-attempt0.out","w",stdout);
	int test;
	cin >> test;
	for (int t = 1; t <= test; ++t)
	{
		LL n;
		cin >> n;
		cout << "Case #" << t << ": ";
		if (0 == n)
		{
			cout << "INSOMNIA";
		}
		else
		{
			for (int i = 0; i < 10; ++i) {arr[i] = false;}
			LL count = 1, num = 0;
			while (1)
			{
				LL number = count * n;
				num = number;
				while (0 < number)
				{
					arr[number % 10] = true;
					number /= 10;
				}
				if (true == status())
				{
					break;
				}
				++count;
			}
			cout << num;
		}
		cout << endl;
	}
	return 0;
}