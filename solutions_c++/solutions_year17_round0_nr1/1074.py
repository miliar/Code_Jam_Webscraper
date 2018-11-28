#include <iostream>
#include <fstream>
#include <string>

using namespace std;

void change(string &s, int K) {
	for (int i = 0; i < K; ++i) {
		if (s[i] == '-') {
			s[i] = '+';
		}
		else {
			s[i] = '-';
		}
	}
}

int search(string &s, int K) {
	if (s.size() == K - 1) {
		for (string::iterator iter = s.begin(); iter != s.end(); ++iter) {
			if (*iter == '-') {
				return -1;
			}
		}
		return 0;
	}
	if (s[0] == '+') {
		return search(s.substr(1), K);
	}
	else {
		change(s, K);
		int step = search(s.substr(1), K);
		return step == -1 ? step : step + 1;
	}
}

void run(istream &in, ostream &out) {
	int T;
	in >> T;
	for (int i = 0; i < T; ++i) {
		string s;
		int K;
		in >> s >> K;
		int step = search(s, K);
		if (step == -1) {
			out << "Case #" << (i + 1) << ": " << "IMPOSSIBLE" << endl;
		}
		else {
			out << "Case #" << (i + 1) << ": " << step << endl;
		}

	}
}

int main()
{
	// ifstream fin("A-large.in");
	// ofstream fout("A-large.out");
	// run(fin, fout);
	run(cin, cout);
	return 0;
}