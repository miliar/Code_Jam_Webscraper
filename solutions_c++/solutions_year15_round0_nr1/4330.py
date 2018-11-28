// ovation #codejam2015
#include <bits/stdc++.h>

#define pb push_back

using namespace std;

ifstream f("ovation.in");
ofstream g("ovation.out");

int n;
string s;
vector<int> A;

void solve() {
	A.resize(0);
	s.resize(0);
	
	f>>n>>s;
	for (unsigned i=0;i<s.size();i++) {
		int x = s[i]-'0';
		A.pb(x);
	}
	
	int people = 0;
	for (int i=1;i<(int)A.size();i++) {
		if (i > A[i-1]) {
			people += i-A[i-1];
			A[i] += i-A[i-1];
		}
		A[i] += A[i-1];
	}
	
	g<<people;
}

int main() {
	
	int t; f>>t;
	for (int i=1;i<=t;i++) {
		g<<"Case #"<<i<<": ";
		solve();
		g<<'\n';
	}
	
	f.close(); g.close();
	return 0;
}
