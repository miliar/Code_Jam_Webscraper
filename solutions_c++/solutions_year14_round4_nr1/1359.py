#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int calc(const vector<int> &s, int x)
{
	int ans = 0;
	vector<bool> use(s.size());
	for (int i=s.size()-1;i>=0;i--)
	{
		if (use[i])
			continue;
		use[i] = true;
		int pos = -1;
		for (int j=i-1;j>=0;j--)
			if (!use[j] && s[j]<=x-s[i])
			{
				pos = j;
				break;
			}
		if (pos!=-1)
			use[pos] = true;
		ans++;
	}
	return ans;
}

int main()
{
	int t;
	cin >> t;
	for (int i=1;i<=t;i++)
	{
		int n, x;
		int tmp;
		vector<int> s;
		cin >> n >> x;
		for (int j=0;j<n;j++)
		{
			cin >> tmp;
			s.push_back(tmp);
		}
		sort(s.begin(), s.end(), less<int>());
		cout << "Case #" << i << ": " << calc(s, x) << endl;
	}
	return 0;
}
