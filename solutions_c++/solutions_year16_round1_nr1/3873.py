#include <iostream>

using namespace std;

string sol(string &s) {
	string snew;
	snew.push_back(s.at(0));
	for (unsigned int i = 1; i < s.size(); i++) {
		if (s.at(i) >= snew.at(0)) snew.insert(0, 1, s.at(i)); 
		else snew.push_back(s.at(i));
	}
	return snew;
}

int main() {

	int x = 0;
	cin >> x;

	for (int i = 1; i <= x; i++) {
		string s;
		cin >> s;
		cout << "Case #" << i << ": ";
		cout << sol(s) << endl;
	}

	return 0;
}