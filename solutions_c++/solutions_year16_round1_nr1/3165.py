#include <bits/stdc++.h>
using namespace std;

int L;
string S;

int main() {
	ios_base::sync_with_stdio(false); cin.tie(0);
	int T; cin >> T;
	for(int cs = 1; cs <= T; cs++) {
		cin >> S; L = S.size();
		string rs = string(1, S[0]);
		for(int i = 1; i < int(S.size()); i++) {
			if(S[i] >= rs[0]) rs = string(1, S[i]) + rs;
			else rs += string(1, S[i]);
		}
		cout << "Case #" << cs << ": " << rs << "\n";
	}
}
