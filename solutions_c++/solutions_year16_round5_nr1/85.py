#include <bits/stdc++.h>
using namespace std;

int TC;
string S;

string reduce(string S) {
	if (S == "") return "";
	vector<int> v, v1;
	v.push_back(-1);
		
		for (int i = 0; i < S.length() - 1; i++) {
			if (S[i] != S[i + 1]) v.push_back(i);
		}
		v.push_back(S.length() - 1);
		for (int i = 0; i < v.size() - 1; i++) v1.push_back((v[i + 1] -v[i]) % 2);
		string news = "";
		for (int i = 0; i < v1.size(); i++) {
			if (v1[i] == 1) {
				if (i % 2 == 0) news += "C";
				else news += "J";
			}
		}
		return news;
}

int main() {
	scanf("%d", &TC);
	for (int tc = 1; tc <= TC; tc++) {
		
		cin >> S;
		int oriscore = S.length() * 5;
		string prev = S;
		S = reduce(S);
		while (prev != S) {
			prev = S;
			S = reduce(S);
		}
		printf("Case #%d: %d\n", tc, oriscore - 5 * (S.length() / 2));
	}
}
