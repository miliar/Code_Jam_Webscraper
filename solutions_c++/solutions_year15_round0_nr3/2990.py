#if !ONLINE_JUDGE
#define _CRT_SECURE_NO_WARNINGS
#endif
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <utility>
#include <algorithm>
#include <cstring>
#include <cmath>
#include <stack>
using namespace std;

int table[4][4] = {
	{1,2,3,4},
	{2,-1,4,-3},
	{3,-4,-1,2},
	{4,3,-2,-1}
};
string str;
vector <int> tree;
bool solve();
int multi(int , int );
int search(int, int, int, int, int);
int main()
{
#if !ONLINE_JUDGE
	freopen("input.in", "r", stdin);
	freopen("output1.out", "w", stdout);
#endif
	
	int t;
	cin >> t;
	for (int z = 1; z <= t; z++)
	{
		int r;
		string str1;
		cin >> r >> r >> str1;
		str = "";
		for (int i = 0; i < r; i++) str += str1;
		int tsize = 0;
		while ((1 << tsize) < str.size()) tsize++;
		tsize = (1 << tsize);
		tree.resize(2 * tsize);
		for (int i = 0; i < tsize; i++)
		{
			if (i < str.length())
			{
				tree[i + tsize] = (str[i] == '1') ? 1 : str[i] - 'i'+2;
			}
			else tree[i + tsize] = 1;
		}

		for (int i = tsize - 1; i>0; i--)
		{
			tree[i] = multi(tree[i * 2], tree[i * 2 + 1]);
		}

		cout << "Case #" << z << ": ";
		if (solve())
		{
			cout << "YES" << endl;
		}
		else cout << "NO" << endl;

	}
	return 0;
}


int multi(int x, int y)
{
	int ans1 = table[abs(x) - 1][abs(y) - 1];
	int sign = 0;
	if (x < 0) sign++;
	if (y < 0) sign++;
	if (ans1 < 0) sign++;

	int ans = abs(ans1);

	if (sign % 2) return -ans;
	else return ans;
}

int search(int cur, int l, int r, int x, int y)
{
	if (l == x && r == y) return tree[cur];

	int mid = l + (r - l) / 2;

	if (x > mid) return search(cur * 2 + 1, mid + 1, r, x, y);
	else if (y <= mid) return search(cur * 2, l, mid, x, y);
	else
	{
		return multi(search(cur * 2, l, mid, x, mid),
			search(cur * 2 + 1, mid + 1, r, mid+1, y));
	}

}

bool solve()
{
	vector <int> iv, kv;
	int imul = 1;

	for (int i = 0; i < str.length() - 2; i++)
	{
		imul = multi(imul, ((str[i] == '1') ? 1 : str[i] - 'i' + 2));
		if (imul == 2) iv.push_back(i);
	}
	int kmul = 1;
	for (int i = str.length()-1; i>1; i--)
	{
		kmul = multi( ((str[i] == '1') ? 1 : str[i] - 'i' + 2),kmul);
		if (kmul == 4) kv.push_back(i);
	}


	for (int i = 0; i < iv.size(); i++)
	{
		for (int j = 0; j < kv.size() ; j++)
		{
			if (iv[i] + 1 >= kv[j]) break;
			if (search(1, 0, tree.size() / 2-1, iv[i] + 1, kv[j] - 1) == 3)
				return true;
		}
	}
	return false;
}