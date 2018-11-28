#include <bits/stdc++.h>

using namespace std;

#define MAX(a, b) (((a) > (b)) ? (a) : (b))
#define MIN(a, b) (((a) < (b)) ? (a) : (b))
#define ABS(a) (((a) > (0)) ? (a) : (-1 * (a)))

int main() {
	int t;
	
	ifstream cin;
	cin.open("A-large.in");

	ofstream cout;
	cout.open("out.txt");

	cin >> t;

	for (int z = 1; z <= t; z++) {
		int n;
		cin >> n;
		string s;

		cin >> s;
		int count = 0;
		int res = 0;
		for (int i = 0; i < s.size(); i++) {
			int tmp = s[i] - '0';
			
			if (i == 0) {
				count += tmp;
				continue;
			}

			if (count < i) {
				res += i - count;
				count = i;
			}
			count += tmp;
		}

		cout << "Case #" << z << ": " << res << endl;
	}
}