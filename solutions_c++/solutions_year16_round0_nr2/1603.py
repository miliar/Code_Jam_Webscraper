#include <bits/stdc++.h>

using namespace std;

const int MAX_N = 100 + 10;

int A[MAX_N];
int top; int ans;

void refresh() {
	ans = 0;
	for (int i = 0; i < MAX_N; i++) {
		A[i] = 0;
	}
}
int firstact() {
	for (int i = 0; i < top; i++) {
		if (A[i] == 1) {
			A[i] = 0;
		}
		else {
			if (i == 0) {
				return 0;
			}
			return 1;
		}
	}
	return 1;
}
void secondact() {
	vector<int> newans;
	for (int i = 0; i < top; i++) {
		newans.push_back(1 - A[top - 1 - i]);
	}
	for (int i = 0; i < top; i++) {
		A[i] = newans[i];
	}
}
void handle() {
	while (top > 0 && A[top - 1] == 1) {
		top--;
	}
	if (top == 0) {
		return;
	}
	if (firstact()) {
		ans++;
	}
	secondact();
	ans++;
	handle();
}

int main() {
	int t; cin >> t;
	int numoftest = 1;
	while (t--) {
		refresh();
		string thestring;
		cin >> thestring;
		for (int i = 0; i < thestring.size(); i++) {
			if (thestring[i] == '+') {
				A[i] = 1;
			}
			else {
				A[i] = 0;
			}
		}
		top = thestring.size();
		handle();
		cout << "Case #" << numoftest << ": ";
		cout << ans << endl;
		numoftest++;
	}
}
