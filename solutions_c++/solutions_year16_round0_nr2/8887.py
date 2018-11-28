#include <bits/stdc++.h>

using namespace std;

int n;
string s;

bool check() {
	for(int i = 0; i < n; ++i) {
		if(s[i] == '-')	return false;
	}
	return true;
}

void dorev(int ind) {
	string ans = s;

	for(int i = ind; i >= 0; --i) {
		ans[ind-i] = (s[i] == '-' ? '+' : '-');
	}

	s = ans;
}

int calc() {
	int ans = 0;
	while(!check()) {
		++ans;
		int rind = n-1;
		for(int i = n-1; i >= 0; --i) {
			if(s[i] == '-') {
				rind = i;
				break;
			}
		}

		if(s[0] == '+') {
			for(int i = 0; i < rind; ++i) {
				if(s[i] == '+')	s[i] = '-';
				else			break;
			}
		}
		else {
			dorev(rind);
		}

	}
	return ans;

}

int main(void) {

	ifstream fin;
	fin.open("B-large.in");

	ofstream fout;
	fout.open("outputLarge.out");

	int t;
	fin>>t;
	for(int tt = 1; tt <= t; ++tt) {
		fin>>s;
		n = s.size();
		int ans = calc();
		//printf("Case #%d: %d\n", tt, ans);
		fout<<"Case #"<<tt<<": "<<ans<<"\n";

	}

	return 0;

}