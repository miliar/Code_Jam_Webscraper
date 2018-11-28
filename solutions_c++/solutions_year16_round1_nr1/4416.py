#include <bits/stdc++.h>
using namespace std;
string solve(string);
int main() {
	int kases, kase=1;
	cin>>kases;
	while(kases--) {
		string s;
		cin >> s;
		cout << "Case #" << kase <<": " << solve(s) << endl;
		kase++;
	}
	return 0;
}

string solve1 (string s) {
	string res = s;
	char seq[s.size() * 2 + 2];
	int posL = s.size()-1;
	int posR = posL;
	seq[posL] = s[0];

	for(int i = 1 ; i < s.size() ; i++) {
		if (s[i] >= seq[posL]) {
			cout << s[i] << ">=" << seq[posL] << " -- L " << endl;
			posL --;
			seq[posL] = s[i];
		}
		else {
			cout << s[i] << "<" << seq[posL] << " -- R " << endl;
			posR++;
			seq[posR] = s[i];
		}
	}
	int j=0;
	for (int i = posL; i <= s.size() ; i++) {
		res[j++] = seq[i];
	}
	return res;
}

string solve (string s) {
	string res;
	char seq[s.size() * 2 + 2];
	int posL = s.size()-1;
	int posR = posL;
	res = res + s[0];
	//seq[posL] = s[0];
	string::iterator it = s.begin();
	for(int i = 1 ; i < s.size() ; i++) {
		if (s[i] >= res[0]) {
			//cout << s[i] << ">=" << res[0] << " -- L " << endl;
			//posL --;
			res.insert(0,1, s[i]);
			//seq[posL] = s[i];
		}
		else {
			//cout << s[i] << "<" << res[0] << " -- R " << endl;
			//posR++;
			res = res + s[i];
		}
	}
//	int j=0;
	//for (int i = posL; i <= s.size() ; i++) {
		//res[j++] = seq[i];
	//}
	return res;
}
