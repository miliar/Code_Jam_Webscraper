#include <iostream>
#include <vector>
#include <string>

using namespace std;

void flip(vector<int>& v, int pos) {
	// flips, 1 is + -1 is -
	if (pos % 2 == 1) {
		int len = (pos + 1) / 2;
		for (int i = 0; i < len; ++i) {
			int tmp = v[i];
			v[i] = v[pos-i]*-1;
			v[pos-i] = tmp*-1;
		}
	} else {
		int len = pos / 2;
		for (int i = 0; i < len; ++i) {
			int tmp = v[i];
			v[i] = v[pos-i]*-1;
			v[pos-i] = tmp*-1;
		}
		v[len] *= -1;
	}
}

int find_last_minus(vector<int>& vec) {
	for (int i = vec.size() - 1; i >= 0; --i) {
		if(vec[i] == -1) {
			return i;
		}
	}
	return -1;
}

int find_last_plus_before(vector<int>& vec, int pos) {
	if (pos > vec.size())
		return -2;
	if (pos < 1)
		return -2;
	for (int i = pos - 1; i >= 0; --i) {
		if(vec[i] == 1) {
			return i;
		}
	}
	return -1;
}


int main() {
	int T;
	cin >> T;
	for (int i = 0; i < T; ++i) {
		string s;
		vector<int> v;
		cin >> s;
		for (int j = 0; j < s.size(); ++j) {
			if (s[j] == '+') {
				v.push_back(1);
			} else {
				v.push_back(-1);
			}
		}
		cout << "Case #" << i + 1 << ": ";
		/*
		for (int j = 0; j < v.size(); ++j) {
			if(v[j] == 1) {
				cout << "+";
			} else {
				cout << "-";
			}
		}
		cout << endl;
		*/

		if (find_last_minus(v) == -1) {
			cout << "0" << endl;
		} else {
			int m = 0;
			while (find_last_minus(v) != -1) {
				int pos = find_last_minus(v);
				if(v[0] == -1) {
					++m;
					flip(v, pos);
				} else {
					++m;
					int p2 = find_last_plus_before(v, pos);
					if (p2 < 0) {
						flip(v, 0);
					} else {
						flip(v, p2);
					}
				}
			}
			cout << m << endl;
		}

	}
	return 0;
}
