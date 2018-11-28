#include <bits/stdc++.h>

using namespace std;

const int MAX_N = 2*1000 + 20;

char A[MAX_N];

int startindex;
int finishindex;

void refresh() {
	for (int i = 0; i < MAX_N; i++) {
		A[i] = 'z';
		startindex = 1000 + 5;
		finishindex = 1000 + 5;
	}
}
string solve(string s) {
	A[startindex] = s[0];
	finishindex++;
	for (int i = 1; i < s.size(); i++) {
		if (A[startindex] > s[i]) {
			A[finishindex] = s[i];
			finishindex++;
		}
		else {
			startindex--;
			A[startindex] = s[i];
		}
	}
	string ans = "";
	for (int i = startindex; i < finishindex; i++) {
		ans += A[i];
	}
	return ans;
}

int main() {
	int t; cin >> t;
	int numoftestcase = 1;
	while (t--) {
		string newstring;
		cin >> newstring;
		refresh();
		string newans = solve(newstring);
		cout << "Case #" << numoftestcase << ": " << newans << endl;
		numoftestcase++;
	}
}
