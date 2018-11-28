#include <bits/stdc++.h>

using namespace std;

void debug(string msg) {
	#ifdef DEBUG_ON
	cerr << msg;
	#endif
}

int main(int argc, char *argv[])
{
	int T;
	cin >> T;

	for(int t = 1; t <= T; t++) {
		string S;
		cin >> S;

		string res;
		res.push_back(S[0]);
		for(unsigned i = 1; i < S.length(); i++) {
			if(S[i] < res[0]) res += S[i];
			else res = S[i] + res;
		}

		cout << "Case #" << t << ": " << res << "\n";
	}

	return 0;
}
