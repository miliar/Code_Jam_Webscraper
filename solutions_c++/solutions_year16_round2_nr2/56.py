#include<bits/stdc++.h>
using namespace std;
typedef long long LL;

LL trans(string s) {
	istringstream is(s);
	LL k;
	is >> k;
	return k;
}

vector<string> solve(string s, string t) {
	vector<string> best;
	LL diff = 1000;
	diff = diff * diff * diff;
	diff *= diff;
	best.push_back("Z"); best.push_back("Z");
	int n = s.size();
	for(int mid=0; mid<n; mid++) {
		string ns = s, nt = t;
		bool ok = true;
		for(int i=0; i<mid; i++) {
			if(s[i] == '?' && t[i] == '?') {
				ns[i] = '0';
				nt[i] = '0';
				continue;
			}
			if(s[i] == '?') {
				ns[i] = nt[i];
				continue;
			}
			if(t[i] == '?') {
				nt[i] = ns[i];
				continue;
			}
			if(s[i] != t[i]) ok = false;
		}
		if(!ok) continue;
		
		for(int k=0; k<3; k++) {
		
			string nns = ns, nnt = nt;
			if(s[mid] == '?' && t[mid] == '?') {
				if(k == 0) {
					nns[mid] = '0';
					nnt[mid] = '1';
				}
				if(k == 1) {
					nns[mid] = '1';
					nnt[mid] = '0';
				}
				if(k == 2) {
					nns[mid] = '0';
					nnt[mid] = '0';
				}
			}
			else if(s[mid] == '?') {
				nns[mid] = nnt[mid]  + k - 1;
				if(nns[mid]<'0' || nns[mid]>'9') continue;
			}
			else if(t[mid] == '?') {
				nnt[mid] = nns[mid]  + k - 1;
				if(nnt[mid]<'0' || nnt[mid]>'9') continue;
			}
			for(int i=mid+1; i<n; i++) {
				if(t[i]=='?') {
					if(nns < nnt) nnt[i] = '0';
					else nnt[i] = '9';
				}
				if(s[i]=='?') {
					if(nns<nnt) nns[i]='9';
					else nns[i] = '0';
				}
			}
			
			LL a = trans(nns), b = trans(nnt);
			if(abs(b-a) < diff) {
				diff = abs(b-a);
				best[0] = nns;
				best[1] = nnt;
			}
			if(abs(b-a) == diff) {
				vector<string> tmp;
				tmp.push_back(nns);
				tmp.push_back(nnt);
				best = min(tmp, best);
			}
		}
	}
	return best;
	
}

int main() {
	int N;
	cin >> N;
	for(int i=0; i<N;i ++) {
		
		string s,t;
		cin >> s >> t;
		vector<string> ans = solve(s, t);
		cout << "Case #" << i+1 << ": " << (ans[0] + " " + ans[1]) << endl;
		
	}
	
	return 0;
	
}

