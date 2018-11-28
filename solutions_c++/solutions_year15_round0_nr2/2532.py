#include<bits/stdc++.h>
using namespace std;
int main()
{
	int i, j, k, t, n, m, x;
	cin >> t;
	for (x = 1; x <= t; ++x)
	{
		vector<int> v;
		cin >> n;
		for (i = 0; i < n; ++i)
		{
			cin >> j;
			v.push_back(j);
		}
		int high = 1000, low = 1;
		int curr_ans;
		while (high>low)
		{
			priority_queue<int> q;
			int mid = (high + low) / 2;
			int tmp = 0;
			int tmp_mid = mid;
			for (i = 0; i < n; ++i)
			{
				q.push(v[i]);
			}
			while (q.top()>tmp_mid && tmp_mid >= 1)
			{
				int e_tmp = q.top();
				q.pop();
				if (e_tmp % 2 == 0)
					q.push(e_tmp / 2);
				else
					q.push((e_tmp / 2) + 1);
				q.push(e_tmp / 2);
				--tmp_mid;
			}
			if (tmp_mid >= 1)
			{
				curr_ans = mid;
				high = mid;
			}
			else
				low = mid + 1;
		}
		high = 1000, low = 1;
		int curr_ans1;
		while (high>low)
		{
			priority_queue<int> q;
			int mid = (high + low) / 2;
			int tmp = 0;
			int tmp_mid = mid;
			for (i = 0; i < n; ++i)
			{
				q.push(v[i]);
			}
			while (q.top()>tmp_mid && tmp_mid >= 1)
			{
				int e_tmp = q.top();
				q.pop();
				if (e_tmp == 9)
				{
					q.push(3);
					q.push(6);
				}
				else
				{
					if (e_tmp % 2 == 0)
						q.push(e_tmp / 2);
					else
						q.push((e_tmp / 2) + 1);
					q.push(e_tmp / 2);
				}
				--tmp_mid;
			}
			if (tmp_mid >= 1)
			{
				curr_ans1 = mid;
				high = mid;
			}
			else
				low = mid + 1;
		}
		//print ans
		cout << "Case #" << x << ": " << min(curr_ans,curr_ans1) << endl;
	}
}