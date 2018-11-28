#include <bits/stdc++.h>
using namespace std;
int main() {
	int t;
	cin >> t;
	int run;
	for(run = 1; run <= t; run++) {
		string str;
		cin >> str;
		string revString, ans;
		char firstChar;
		revString.push_back(str[0]);
		firstChar = str[0];
		int i;
		for(i = 1; i < str.size(); i++) {
			char ch = firstChar;
			if(ch <= str[i]) {
				revString.push_back(str[i]);
				firstChar = str[i];
			} else {
				ans.push_back(str[i]);
			}
		}
		reverse(revString.begin(), revString.end());
		cout << "Case #" << run << ": " << revString << ans << endl;
	}
	return 0;
}