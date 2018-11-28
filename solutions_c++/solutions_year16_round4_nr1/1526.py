#define _USE_MATH_DEFINES

#include <iostream>
#include <sstream>
#include <cmath>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <algorithm>

using namespace std;

typedef vector<int> VI;

typedef long long ll;

#define FOR(x, b, e) for (int x = b; x <= (e); ++x)
#define FORR(x, b, e) for (int x = b; x >= (e); --x)
#define REP(x, n) for(int x = 0; x < (n); ++x)
#define REPR(x, n) for(int x = (n - 1); x >= 0; --x)

const int INF = 1000000001;
typedef vector<ll> vll;

stringstream out;

int norm(int n) { return n < INF ? n : INF; }
//---------------------------------------------------------------

string change(string a, char b, char c)
{
	for (int i = 0; i < a.length(); i++)
	{
		if (a[i] == b)
			a[i] = c;
	}
	return a;
}

void function()
{
	int n, r, p, s;
	cin >> n >> r >> p >> s;
	int total = r + p + s;
	int t1 = 0, t2 = 0, t3 = 0;
	int temp1, temp2, temp3;
	string res = "A";
	string temp;
	t1 = 1;
	FOR(i, 1, n) {
		temp1 = t1;
		temp2 = t2;
		temp3 = t3;
		t1 += temp3;
		t2 += temp1;
		t3 += temp2;
		temp = "";
		for (int i = 0; i < res.length(); i++)
		{
			if (res[i] == 'B')
				temp += "BC";
			if (res[i] == 'C')
				temp += "CA";
			if (res[i] == 'A')
				temp += "AB";
		}
		res = temp;
	}

	if ((t1 == p && t2 == r && t3 == s))
	{
		temp = change(temp, 'A', 'P');
		temp = change(temp, 'B', 'R');
		temp = change(temp, 'C', 'S');
	}
	else if ((t1 == p && t2 == s && t3 == r))
	{
		temp = change(temp, 'A', 'P');
		temp = change(temp, 'B', 'S');
		temp = change(temp, 'C', 'R');
	}
	else if ((t1 == r && t2 == p && t3 == s))
	{
		temp = change(temp, 'A', 'R');
		temp = change(temp, 'B', 'P');
		temp = change(temp, 'C', 'S');
	}
	else if ((t1 == r && t2 == s && t3 == p))
	{
		temp = change(temp, 'A', 'R');
		temp = change(temp, 'B', 'S');
		temp = change(temp, 'C', 'P');
	}
	else if ((t1 == s && t2 == p && t3 == r))
	{
		temp = change(temp, 'A', 'S');
		temp = change(temp, 'B', 'P');
		temp = change(temp, 'C', 'R');
	}
	else if ((t1 == s && t2 == r && t3 == p))
	{
		temp = change(temp, 'A', 'S');
		temp = change(temp, 'B', 'R');
		temp = change(temp, 'C', 'P');
	}
	else 
	{
		out << "IMPOSSIBLE\n";
		return;
	}

	for (int i = 1; i < n; i++)
	{
		int power = pow(2, i);
		for (int j = 0; j < total; j += power)
		{
			string a = temp.substr(j, power / 2);
			string b = temp.substr(j + power / 2, power / 2);
			if (b < a) {
				temp.replace(j, power / 2, b);
				temp.replace(j + power / 2, power / 2, a);
			}
		}
	}

	out << temp << endl;
}

//---------------------------------------------------------------
int main()
{
	ios_base::sync_with_stdio(0);
	int t;
	cin >> t;
	FOR(i, 1, t)
	{
		out << "Case #" << i << ": ";
		function();
	}
	cout << out.str();
	return 0;
}