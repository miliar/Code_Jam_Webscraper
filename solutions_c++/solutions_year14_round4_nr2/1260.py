#include <iostream>
#include <vector>
#include <algorithm>
#define N 1000
using namespace std;

bool check(const vector<int> &a)
{
	int n = a.size();
	int pos = 0;
	for (int i=1;i<n;i++)
		if (a[i]>a[pos])
			pos = i;
	for (int j=0;j<pos;j++)
		if (!(a[j]<a[j+1]))
			return false;
	for (int j=n-1;j>pos;j--)
		if (!(a[j-1]>a[j]))
			return false;
	return true;
}

int count_merge(vector<int> &a, int l, int r)
{
	static vector<int> tmp(N);
	if (r-l==1)
		return 0;
	int m = (l+r)/2;
	int ans = 0;
	ans += count_merge(a, l, m);
	ans += count_merge(a, m, r);
	int il = l, im = m;
	int tc = l;
	while (il<m && im<r)
	{
		if (a[il]<a[im])
			tmp[tc++] = a[il++];
		else
		{
			tmp[tc++] = a[im++];
			ans += m-il;
		}
	}
	while (il<m)
		tmp[tc++] = a[il++];
	while (im<r)
		tmp[tc++] = a[im++];
	for (int i=l;i<r;i++)
		a[i] = tmp[i];
	return ans;
}

int count(const vector<int> &a, const vector<int> &ori_a)
{
	int n = a.size();
	vector<int> tmp_a(n);
	for (int i=0;i<n;i++)
		for (int j=0;j<n;j++)
			if (a[i]==ori_a[j])
				tmp_a[i] = j;
	return count_merge(tmp_a, 0, n);
}

int main()
{
	int t;
	cin >> t;
	for (int i=1;i<=t;i++)
	{
		int n;
		int tmp;
		vector<int> a, ori_a;
		cin >> n;
		for (int j=0;j<n;j++)
		{
			cin >> tmp;
			a.push_back(tmp);
		}
		ori_a = a;
		sort(a.begin(), a.end(), less<int>());
		int ans = count(a, ori_a);
		while (next_permutation(a.begin(), a.end()))
			if (check(a))
				ans = min(ans, count(a, ori_a));
		cout << "Case #" << i << ": " << ans << endl;
	}
	return 0;
}
