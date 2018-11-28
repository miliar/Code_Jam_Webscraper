#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <vector>
#include <string>

using namespace std;

int main() {
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("out", "w", stdout);
	int t, x, count = 0, temp;
	string s;
	vector<int> k;
	cin >> t;
	for (int i = 1; i <= t; i++)
	{
		cin >> x >> s;
		x++;
		s.erase(s.begin() + x, s.end());
		temp = stoi(s);
		while (temp > 0)
		{
			int digit = temp % 10;
			temp /= 10;
			k.push_back(digit);
		}
		for (int j = 0; j < s.size(); j++)
		{
			if (s[j] != '0')
			{
				break;
			}
			k.push_back(0);
		}
		reverse(k.begin(), k.end());
		temp = 0;
		for (int j = 1; j <= k.size(); j++)
		{
			count += k[j-1];
			while (j > count)
			{
				temp++;
				count++;
			}
		}
		cout << "Case #" << i << ": " << temp << endl;
		count = 0;
		k.clear();
	}
	return 0;
}