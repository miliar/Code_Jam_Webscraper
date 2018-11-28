#include <iostream>
#include <vector>
#include <algorithm>
#include <set>

using namespace std;

const long long I_MAX = 100000;

int main() {
	long long n_tests;

	cin >> n_tests;
	cin.ignore();

	for (long long test = 0; test < n_tests; test++) {
		// input
		long long n;
		long long i;
		set<int> s;
		cin >> n;
		cin.ignore();

		for (i = 1; s.size() < 10 && i < I_MAX; i++) {
			for (char c : to_string(n*i)) {
				if (s.find(c-'0') == s.end()) {
					s.insert(c - '0');
					//cout << c-'0' << endl;
				}
			}
		}

		cout << "Case #" << test+1 << ": "; 

		// output
		cout << ((i < I_MAX) ? (to_string(n*(i-1))) : ("INSOMNIA"));

		cout << endl;
	}

	return 0;
}