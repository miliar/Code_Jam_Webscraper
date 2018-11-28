#include <bits/stdc++.h>
using namespace std;
#define mp make_pair
#define pb push_back
typedef long long ll;
typedef pair<int,int> pii;
#define X first
#define Y second

map<string, int> d;

string norm(string s)
{
	string r = "";
	r.pb(s[0]);
	for (int i = 1; i < (int)s.size(); i++)
	   if (s[i] != r.back()) r.pb(s[i]);
	return r;
}

int get(string s)
{
//	cout << "get(" << s << ")" << endl;
	s = norm(s);
	bool ok = 1;
	for (int i = 0; i < (int)s.size(); i++) if (s[i] != '+') ok = 0;
//	if (ok) cout << "OK!!" << endl;
	if (ok) return 0;
	if (d.count(s) != 0) return d[s];
	d[s] = (int)1e9;
	int n = s.size();
	for (int i = 1; i <= n; i++)
	{
		string nw = s;
		reverse(nw.begin(), nw.begin() + i);
		for (int j = 0; j < i; j++)
		   if (nw[j] == '+') nw[j] = '-';
		   else nw[j] = '+';
		d[s] = min(d[s], get(nw) + 1);
	}
//	cout << "d[" << s << "] = " << d[s] << endl;
	return d[s];
}

void solve(int test)
{
	int k,c,s;
	cin >> k >> c >> s;
	cout << "Case #" << test << ": ";
	for (int i = 1; i <= s; i++) cout << i << " \n"[i==s];
}

int main()
{
	int t;
	cin >> t;
	for (int i = 1; i <= t; i++) solve(i);
	return 0;
}
