#include <bits/stdc++.h>

using namespace std;

int main (int argc, char const *argv[]) {
	//freopen("input.txt", "r", stdin);
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);	

	int T, cs = 0; string S; deque <char> D;
	scanf("%d", &T); while (T--) {
		cin >> S; D.clear();
		D.push_back(S[0]);
		for (int i = 1; i < S.size(); i++) {
			char a = D.front(), b = D.back();
			if (S[i] >= a) D.push_front(S[i]);
			else D.push_back(S[i]);
		}
		string R = "";
		for (int i = 0; i < S.size(); i++) R += D[i];
		printf("Case #%d: ", ++cs);
		cout << R << endl;
	}
	return 0;
}

