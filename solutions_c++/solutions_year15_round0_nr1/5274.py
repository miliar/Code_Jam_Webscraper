//============================================================================
// Name        : Codejam15.cpp
// Author      : Mahmoud Saleh A. Gawad
// Version     :
// Copyright   : None.
// Description : Codejam'15 Qualification Round.
//============================================================================

#include <bits/stdc++.h>
using namespace std;

int main() {
	ifstream in("a.txt");
	ofstream out("a.out");

	int t;
	in>>t;
	for(int tt=1;tt<=t;tt++){
		int k;
		in>>k;
		string s;
		in>>s;
		int cnt = 0, ans = 0;
		for(int i=0;i<=k;i++){
			if(s[i]>'0'&&cnt<i){
				ans += (i-cnt);
				cnt += (i-cnt);
			}
			cnt += (s[i]-'0');
		}
		out << "Case #"<<tt<<": "<<ans<<endl;
	}

	return 0;
}
