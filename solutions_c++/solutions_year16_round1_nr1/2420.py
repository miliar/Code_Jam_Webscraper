#include <bits/stdc++.h>
using namespace std;

int main() {
	int T; cin >> T;
	for (int tt=1; tt<=T; tt++) {
		string S; cin >> S;
		list<char> curString;
		for (int i=0; i<S.size(); i++) {
			char f = curString.front();
			char b = curString.back();
			if (S[i] >= f) curString.push_front(S[i]);
			else curString.push_back(S[i]);
		}
		printf("Case #%d: ",tt);
		for (auto it=curString.begin(); it!=curString.end(); it++)
			cout << *it;
		cout << endl;
	}
	return 0;
}