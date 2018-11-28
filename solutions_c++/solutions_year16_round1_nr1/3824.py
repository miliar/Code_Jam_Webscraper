#include <bits/stdc++.h>
using namespace std;

bool myfunc(char a, char b) {
	return a > b;
}

int main() {
	ifstream fin("A-large.in",ios::in);
	ofstream fout("A-large.out",ios::out);
	list<char> CharList;
	char S[1010], SF[1010];
	int t;
	fin >> t;
	for (int i = 0; i < t; i++) {
		fin >> S;
		fout << "Case #" << i + 1 << ": ";
		int len = strlen(S);
		CharList.push_front(S[0]);
		for (int j = 1; j < len; j++) {
			if (S[j] >= CharList.back())
				CharList.push_back(S[j]);
			else
				CharList.push_front(S[j]);
		}
		//strcpy(SF, S);
		//	sort(SF, S + strlen(SF), myfunc);
		while (!CharList.empty()) {
			fout << CharList.back();
			CharList.pop_back();
		}
		fout << endl;
	}
}
