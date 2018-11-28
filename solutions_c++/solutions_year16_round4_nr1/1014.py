#include <iostream>
#include <string>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <vector>
#include <set>
#include <map>
#include <cstring>
#include <algorithm>
#include <queue>
using namespace std;

class C
{
public:
	int r, p, s;
	C()
	{
		r = p = s = 0;
	}
};

C get_count(char c, int n)
{
	C res;
	char c2;
	if (c == 'r')
	{
		res.r++;
		c2 = 's';
	}
	else if (c == 's')
	{
		res.s++;
		c2 = 'p';
	}
	else
	{
		res.p++;
		c2 = 'r';
	}

	if (n > 0)
	{
		C left = get_count(c, n - 1);
		C right = get_count(c2, n - 1);
		res.r = left.r + right.r;
		res.s = left.s + right.s;
		res.p = left.p + right.p;
	}

	return res;
}

string mat[3][14];

int get_index(char c)
{
	if (c == 'R') return 0;
	else if (c == 'P') return 1;
	else return 2;
}

string get_res(char c, int n)
{
	string res = mat[get_index(c)][n];
	if (res != "") return res;

	if (n == 0)
	{
		res += c;
	}
	else
	{
		char c2;
		
		if (c == 'R') c2 = 'S';
		else if (c == 'S') c2 = 'P';
		else c2 = 'R';

		string left = get_res(c, n - 1);
		string right = get_res(c2, n - 1);

		if (left < right) res = left + right;
		else res = right + left;
	}

	mat[get_index(c)][n] = res;
	return res;
}


int main()
{
#if !ONLINE_JUDGE
	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);
#endif

	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);


	for (int i = 0; i < 3; i++)
	{
		for (int j = 0; j < 14; j++)
			mat[i][j] = "";
	}

	char arr[] = { 'R', 'P', 'S' };
	for (int i = 0; i < 3; i++)
	{
		for (int j = 0; j < 14; j++)
		{
			string x = get_res(arr[i], j);
			//cout << x << endl;
		}
	}
	int t;
	cin >> t;
	for (int z = 1; z <= t; z++)
	{
		int n, r, p, s;
		cin >> n >> r >> p >> s;
		
		cout << "Case #" << z << ": ";
		C cnt = get_count('r', n);
		
		if (cnt.r == r && cnt.p == p && cnt.s == s)
		{
			cout << get_res('R', n) << endl;
			continue;
		}
		cnt = get_count('p', n);
		if (cnt.r == r && cnt.p == p && cnt.s == s)
		{
			cout << get_res('P', n) << endl;
			continue;
		}
		
		cnt = get_count('s', n);
		if (cnt.r == r && cnt.p == p && cnt.s == s)
		{
			cout << get_res('S', n) << endl;
			continue;
		}
		cout << "IMPOSSIBLE" << endl;
	}

	return 0;
}