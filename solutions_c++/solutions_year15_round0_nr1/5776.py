#include <iostream>
using namespace std;

int minFriendsForSO(int smax, string s) {
	int i = 0;
	int friends = 0;
	int total = 0;
	for (int i = 0; i <= smax; ++i) {
		int si = s[i]-'0';
		if (i > total) {
			friends++;
			total++;
		}
		total += si;
	}
	return friends;
}

int main() {
	int T;
	cin >> T;
	for (int i = 0; i < T; ++i) {
		int smax;
		string s;
		cin >> smax >> s;
		cout << "Case #" << i+1 << ": " << minFriendsForSO(smax, s) << endl;
	}
}