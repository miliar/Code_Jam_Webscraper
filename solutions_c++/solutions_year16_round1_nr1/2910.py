#include <string>
#include <iostream>
#include <sstream>
#include <list>

using namespace std;

int main() {
	int t; cin >> t; cin.ignore();

	for (int i = 1; i <= t; ++i) {
		string in; cin >> in;
		list<char> word;

		word.push_front(in.at(0));

		for (int j = 1; j < in.size(); ++j) {
			if (in.at(j) >= word.front())
				word.push_front(in.at(j));
			else
				word.push_back(in.at(j));
		}

		cout << "Case #" << i << ": ";

		for (list<char>::iterator it = word.begin(); it != word.end(); ++it) {
			cout << *it;
		}

		cout << endl;
	}
}
