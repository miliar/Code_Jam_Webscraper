#include <iostream>
#include <map>
#include <string>
#include <vector>
#include <math.h>
#include <algorithm>
#include <stdio.h>
#include <iomanip>
using namespace std;

int to_val(const vector<int> & plt, int val)
{
	int res = 0;
	for (vector<int>::const_iterator it = plt.begin(); it != plt.end(); ++it)
	{
		if (*it <= val) continue;
		if (*it > 2 * val) res += ((*it + val - 1)/val - 1);
		else ++res;
	}
	return res;
}

int main()
{
    ios_base::sync_with_stdio(false);
    int t;
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
    cin>>t;
	for (int j = 0; j < t; ++j)
	{
		int n;
		cin>>n;
		vector<int> plt(n);
		int max_p = 0;
		for (int i = 0; i < n; ++i)
		{
			cin>>plt[i];
			if (max_p < plt[i]) max_p = plt[i];
		}
		sort(plt.begin(), plt.end());		
		int res = max_p;
		for (int i = max_p - 1; i > 0; --i)
		{
			int t = i + to_val(plt, i);
			if (t < res) res = t;
		}
		cout<<"Case #"<<j + 1<<": "<<res<<endl;		
	}
    return 0;
}