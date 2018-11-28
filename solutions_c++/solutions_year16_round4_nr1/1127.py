/*************************************************************\
~*********************ENJOY THE SILENCE***********************~
\*************************************************************/

#include <bits/stdc++.h>
using namespace std;

/*******************Debugging defines*************************/

#define ok_dump() cerr<<"OK\n"
#define var_dump(x) cerr<<#x": "<<x<<'\n'
#define arr_dump(x, n) {cerr<<#x"[]: ";\
	for(int _=1;_<=n;++_) cerr<<x[_]<<" ";cerr<<'\n';}

/*************************************************************/

map<string, string> Sol;

void Gen(string S, int n) {
	if(n >= 15) return;

	string sorted = S;
	sort(sorted.begin(), sorted.end());
	Sol[sorted] = S;

	string nws;
	for(auto c : S) {
		string nw;

		if(c == 'P') nw = "RP";
		if(c == 'S') nw = "PS";
		if(c == 'R') nw = "RS";
		
		nws += nw;
	}

	cerr << nws << "->";
	for(int i = 1; i <= n + 1; ++i) {
		for(int j = 0; j < nws.size(); j += (1 << i)) {
			int len = (1 << (i - 1)), 
				p1 = j,
				p2 = j + len; 

			bool greater = 0;
			for(int p = 0; p < len; ++p) {
				if(nws[p1 + p] > nws[p2 + p]) {
					greater = 1;
					break;
				}
			}

			if(greater) {
				for(int p = 0; p < len; ++p)
					swap(nws[p1 + p], nws[p2 + p]);
			}
		}
	}
	cerr << nws << '\n';

	Gen(nws, n + 1);
}

int main() {	
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	
	Gen("R", 0);
	Gen("P", 0);
	Gen("S", 0);

	int t;
	cin >> t;

	for(int tt = 1; tt <= t; ++tt) {
		int n, a, b, c;
		cin >> n >> a >> b >> c;

		string str = "";
		while(a--) str += "R";
		while(b--) str += "P";
		while(c--) str += "S";
		sort(str.begin(), str.end());

		cout << "Case #" << tt << ": ";
		if(Sol.find(str) != Sol.end()) {
			cout << Sol[str] << '\n';
		} else {
			cout << "IMPOSSIBLE\n";
		}

	}	

	for(auto p : Sol) cerr << p.second << '\n';
	
	return 0;
}

/*************************************************************\
~*********************ENJOY THE SILENCE***********************~
\*************************************************************/


