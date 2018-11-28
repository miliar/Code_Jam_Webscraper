#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <set>
#include <string>
using namespace std;


int main() {
	freopen("B-large.in", "r", stdin);
	freopen("outputB.txt", "w", stdout);
	int n;
	cin >> n;
	string str;
	int kol=0;
	bool state;
	for (int i = 0; i < n; i++) {
		cin >> str;
		if (str[0] == '-') {
			//kol++;
			state = false;
		}
		else state = true;
		for (int j = 1; j < str.length(); j++) {
			if ((str[j] == '+' && state == false) || (str[j] == '-' && state == true)) {
				state = !state;
				kol++;
			}
		}
		if (str[str.length() - 1] == '-') kol++;
		cout <<"Case #"<<i+1<<": "<< kol << endl; 
		kol = 0;
	}
	return 0;
}