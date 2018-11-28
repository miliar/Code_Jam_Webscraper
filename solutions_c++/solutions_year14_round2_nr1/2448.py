#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
using namespace std;

int error = 0;
int Solve(string *S, int N) {
	int avg = 0;
	char T = S[0][0];
	for (int i = 0; i < N; i++) {
		avg += S[i].size();
		if (T != S[i][0]) {
			error = 1;
			break;
		}
	}
	avg /= N;
	int res = 0;
	for (int i = 0; i < N; i++) {
		res += abs((int)S[i].size() - avg);
	}
	return res;
}
string Cut(string S) {
	int i;
	for (i = 1; i < S.size(); i++) {
		if (S[0] != S[i]) break;
	}
	if (S == "") return "";
	return S.substr(i, S.size() - i);
}
string GetHead(string S) {
	int i;
	for (i = 1; i < S.size(); i++) {
		if (S[0] != S[i]) break;
	}
	return S.substr(0, i);
}
int main() {
	ifstream fin;
	ofstream fout;
	fin.open("A-small-attempt3.in");
	fout.open("A-small-attempt3.out");

	int TestCase;
	fin >> TestCase;
	for (int Test = 1; Test <= TestCase; Test++) {
		int N, res = 0;
		fin >> N;
		string *Sinput = new string[N], *compare = new string[N];

		for (int i = 0; i < N; i++) {
			fin >> Sinput[i];
			compare[i] = GetHead(Sinput[i]);
		}

		int stop = 0;
		while (true) {
			res += Solve(compare, N);
			if (stop == 1 || error == 1) break;
			for (int j = 0; j < N; j++) {
				Sinput[j] = Cut(Sinput[j]);
				compare[j] = GetHead(Sinput[j]);
				if (Sinput[j].size() == 0) stop = 1;
			}
		}

		if (error == 1)
			fout << "Case #" << Test << ": Fegla Won" << endl;
		else {
			fout << "Case #" << Test << ": " << res << endl;
		}
		error = 0;
	}
	return 0;
}