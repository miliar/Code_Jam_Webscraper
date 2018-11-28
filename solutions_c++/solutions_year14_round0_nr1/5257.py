#include <iostream>
#include <algorithm>
using namespace std;

#define REP(i,n) for (int i = 0; i < n; i++)

int n, t, ans1, ans2, row1[20], row2[20];

int main() {
	cin >> t;
	REP(qqq,t) {
		cin >> ans1;
		REP(i,16) cin >> n, row1[n] = 1+ i/4;
		cin >> ans2;
		REP(i,16) cin >> n, row2[n] = 1+ i/4;

		int cnt = 0, ans = -1;
		REP(i,16) if (row1[i+1] == ans1 && row2[i+1] == ans2) cnt++, ans = i+1;
		
		cout << "Case #" << (qqq+1) << ": ";
		if (cnt == 1)
			cout << ans;
		else
			cout << (cnt==0?"Volunteer cheated!":"Bad magician!");
		cout << endl;
	}
}
