#include <iostream>
#include <vector>
#include <list>
#include <set>
#include <string>
#include <cmath>
#include <climits>
#include <algorithm>

using namespace std;

bool all_true(vector<bool>& count)
{
	for (int i = 0; i < 10; ++i)
		if (!count[i])
			return false;
	return true;

}


int main()
{
	int t;
	cin >> t;
	for(int xt = 1; xt <= t; ++xt)
	{
		
		int n;
		cin >> n;
		cout << "Case #" << xt << ": ";
		if (n == 0)
			cout << "INSOMNIA" << endl;
		else
		{
			vector<bool> count(10, false);
			unsigned long long multiple = 1;
			int i = 1;
			while (!all_true(count))
			{
				multiple = i*n;
				string s = to_string(multiple);
				for (auto x : s)
					count[x - '0'] = true;
				++i;
			}
			cout << multiple << endl;
		}
	}
}