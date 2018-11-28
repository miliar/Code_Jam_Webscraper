#include <bits/stdc++.h>
using namespace std;

int main() {
	short k;
	short c;
	
	scanf("%hi", &k);
	c = k;
	
	while (k--) {
		char s[2001] = "";
		string S = "";
		multiset<short> ms;

		scanf("%s", s);
		S = s;

		while (S.find("Z") != string::npos) {
			S.erase(S.begin() + S.find("Z"));
			S.erase(S.begin() + S.find("E"));
			S.erase(S.begin() + S.find("R"));
			S.erase(S.begin() + S.find("O"));
			ms.insert(0);
		}

		while (S.find("W") != string::npos) {
			S.erase(S.begin() + S.find("T"));
			S.erase(S.begin() + S.find("W"));
			S.erase(S.begin() + S.find("O"));
			ms.insert(2);
		}

		while (S.find("U") != string::npos) {
			S.erase(S.begin() + S.find("F"));
			S.erase(S.begin() + S.find("O"));
			S.erase(S.begin() + S.find("U"));
			S.erase(S.begin() + S.find("R"));
			ms.insert(4);
		}

		while (S.find("O") != string::npos) {
			S.erase(S.begin() + S.find("O"));
			S.erase(S.begin() + S.find("N"));
			S.erase(S.begin() + S.find("E"));
			ms.insert(1);
		}

		while (S.find("R") != string::npos) {
			S.erase(S.begin() + S.find("T"));
			S.erase(S.begin() + S.find("H"));
			S.erase(S.begin() + S.find("R"));
			S.erase(S.begin() + S.find("E"));
			S.erase(S.begin() + S.find("E"));
			ms.insert(3);
		}

		while (S.find("F") != string::npos) {
			S.erase(S.begin() + S.find("F"));
			S.erase(S.begin() + S.find("I"));
			S.erase(S.begin() + S.find("V"));
			S.erase(S.begin() + S.find("E"));
			ms.insert(5);
		}

		while (S.find("X") != string::npos) {
			S.erase(S.begin() + S.find("S"));
			S.erase(S.begin() + S.find("I"));
			S.erase(S.begin() + S.find("X"));
			ms.insert(6);
		}

		while (S.find("S") != string::npos) {
			S.erase(S.begin() + S.find("S"));
			S.erase(S.begin() + S.find("E"));
			S.erase(S.begin() + S.find("V"));
			S.erase(S.begin() + S.find("E"));
			S.erase(S.begin() + S.find("N"));
			ms.insert(7);
		}

		while (S.find("G") != string::npos) {
			S.erase(S.begin() + S.find("E"));
			S.erase(S.begin() + S.find("I"));
			S.erase(S.begin() + S.find("G"));
			S.erase(S.begin() + S.find("H"));
			S.erase(S.begin() + S.find("T"));
			ms.insert(8);
		}

		while (S.find("N") != string::npos) {
			S.erase(S.begin() + S.find("N"));
			S.erase(S.begin() + S.find("I"));
			S.erase(S.begin() + S.find("N"));
			S.erase(S.begin() + S.find("E"));
			ms.insert(9);
		}

		printf("Case #%hi: ", c-k);
		for (std::multiset<short>::const_iterator i(ms.begin()), end(ms.end()); i != end; ++i)
			printf("%hi", *i);
		printf("\n");
	}
	
	return 0;
}
