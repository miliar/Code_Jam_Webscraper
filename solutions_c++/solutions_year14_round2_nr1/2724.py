#include <iostream>
#include <vector>
#include <string>
#include <list>
using namespace std;

void reduce(const string &s1, string &s2, list<int> &l) {
	s2 = "";
	for (int i = 0; i < s1.length(); ++i) {
		char c = s1[i];
		s2 += c;
		int k = 1;
		while (i+1 < s1.length() and s1[i+1] == c) {
			++i;
			++k;
		}
		l.push_back(k);
	}
}

int main() {
	int T;
	cin >> T;
	for (int k = 1; k <= T; ++k) {
		int N;
		cin >> N;
		string current;
		cin >> current;
		string s;
		list<int> min;
		reduce(current, s, min);
		list<int> max(min);
		
		bool possible = true;
		for (int i = 1; i < N; ++i) {
			cin >> current;
			string s2;
			list<int> l;
			reduce (current, s2, l);
			if (s != s2) possible = false;
			if (possible) {
				list<int>::iterator mi = min.begin();
				list<int>::iterator ma = max.begin();
				for (list<int>::iterator it = l.begin(); it != l.end(); ++it) {
					if (*it > *ma) *ma = *it;
					else if (*it < *mi) *mi = *it;
					++mi;
					++ma;
				}
			}
		}
		/*
		bool possible = true;
		int result = 0;
		for (int i = 0; i < N and possible; ++i) {
			int minim, maxim;
			int start = it[0];
			while (it[0] < v[0].length() and v[0][it[0]] == c) ++it[0];
			minim = maxim = it[0]-start;
			for (int j = 1; possible and j < N; ++j) {
				possible = it[j] < v[j].length() and v[j][it[j]] == c;
				start = it[j];
				while (it[j] < v[j].length() and v[j][it[j]] == c) ++it[j];
				if (it[j]-start < minim) minim = it[j]-start;
				else if (it[j]-start > maxim) maxim = it[j]-start;
			}
			result += maxim-minim;
		}
		*/
		cout << "Case #" << k << ": ";
		if (possible) {
			int result = 0;
			list<int>::iterator mi = min.begin();
			list<int>::iterator ma = max.begin();
			while (mi != min.end()) {
				result += *ma - *mi;
				++mi;
				++ma;
			}
			cout << result << '\n';
		}
		else cout << "Fegla Won" << '\n';
	}
}