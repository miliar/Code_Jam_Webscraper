#include <iostream>
#include <string>
#include <deque>

using namespace std;

void last() {
	string s;
	cin >> s;
	
	deque<char> q;
	q.push_front(s[0]);
	for (int i=1; i<s.length(); i++) {
		if (s[i] >= q.front()) q.push_front(s[i]);
		else q.push_back(s[i]);
	}
	for (int i=0; i<s.length(); i++) cout << q[i];
	cout << endl;
}

int main() {
	int T;
	cin >> T;
	for (int i=0; i<T; i++) {
		cout << "Case #" << i+1 << ": ";
		last();
	}
	return 0;
}