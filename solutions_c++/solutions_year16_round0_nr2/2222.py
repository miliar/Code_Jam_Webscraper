#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

vector<bool> st;

int iolm() {
	int i = st.size() - 1;
	while (st[i]) i--;
	return i;
}

int ioefp() {
	int i = 0;
	while (st[i]) i++;
	i--;
	return i;
}

void maneuver(int b) {
	reverse(st.begin(), st.begin() + b + 1);
	for (vector<bool>::iterator it = st.begin(); it != st.begin() + b + 1 ; it++) 
		*it = !*it;
}

bool done() {
	bool ret = true;
	for (int i = 0; i < st.size(); i++) {
		ret = ret && st[i];
	}
	return ret;
}


int main()
{
	int t;
	cin >> t;

	int c = 1;

	while (t--) {
		
		cout << "Case #" << c << ": ";
		c++;

		int moves = 0;

		string s;
		cin >> s;

		st.clear();
		for (int i = 0; i < s.size(); i++) {
			if (s[i] == '-') st.push_back(false);
			else st.push_back(true);
		}

		while (!done()) {

			if (!st[0]) {
				maneuver(iolm());
			}
			else {
				maneuver(ioefp());
			}

			/*for (int i = 0; i < st.size(); i++) {
				if (st[i]) cerr << "+";
				else cerr << "-";
			}
			cerr << endl;*/

			moves++;


		}
		
		cout << moves << endl;

	}
	return 0;
}

/*
for (int i = 0; i < st.size(); i++) {
			if (st[i]) cout << "+";
			else cout << "-";
		}
		*/