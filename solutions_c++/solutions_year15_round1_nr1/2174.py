#include<iostream>
#include<algorithm>
#include<cmath>
#include<string>
#include<vector>
#include<cstring>
using namespace std;
#pragma warning (disable : 4996)
typedef long long ll;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t, bk;
	cin >> t;
	for (bk = 1; bk <= t; bk++)
	{
		cout << "Case #" << bk << ": ";
		ll n, i, j, k, temp, ans1 = 0, ans2 = 0;
		vector<ll> v;
		cin >> n;
		for (i = 0; i < n; i++)
		{
			cin >> temp;
			v.push_back(temp);
		}
		
		for (i = 0; i < v.size() - 1; i++)
		{
			if (v[i]>v[i + 1])
				ans1 += v[i] - v[i + 1];
		}
		temp = v[0] - v[1];
		for (i = 1; i < v.size() - 1; i++)
		{
			//cout << temp << endl;
			//cout << "it:" << v[i] - v[i + 1] << endl;
			temp = max(temp, v[i] - v[i + 1]);
				//cout << temp << endl << endl;
		}
		//cout << "max:" << temp << endl;
		for (i = 0; i < v.size() - 1; i++)
		{
			if (v[i] < temp)
				ans2 += v[i];
			else
				ans2 += temp;
		}
		cout << ans1 << " ";
		cout << ans2;
		cout << endl;
	}
	return 0;
}