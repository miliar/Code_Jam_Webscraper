/*/**/

#include <bits/stdc++.h>

using namespace std;

int a[33];
int ans[10];

void mns(string s, int sum) {
	for(int i = 0; i < s.size(); i++) {	
		int idx = s[i] - 'A';
		a[idx] -= sum;
	}
}

int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t;
	cin >> t;
	for(int tt = 1; tt <= t; tt++) {
		string s;
		cin >> s;
		memset(a, 0, sizeof a);
		for(int i = 0; i < s.size(); i++) {
			a[s[i] - 'A']++;
		}
		memset(ans, 0, sizeof ans);
		ans[0] = a['Z' - 'A'];
		mns("ZERO", ans[0]);
		ans[2] = a['W' - 'A'];
		mns("TWO", ans[2]);
		ans[4] = a['U' - 'A'];
		mns("FOUR", ans[4]);
		ans[6] = a['X' - 'A'];
		mns("SIX", ans[6]);
		ans[8] = a['G' - 'A'];
		mns("EIGHT", ans[8]);
		ans[1] = a['O' - 'A'];
		mns("ONE", ans[1]);
		ans[3] = a['H' - 'A'];
		mns("THREE", ans[3]);
		ans[5] = a['F' - 'A'];
		mns("FIVE", ans[5]);
		ans[7] = a['S' - 'A'];
		mns("SEVEN", ans[7]);
		ans[9] = a['I' - 'A'];
		mns("NINE", ans[9]);
		cout << "Case #" << tt << ": ";
		for(int i = 0; i < 10; i++) {
			for(int j = 0; j < ans[i]; j++) {
				cout << char(i + '0');
			}
		}
		cout << endl;
	}
	return 0;
}
