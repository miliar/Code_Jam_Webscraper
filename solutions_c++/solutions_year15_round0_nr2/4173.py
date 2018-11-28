#include <iostream>
#include <stdio.h>
#include <stack>
#include <queue>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;
int main()
{
	freopen("src.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int tt, d;
	cin >> tt;
	for (int t = 1; t <= tt; t++)
	{
		vector<int>v;
		cin >> d;
		v.resize(d);
		int emp = 0;
		int pnk = 0;
		int mx = -1;
		for (int i = 0; i < d; i++)
		{
			cin >> v[i];
			pnk += v[i];
			mx = max(mx, v[i]);
		}
		int cnt = 0;
		while (pnk)
		{

			if (v.size() > 1)
			{
				vector<int>v2;
				for (int i = 0; i < v.size(); i++)
				{
					if (v[i])
						v2.push_back(v[i]);
				}
				v = v2;
			}
			/*sort(v.begin(), v.end());
			for (int i = 0; i < v.size(); i++)
				cout << v[i] << " ";
				
			cout << endl;*/
			int idx = -1;
			for (int i = 0; i < v.size(); i++)
				if (idx == -1 || v[i] > v[idx])
					idx = i;
			int _big = 0;
			int num = 2;
			for (int i = 2; i < v[idx]; i++)
			{
				if (v[idx] % i == 0)
				{
					num = i;
					break;
				}
			}
			for (int i = 0; i < v.size(); i++)
				if (v[i] >(v[idx]) / num)
					_big++;
			if (_big >= (v[idx] + 1) / num || v[idx] == 1)
			{
				for (int i = 0; i < v.size(); i++)
				{
					if (v[i])
					{
						v[i]--;
						pnk--;
					}
				}
			}
			else
			{
				v.push_back(v[idx] / num);
				v[idx] -= v.back();
			}
			cnt++;
		}
		cout << "Case #" << t << ": " << min(cnt, cnt) << endl;
	}
	return 0;
}