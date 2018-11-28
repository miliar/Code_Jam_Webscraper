#include <bits/stdc++.h>
using namespace std;
#define mp make_pair
#define pb push_back
typedef long long ll;
typedef pair<int,int> pii;
#define X first
#define Y second


string gen(char first, int depth)
{
	if (depth == 0) 
	{
		string r = "";
		r.pb(first);
		return r;
	}
	string l,r;
	if (first == 'R') 
	{
		l = gen('R', depth-1); 
		r = gen('S', depth - 1);
    }
	if (first == 'P') 
	{
		l = gen('P', depth-1); 
		r = gen('R', depth - 1);
    }
	if (first == 'S') 
	{
		l = gen('P', depth-1); 
		r = gen('S', depth - 1);
    }
	return min(l,r) + max(l,r);
}

void calc(string s, int &r, int &p, int &sc)
{
	r = p = sc = 0;
	for (int i = 0; i < (int)s.size(); i++)
	   if (s[i] == 'R') r++;
	   else if (s[i] == 'P') p++;
	   else if (s[i] == 'S') sc++;
}

void solve(int test)
{
	int n, r, p ,s;
	cin >> n >> r >> p >> s;
	string a = gen('R', n);
	string b = gen('P', n);
	string c = gen('S', n);
	//cout << a << ' ' << b << ' ' << c << endl;
	int ar,ap,as;
	calc(a, ar, ap, as);
	string answer = "IMPOSSIBLE";
	if (ar == r && ap == p && as == s)
	   answer = a;
	calc(b, ar, ap, as);
	if (ar == r && ap == p && as == s)
	   answer = b;
	calc(c, ar, ap, as);
	if (ar == r && ap == p && as == s)
	   answer = c;
	cout << "Case #" << test << ": " << answer << endl;
}

int main()
{
	int t;
	cin >> t;
	for (int i =0 ; i < t; i++) solve(i+1);
	return 0;
}
