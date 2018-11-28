#include<iostream>
#include<vector>
#include<cstdio>
#include<cmath>
#include<map>
#include<set>
#include<algorithm>
#include<stack>
#include<queue>
#include<string>
#include<cstring>

using namespace std;

void remove0(string& s, vector<int> &v) {
	int c = count(s.begin(), s.end(), 'Z');
	for (int i = 0; i < c; i++) v.push_back(0);
	for (int i = 0; i < c; i++) {
		for (string::iterator j = s.begin(); j != s.end(); j++) {
			if (*j == 'Z') {
				s.erase(j);
				break;
			}
		}
	}
	for (int i = 0; i < c; i++) {
		for (string::iterator j = s.begin(); j != s.end(); j++) {
			if (*j == 'E') {
				s.erase(j);
				break;
			}
		}
	}
	for (int i = 0; i < c; i++) {
		for (string::iterator j = s.begin(); j != s.end(); j++) {
			if (*j == 'R') {
				s.erase(j);
				break;
			}
		}
	}
	for (int i = 0; i < c; i++) {
		for (string::iterator j = s.begin(); j != s.end(); j++) {
			if (*j == 'O') {
				s.erase(j);
				break;
			}
		}
	}
}
void remove1(string& s, vector<int> &v) {
	int c = count(s.begin(), s.end(), 'N');
	for (int i = 0; i < c; i++) v.push_back(1);
	for (int i = 0; i < c; i++) {
		for (string::iterator j = s.begin(); j != s.end(); j++) {
			if (*j == 'O') {
				s.erase(j);
				break;
			}
		}
	}
	for (int i = 0; i < c; i++) {
		for (string::iterator j = s.begin(); j != s.end(); j++) {
			if (*j == 'N') {
				s.erase(j);
				break;
			}
		}
	}
	for (int i = 0; i < c; i++) {
		for (string::iterator j = s.begin(); j != s.end(); j++) {
			if (*j == 'O') {
				s.erase(j);
				break;
			}
		}
	}
}
void remove2(string& s, vector<int> &v) {
	int c = count(s.begin(), s.end(), 'W');
	for (int i = 0; i < c; i++) v.push_back(2);
	for (int i = 0; i < c; i++) {
		for (string::iterator j = s.begin(); j != s.end(); j++) {
			if (*j == 'T') {
				s.erase(j);
				break;
			}
		}
	}
	for (int i = 0; i < c; i++) {
		for (string::iterator j = s.begin(); j != s.end(); j++) {
			if (*j == 'W') {
				s.erase(j);
				break;
			}
		}
	}
	for (int i = 0; i < c; i++) {
		for (string::iterator j = s.begin(); j != s.end(); j++) {
			if (*j == 'O') {
				s.erase(j);
				break;
			}
		}
	}
}
void remove3(string& s,vector<int> &v) {
	int c = count(s.begin(), s.end(), 'T');
	for (int i = 0; i < c; i++) v.push_back(3);
	for (int i = 0; i < c; i++) {
		for (string::iterator j = s.begin(); j != s.end(); j++) {
			if (*j == 'T') {
				s.erase(j);
				break;
			}
		}
	}
	for (int i = 0; i < c; i++) {
		for (string::iterator j = s.begin(); j != s.end(); j++) {
			if (*j == 'H') {
				s.erase(j);
				break;
			}
		}
	}
	for (int i = 0; i < c; i++) {
		for (string::iterator j = s.begin(); j != s.end(); j++) {
			if (*j == 'R') {
				s.erase(j);
				break;
			}
		}
	}
	for (int i = 0; i < 2 * c; i++) {
		for (string::iterator j = s.begin(); j != s.end(); j++) {
			if (*j == 'E') {
				s.erase(j);
				break;
			}
		}
	}
}
void remove4(string& s, vector<int> &v) {
	int c = count(s.begin(), s.end(), 'U');
	for (int i = 0; i < c; i++) v.push_back(4);
	for (int i = 0; i < c; i++) {
		for (string::iterator j = s.begin(); j != s.end(); j++) {
			if (*j == 'F') {
				s.erase(j);
				break;
			}
		}
	}
	for (int i = 0; i < c; i++) {
		for (string::iterator j = s.begin(); j != s.end(); j++) {
			if (*j == 'O') {
				s.erase(j);
				break;
			}
		}
	}
	for (int i = 0; i < c; i++) {
		for (string::iterator j = s.begin(); j != s.end(); j++) {
			if (*j == 'U') {
				s.erase(j);
				break;
			}
		}
	}
	for (int i = 0; i < c; i++) {
		for (string::iterator j = s.begin(); j != s.end(); j++) {
			if (*j == 'R') {
				s.erase(j);
				break;
			}
		}
	}
}
void remove5(string& s,vector<int> &v) {
	int c = count(s.begin(), s.end(), 'F');
	for (int i = 0; i < c; i++) v.push_back(5);
	for (int i = 0; i < c; i++) {
		for (string::iterator j = s.begin(); j != s.end(); j++) {
			if (*j == 'F') {
				s.erase(j);
				break;
			}
		}
	}
	for (int i = 0; i < c; i++) {
		for (string::iterator j = s.begin(); j != s.end(); j++) {
			if (*j == 'I') {
				s.erase(j);
				break;
			}
		}
	}
	for (int i = 0; i < c; i++) {
		for (string::iterator j = s.begin(); j != s.end(); j++) {
			if (*j == 'V') {
				s.erase(j);
				break;
			}
		}
	}
	for (int i = 0; i < c; i++) {
		for (string::iterator j = s.begin(); j != s.end(); j++) {
			if (*j == 'E') {
				s.erase(j);
				break;
			}
		}
	}
}
void remove6(string& s,vector<int> &v) {
	int c = count(s.begin(), s.end(), 'X');
	for (int i = 0; i < c; i++) v.push_back(6);
	for (int i = 0; i < c; i++) {
		for (string::iterator j = s.begin(); j != s.end(); j++) {
			if (*j == 'S') {
				s.erase(j);
				break;
			}
		}
	}
	for (int i = 0; i < c; i++) {
		for (string::iterator j = s.begin(); j != s.end(); j++) {
			if (*j == 'I') {
				s.erase(j);
				break;
			}
		}
	}
	for (int i = 0; i < c; i++) {
		for (string::iterator j = s.begin(); j != s.end(); j++) {
			if (*j == 'X') {
				s.erase(j);
				break;
			}
		}
	}
}
void remove7(string& s,vector<int> &v) {
	int c = count(s.begin(), s.end(), 'S');
	for (int i = 0; i < c; i++) v.push_back(7);
	for (int i = 0; i < c; i++) {
		for (string::iterator j = s.begin(); j != s.end(); j++) {
			if (*j == 'S') {
				s.erase(j);
				break;
			}
		}
	}
	for (int i = 0; i < 2 * c; i++) {
		for (string::iterator j = s.begin(); j != s.end(); j++) {
			if (*j == 'E') {
				s.erase(j);
				break;
			}
		}
	}
	for (int i = 0; i < c; i++) {
		for (string::iterator j = s.begin(); j != s.end(); j++) {
			if (*j == 'V') {
				s.erase(j);
				break;
			}
		}
	}
	for (int i = 0; i < c; i++) {
		for (string::iterator j = s.begin(); j != s.end(); j++) {
			if (*j == 'N') {
				s.erase(j);
				break;
			}
		}
	}
}
void remove8(string& s, vector<int>& v) {
	int c = count(s.begin(), s.end(), 'G');
	for (int i = 0; i < c; i++) v.push_back(8);
	for (int i = 0; i < c; i++) {
		for (string::iterator j = s.begin(); j != s.end(); j++) {
			if (*j == 'E') {
				s.erase(j);
				break;
			}
		}
	}
	for (int i = 0; i < c; i++) {
		for (string::iterator j = s.begin(); j != s.end(); j++) {
			if (*j == 'I') {
				s.erase(j);
				break;
			}
		}
	}
	for (int i = 0; i < c; i++) {
		for (string::iterator j = s.begin(); j != s.end(); j++) {
			if (*j == 'G') {
				s.erase(j);
				break;
			}
		}
	}
	for (int i = 0; i < c; i++) {
		for (string::iterator j = s.begin(); j != s.end(); j++) {
			if (*j == 'H') {
				s.erase(j);
				break;
			}
		}
	}
	for (int i = 0; i < c; i++) {
		for (string::iterator j = s.begin(); j != s.end(); j++) {
			if (*j == 'T') {
				s.erase(j);
				break;
			}
		}
	}
}
void remove9(string& s, vector<int> &v) {
	int c = count(s.begin(), s.end(), 'I');
	for (int i = 0; i < c; i++) v.push_back(9);
	for (int i = 0; i < c; i++) {
		for (string::iterator j = s.begin(); j != s.end(); j++) {
			if (*j == 'N') {
				s.erase(j);
				break;
			}
		}
	}
	for (int i = 0; i < c; i++) {
		for (string::iterator j = s.begin(); j != s.end(); j++) {
			if (*j == 'I') {
				s.erase(j);
				break;
			}
		}
	}
	for (int i = 0; i < c; i++) {
		for (string::iterator j = s.begin(); j != s.end(); j++) {
			if (*j == 'N') {
				s.erase(j);
				break;
			}
		}
	}
	for (int i = 0; i < c; i++) {
		for (string::iterator j = s.begin(); j != s.end(); j++) {
			if (*j == 'E') {
				s.erase(j);
				break;
			}
		}
	}
}
int main() {
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	int t;
	cin >> t;
	for (int done = 0; done < t; done++) {
		string s;
		cin >> s;
		vector<int> n;
		
		remove0(s,n);
		remove2(s,n);
		remove4(s,n);
		remove5(s,n);
		remove6(s,n);
		remove7(s,n);
		remove8(s,n);
		remove9(s,n);
		remove3(s,n);
		remove1(s,n);

		sort(n.begin(), n.end());
		cout << "Case #" << done + 1 << ": ";
		for (int i = 0; i < n.size(); i++) cout << n[i];
		cout << endl;
	}
	return 0;
}