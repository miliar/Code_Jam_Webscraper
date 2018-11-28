#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define mp make_pair
#define pb push_back

#define MOD 1000000007LL

int main(){
	int t;
	cin >> t;
	for (int tt = 1; tt <= t; tt++){
		string s;
		cin >> s;
		while (s.back() == '+') s.pop_back();

		string ss;
		for (char c : s){
			if (ss.size() == 0) ss.pb(c);
			else if (c != ss.back()) ss.pb(c);
		}

		cout << "Case #" << tt << ": "<<ss.size() <<endl;
	}
	return 0;
}