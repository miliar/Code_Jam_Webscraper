#include "stdafx.h"

#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <iomanip>

using namespace std;
typedef long long ll;


bool better(ll a, ll b, ll i, ll j) {
	if (abs(i - j) < abs(a - b)) return true;
	if (abs(i - j) > abs(a - b)) return false;
	if (i < a) return true;
	if (i > a) return false;
	if (j < b) return true;
	return false;
}

bool valid(ll x, const string& s) {
	for (int pos = s.size() - 1; pos >= 0; --pos) {
		if (s[pos] != '?' && s[pos] != '0' + (x % 10))
			return false;
			x /= 10;
	}
		return x == 0;
}

int main() {
	ifstream in;
	in.open("../Bin.txt");
	ofstream out;
	out.open("../Bout.txt");

	int T;
	in >> T;
	for (int icase = 1; icase <= T; ++icase) {
		out << "Case #" << icase << ": ";

		string s1, s2;
		in >> s1 >> s2;
		int n = s1.size();
		int a = 999, b = 0;
		for (int i = 0; i < 1000; ++i)
			if (valid(i, s1))
				for (int j = 0; j < 1000; ++j)
					if (better(a, b, i, j) && valid(j, s2)) {
						a = i;
						b = j;
					}

		out << setfill('0') << setw(n) << a << ' ' << setfill('0') << setw(n) << b;
		out << "\n";
	}
}