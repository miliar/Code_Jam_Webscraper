#include <iostream>
#include <string>

using namespace std;

int solve() {
	int N;
	cin >> N;
	string s1, s2;
	cin >> s1;
	cin >> s2;
	
	int l1 = s1.size();
	int l2 = s2.size();
	
	int i = 0, j = 0;
	
	int count = 0;
	
	while (i < l1 && j < l2) {
		if (s1[i] == s2[j]) {
			i++; j++;
		}
		else {
			if (i == 0 && j == 0) return -1;
			if (i != 0 && s1[i] == s1[i-1]) {
				count++;
				i++;
			} else if (j != 0 && s2[j] == s2[j-1]) {
				count++;
				j++;
			} else
				return -1;			
		}
	}
	if (i == l1) {
		count += l2-j;
		for (; j < l2; j++)
			if (s2[j] != s1[i-1])
				return -1;
	}
	else if (j == l2) {
		count += l1-i;
		for (; i < l1; i++)
			if (s1[i] != s2[j-1])
				return -1;
	}
	return count;
}

int main() {
	int T;
	cin >> T;
	
	for (int t = 1; t <= T; t++) {
		int r = solve();
		if (r == -1)
			cout << "Case #" << t << ": Fegla Won" << endl;
		else
			cout << "Case #" << t << ": " << r << endl;
	}
}
