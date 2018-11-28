#include <iostream>
#include <deque>

using namespace std;

void solve(string s) {
	deque<char> q;
	char cl = s.at(0);
	q.push_back(cl);
	for(int i = 1; i < s.size(); i++) {
		char l = s.at(i);
		if(l < cl) {
			q.push_back(l);
		} else {
			q.push_front(l);
			cl = l;
		}
	}
	for (char c : q) { cout << c; }
}

int main() {
	int tc;
	cin >> tc;
	for(int ctc = 1; ctc <= tc; ctc++) {
		string s;
		cin >> s;
		cout << "Case  #"<< ctc <<": ";
		solve(s);
		cout << endl;
	}
	return 0;
}
