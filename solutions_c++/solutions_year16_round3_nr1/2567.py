#include <bits/stdc++.h>
using namespace std;

struct compare_pair
{
	bool operator()(const pair<int, char>& a, const pair<int, char>& b) const
	{
		return a.first < b.first;
	}
};

priority_queue<pair<int, char>, vector<pair<int, char>>, compare_pair> myQueue;

int main()
{
	int t, n, p, sum;
	string ans;
	cin >> t;
	for (int z=1; z<=t; ++z)
	{
		sum = 0;
		ans.clear();
		cin >> n;
		for (int j=0; j<n; ++j)
		{
			cin >> p;
			myQueue.push(make_pair(p, char('A' + j)));
			sum += p;
		}
		if (sum % 2 != 0)
		{
			const pair<int, char> top1 = myQueue.top();
			// cout << top1.first << " " << top1.second << endl;
			ans.push_back(top1.second);
			ans.append(" ");
			// cout << ans << endl;
			myQueue.pop();
			if (top1.first-1 > 0)
			{
				myQueue.push(make_pair(top1.first-1, top1.second));
			}
		}
		while (!myQueue.empty())
		{
			const pair<int, char> top1 = myQueue.top();
			// cout << top1.first << " " << top1.second << endl;
			ans.push_back(top1.second);
			// cout << ans << endl;
			myQueue.pop();
			if (top1.first-1 > 0)
			{
				myQueue.push(make_pair(top1.first-1, top1.second));
			}
			const pair<int, char> top2 = myQueue.top();
			// cout << top2.first << " " << top2.second << endl;
			ans.push_back(top2.second);
			ans.append(" ");
			// cout << ans << endl;
			myQueue.pop();
			if (top2.first-1 > 0)
			{
				myQueue.push(make_pair(top2.first-1, top2.second));
			}
		}
		
		ans.pop_back();
		
		cout << "Case #" << z << ": ";
		cout << ans;
		cout << endl;
	}
	return 0;
}
