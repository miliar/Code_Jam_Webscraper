#include <bits/stdc++.h>

using namespace std;

int solve() {
	int a;
	cin >> a;
	string S;
	cin >> S;

	int friends = 0;
	int total = 0;
	for(int i=0; i < S.size(); i++) {
		if(total + friends < i) friends += i - (total+friends);
		total += S[i] - '0'; 
	}
	return friends;
}

int main() {
	int t;
	cin >> t;
	for(int i=1; i <=t; i++) cout << "Case #" << i << ": " << solve() << endl;
}