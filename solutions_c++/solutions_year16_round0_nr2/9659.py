#include <iostream>
#include <stdio.h>
#include <map>
using namespace std;

string str;
int h = 0;
bool test() {
	for (int i = 0; i < str.size(); i++) {
		if (str[i] == '-')
			return 0;
	}
	return 1;
}

bool sol() {
	int indx = -1;
	for (int i = 0; i < str.size(); i++) {
		if (str[i] == '-')
			indx = i;
	}
	if (indx == -1)
		return 1;
	for (int i = 0; i <= indx; i++) {
		if (str[i] == '-')
			str[i] = '+';
		else
			str[i] = '-';
	}
	h++;
	//cout << str << " " << indx << endl;
	return test();

}

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int t;
	cin >> t;
	int z = t;
	int k = 0;
	while (t--) {
		k = 0;
		h = 0;
		cin >> str;
		while (!sol()) {

		}
		cout << "Case #" << z - t << ": " << h << endl;
	}
	return 0;
}
