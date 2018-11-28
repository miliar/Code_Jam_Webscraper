#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int n, k;
vector<string> allans;

string doubleString(string thestring) {
	string theans = "";
	for (int i = 0; i < thestring.size(); i++) {
		theans += thestring[i];
		theans += thestring[i];
	}
	return theans;
}
string cascadeString(string thestring, int number) {
	string newstring = "";
	for (int i = 0; i < (number - thestring.size()); i++) {
		newstring += '0';
	}
	newstring += thestring;
	return newstring;
}
string reverseString(string thestring) {
	string ans = "";
	for (int i = thestring.size() - 1; i >= 0; i--) {
		ans += thestring[i];
	}
	return ans;
}
string toBin(int thenum) {
	string theans = "";
	ll temp = thenum;
	while (temp) {
		if (temp % 2) {
			theans += '1';
		}
		else {
			theans += '0';
		}
		temp /= 2;
	}
	theans = reverseString(theans);
	return theans;
}
void handle() {
	for (int i = 0; i < (1 << (n / 2)); i++) {
		if (i == k) {
			break;
		}
		string newans = ""; string tempans = "";
		tempans = toBin(i);
		tempans = cascadeString(tempans, n / 2 - 1);
		tempans = doubleString(tempans);
		newans += '1';
		newans += tempans;
		newans += '1';
		allans.push_back(newans);
	}
}

int main() {
	int t; cin >> t;
	cin >> n >> k;
	handle();
	cout << "Case #1:" << endl;
	for (int i = 0; i < allans.size(); i++) {
		cout << allans[i] << " ";
		for (int j = 2; j < 10; j++) {
			cout << j + 1 << " ";
		}
		cout << 11 << endl;
	}
}
