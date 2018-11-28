#include <cmath>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
	int numberOfCases, p = 0;
	string N;

	cin >> numberOfCases;
	while (cin >> N) {
		string resp = "";
		vector<int> v;
		vector<char> c;
		// resp.push_back(N[0]);
		for (unsigned int i = 0; i < N.length(); i++) {
			c.push_back(N[i]);
		}

		while (!c.empty()) {
			if (find(c.begin(), c.end(), 'Z') != c.end()) {
				c.erase(find(c.begin(), c.end(), 'Z'));
				c.erase(find(c.begin(), c.end(), 'E'));
				c.erase(find(c.begin(), c.end(), 'R'));
				c.erase(find(c.begin(), c.end(), 'O'));
				v.push_back(0);
			} else if (find(c.begin(), c.end(), 'W') != c.end()) {
				c.erase(find(c.begin(), c.end(), 'T'));
				c.erase(find(c.begin(), c.end(), 'W'));
				c.erase(find(c.begin(), c.end(), 'O'));
				v.push_back(2);
			} else if (find(c.begin(), c.end(), 'G') != c.end()) {
				c.erase(find(c.begin(), c.end(), 'E'));
				c.erase(find(c.begin(), c.end(), 'I'));
				c.erase(find(c.begin(), c.end(), 'G'));
				c.erase(find(c.begin(), c.end(), 'H'));
				c.erase(find(c.begin(), c.end(), 'T'));
				v.push_back(8);
			} else if (find(c.begin(), c.end(), 'H') != c.end()) {
				c.erase(find(c.begin(), c.end(), 'T'));
				c.erase(find(c.begin(), c.end(), 'H'));
				c.erase(find(c.begin(), c.end(), 'R'));
				c.erase(find(c.begin(), c.end(), 'E'));
				c.erase(find(c.begin(), c.end(), 'E'));
				v.push_back(3);
			} else if (find(c.begin(), c.end(), 'X') != c.end()) {
				c.erase(find(c.begin(), c.end(), 'S'));
				c.erase(find(c.begin(), c.end(), 'I'));
				c.erase(find(c.begin(), c.end(), 'X'));
				v.push_back(6);
			} else if (find(c.begin(), c.end(), 'S') != c.end()) {
				c.erase(find(c.begin(), c.end(), 'S'));
				c.erase(find(c.begin(), c.end(), 'E'));
				c.erase(find(c.begin(), c.end(), 'V'));
				c.erase(find(c.begin(), c.end(), 'E'));
				c.erase(find(c.begin(), c.end(), 'N'));
				v.push_back(7);
			} else if (find(c.begin(), c.end(), 'F') != c.end()) {
				if (find(c.begin(), c.end(), 'O') != c.end() && find(c.begin(), c.end(), 'R') != c.end()
				 		&& find(c.begin(), c.end(), 'U') != c.end()) {
					c.erase(find(c.begin(), c.end(), 'F'));
					c.erase(find(c.begin(), c.end(), 'O'));
					c.erase(find(c.begin(), c.end(), 'U'));
					c.erase(find(c.begin(), c.end(), 'R'));
					v.push_back(4);
				} else {
					c.erase(find(c.begin(), c.end(), 'F'));
					c.erase(find(c.begin(), c.end(), 'I'));
					c.erase(find(c.begin(), c.end(), 'V'));
					c.erase(find(c.begin(), c.end(), 'E'));
					v.push_back(5);
				}
			} else if (find(c.begin(), c.end(), 'I') != c.end()) {
				c.erase(find(c.begin(), c.end(), 'N'));
				c.erase(find(c.begin(), c.end(), 'I'));
				c.erase(find(c.begin(), c.end(), 'N'));
				c.erase(find(c.begin(), c.end(), 'E'));
				v.push_back(9);
			} else {
				c.erase(find(c.begin(), c.end(), 'O'));
				c.erase(find(c.begin(), c.end(), 'N'));
				c.erase(find(c.begin(), c.end(), 'E'));
				v.push_back(1);
			}
		}

		while (!v.empty()) {
			if (find(v.begin(), v.end(), 0) != v.end()) {
				v.erase(find(v.begin(), v.end(), 0));
				resp.push_back('0' + 0);
			} else if (find(v.begin(), v.end(), 1) != v.end()) {
				v.erase(find(v.begin(), v.end(), 1));
				resp.push_back('0' + 1);
			} else if (find(v.begin(), v.end(), 2) != v.end()) {
				v.erase(find(v.begin(), v.end(), 2));
				resp.push_back('0' + 2);
			} else if (find(v.begin(), v.end(), 3) != v.end()) {
				v.erase(find(v.begin(), v.end(), 3));
				resp.push_back('0' + 3);
			} else if (find(v.begin(), v.end(), 4) != v.end()) {
				v.erase(find(v.begin(), v.end(), 4));
				resp.push_back('0' + 4);
			} else if (find(v.begin(), v.end(), 5) != v.end()) {
				v.erase(find(v.begin(), v.end(), 5));
				resp.push_back('0' + 5);
			} else if (find(v.begin(), v.end(), 6) != v.end()) {
				v.erase(find(v.begin(), v.end(), 6));
				resp.push_back('0' + 6);
			} else if (find(v.begin(), v.end(), 7) != v.end()) {
				v.erase(find(v.begin(), v.end(), 7));
				resp.push_back('0' + 7);
			} else if (find(v.begin(), v.end(), 8) != v.end()) {
				v.erase(find(v.begin(), v.end(), 8));
				resp.push_back('0' + 8);
			} else if (find(v.begin(), v.end(), 9) != v.end()) {
				v.erase(find(v.begin(), v.end(), 9));
				resp.push_back('0' + 9);
			}
		}



		cout << "Case #" << ++p << ": " << resp << endl;
	}
}
