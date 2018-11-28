#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<string>
using namespace std;
int T, n, r, p, s;
string ans;

string calc(int w, int n, int &r, int &p, int &s)
{
	if (n == 0)
	{
		r = (w == 0), p = (w == 1), s = (w == 2);
		return w == 0 ? "R" : (w == 1 ? "P" : "S");
	}
	int x, y, z;
	string a = calc(w, n - 1, r, p, s);
	string b = calc((w + 2) % 3, n - 1, x, y, z);
	r += x, p += y, s += z;
	if (a < b) return a + b; else return b + a;
}

void solve(string str, int x, int y, int z)
{
	if (x == r && y == p && z == s)
	{
		if (ans == "" || ans > str) ans = str;
	}
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	cin >> T;
	for (int C = 1; C <= T; C++)
	{
		cin >> n >> r >> p >> s;
		int x, y, z;
		ans = "";
		string str = calc(0, n, x, y, z);
		solve(str, x, y, z);
		str = calc(1, n, x, y, z);
		solve(str, x, y, z);
		str = calc(2, n, x, y, z);
		solve(str, x, y, z);
		cout << "Case #" << C << ": ";
		if (ans == "") ans = "IMPOSSIBLE";
		cout << ans << endl;
	}
}