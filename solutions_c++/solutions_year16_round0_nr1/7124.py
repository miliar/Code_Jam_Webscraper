#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>

using namespace std;

bool digit[10];

int main()
{
	ifstream cin("a.in");
	ofstream cout("a.out");
	int t;
	cin >> t;
	for (int k = 1; k <= t;k++)
	{
		memset(digit, false, sizeof(digit));
		int n;
		cin >> n;
		if (n == 0)
		{
			cout << "Case #" << k << ": INSOMNIA\n";
			continue;
		}

		for (int i = 1;; i++)
		{	
			int m = n*i;
			while (m > 0)
			{
				digit[m % 10] = true;
				m /= 10;
			}
			bool found = true;
			for (int j = 0; j < 10; j++)
			{
				if (digit[j] == false)
				{
					found = false;
					break;
				}
			}
			if (found)
			{
				cout << "Case #" << k << ": " << n*i << endl;
				break;
			}
		}
	}
	return 0;
}