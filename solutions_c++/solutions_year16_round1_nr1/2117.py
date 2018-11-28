#include <iostream>
#include <cstdio>
#include <list>

using namespace std;

int main() {

	int N;
	scanf("%d\n", &N);

	string str;
	for (int i = 0; i < N; ++i) {
		getline(cin, str);
		//cout << str << endl;
		list<char> newStr;
		newStr.push_back(str[0]);
		for (int j = 1; j < str.size(); ++j) {
			if (newStr.front() <= str[j]) {
				newStr.push_front(str[j]);
			} else {
				newStr.push_back(str[j]);
			}
		}
		cout << "Case #" << (i + 1) << ": ";
		while (newStr.size()) {
			cout << newStr.front();
			newStr.pop_front();
		}
		cout << endl;
	}

	return 0;
}