#include <vector>
#include <map>
#include <cstring>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <sstream>
#include <complex>
#include <queue>
#include <stack>
#include <map>
#include <bitset>
#include <iomanip>
#include <set>
#include <stack>
#include <stdio.h>
#include <string>

using namespace std;

#define bigint pair<long long, long long>
#define ll long long
#define vll vector<long long>
#define EP 100000000
#define STP 10000000000000000

bigint mulbig(ll a, ll b)
{
	bigint ret;
	ll a1, a2, b1, b2;
	a1 = a / EP;
	a2 = a % EP;
	b1 = b / EP;
	b2 = b % EP;
	ret.first = a1 * b1 + (a1 * b2 + a2 * b1 + a2 * b2 / EP) / EP;
	ret.second = ((a1 * b2 + a2 * b1) % EP * EP + a2 * b2) % STP;
	return ret;
}

bigint powbig(int a, int n)
{
	bigint ret;
	int l = 16 / log10(double(a));
	if(n < l)
	{
		ret.first = 0;
		ret.second = pow(double(a), n);
	}
	else
	{
		ret = mulbig(pow(double(a), n - l), pow(double(a), l));
	}
	return ret;
}

bigint sumbig(bigint a, bigint b)
{
	bigint ret;
	ret.first = a.first + b.first + (a.second + b.second) / STP;
	ret.second = (a.second + b.second) % STP;
	return ret;
}

string tentotwo(ll a)
{
	if(a == 0) return "0";
	string ret = "";
	while(a > 0)
	{
		if(a % 2 == 0)
			ret.insert(ret.begin(), '0');
		else
			ret.insert(ret.begin(), '1');
		a /= 2;
	}
	return ret;
}

bigint twototen(string s, int b)
{
	bigint ret;
	for(int i = 0; i < s.length(); ++i)
	{
		if(s[i] == '1')
			ret = sumbig(ret, powbig(b, s.length() - 1 - i));
	}
	return ret;
}

void printbig(bigint a)
{
	string a1, a2;
	a1 = to_string(a.first);
	a2 = to_string(a.second);
	if(a1 == "0")
		cout << a2;
	else
	{
		while(a2.length() < 16)
			a2.insert(a2.begin(), '0');
		cout << a1 << a2;
	}
}

ll prime(bigint a)
{
	if(a.second % 2 == 0)
		return 2;
	if(a.first == 0)
	{
		for(int i = 3; i <= sqrt(double(a.second)); i += 2)
			if(a.second % i == 0)
				return i;
		return 1;
	}
	else
	{
		for(int i = 3; i <= sqrt(double(a.first + 1)) * EP; i += 2)
			if(a.second % i == 0)
				return i;
		return 1;
	}
}

vll check(string s)
{
	vll ret;
	ll t;
	for(int i = 2; i <= 10; ++i)
	{
		t = prime(twototen(s, i));
		if(t == 1)
		{
			ret.clear();
			return ret;
		}
		else
			ret.push_back(t);
	}
	return ret;
}

int main()
{
	/*freopen("C-small-attempt0.in", "r", stdin);
	freopen("outC1.out", "w", stdout);*/

	int T;
	cin >> T;

	for(int i = 1; i <= T; ++i)
	{
		int N, J;
		cin >> N >> J;
		cout << "Case #" << i << ":\n";

		int j = 1;
		while(J > 0)
		{
			string s = tentotwo(pow(2.0, N - 1) + j);
			vll v = check(s);

			if(v.size() > 0)
			{
				cout << s;
				for(int k = 2; k <= 10; ++k)
					cout << " " << v[k - 2];
				cout << endl;
				--J;
			}
			j += 2;
		}
	}

	return 0;
}