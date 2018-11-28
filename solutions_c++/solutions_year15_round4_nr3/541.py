#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int solve() {
	int n;
	cin >> n;
	
	vector<vector<string>> v(n);

	string s;
	getline(cin, s);
	for(int i=0; i < n; i++) {
		getline(cin, s);
		//cout << s << endl;
		istringstream iss(s);
	    do
	    {
	        string sub;
	        iss >> sub;
	        if(sub != "")
	        	v[i].push_back(sub);
	    } while (iss);
	}
	
	/*for(int i=0; i < n; i++) {
		for(auto s: v[i]) cout << "*" << s << "* "; cout << endl;
	}*/

	set<string> F,E,S;
	for(auto s: v[0]) F.insert(s);
	for(auto s: v[1]) {
		if(F.find(s) != F.end()) S.insert(s);
		else E.insert(s);
	}
	int res = S.size();

	int result = 474747;
	if(n == 2) result = 0;
	for(int i=0; i < (1 << (n-2)); i++) {
		set<string> e,f;
		for(int j=2; j < n; j++) {
			if(i & (1 << (j-2))) {
				for(auto s: v[j]) e.insert(s);
			}
			else {
				for(auto s: v[j]) f.insert(s);
			}
		}
		int akt = 0;

		for(auto s: e) {
			if(S.find(s) != S.end() || E.find(s) != E.end()) continue;
			if(f.find(s) != f.end() || F.find(s) != F.end()) akt++;
		}
		for(auto s: f) {
			if(E.find(s) != E.end()) akt++;
		}
		//cout << i << " " << akt << endl;
		result = min(akt, result);
	}
	cout << result + res << endl;
}

int main(void) {
	ios::sync_with_stdio(false);

	int T;
	cin >> T;
	for(int t=1; t <= T; t++) {
		cout << "Case #"<< t << ": "; 
		solve();
	}
	return 0;
}