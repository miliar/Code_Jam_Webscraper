#define _CRT_SECURE_NO_DEPRECATE
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <deque>
#include <queue>
#include <list>
#include <stack>
#include <bitset>
#include <cmath>
#include <ctime>
#include <complex>
#include <cstring>
#include <cstdlib>
#include <iomanip>
#include <sstream>
using namespace std;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int n;
	cin >> n;
	for (int i = 0; i < n; i++)
	{
		int numb;
		cin >> numb;
		map<int, int>a;
		a[0] = 0;
		a[1] = 0;
		a[2] = 0;
		a[3] = 0;
		a[4] = 0;
		a[5] = 0;
		a[6] = 0;
		a[7] = 0;
		a[8] = 0;
		a[9] = 0;
		bool end;
		for (int j = 1; j < 100; j++)
		{
			int line = j*numb;
			int temp = line;
			while (temp > 0)
			{
				a[temp % 10]++;
				temp /= 10;
			}
			end = true;
			bool step = false;
			for (int i = 0; i < 10; i++)
			{
				if (a[i] == 0) { end = false; }
			}
			if (numb==0) { cout << "Case #"<<i+1<<": "<<"INSOMNIA" << endl; break; }
			if (end) { cout << "Case #" << i + 1 << ": "<< line << endl; break; }
		}

	}

	return 0;
}