#include <bits/stdc++.h>
using namespace std;
void generate(int n, int j) {
	int i;
	for(i = 0; i < j; i++) {
		cout << "11";
		string str;
		int temp = i;
		while(i) {
			if(i & 1) {
				str = str + "11";
			} else {
				str = str + "00";
			}
			i >>= 1;
		}
		i = temp;
		while(str.size() != n) {
			str = str + "00";
		}
		reverse(str.begin(), str.end());
		cout << str;
		cout << "11 ";
		int j;
		for(j = 2; j <= 10; j++) {
			cout << j + 1 << " ";
		}
		cout << endl;
	}
}
int main() {
	int t;
	cin >> t;
	int run;
	for(run = 1; run <= t; run++) {
		int n, j;
		cin >> n >> j;
		cout << "Case #" << run << ": " << endl;
		generate((n - 4), j);
	}
	return 0;
}