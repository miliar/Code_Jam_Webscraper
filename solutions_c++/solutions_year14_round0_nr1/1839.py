#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>

using namespace std;
int casenum,T;

int main() {
	freopen("gcj14.in","r",stdin);
	freopen("gcj14.out","w",stdout);
	cin >> T;
	for (casenum = 1; casenum <= T; casenum++) {
		cout << "Case #" << casenum << ": ";
		int la, lb;
		int a[5][5], b[5][5];
		cin >> la;
		for (int i = 1; i <= 4; i++)
			for (int j = 1; j <= 4; j++)
				cin >> a[i][j];
		cin >> lb;
		for (int i = 1; i <= 4; i++)
			for (int j = 1; j <= 4; j++)
				cin >> b[i][j];
		int num, cnt;
		cnt = 0;
		for (int i = 1; i <= 4; i++)
			for (int j = 1; j <= 4; j++)
				if (a[la][i] == b[lb][j]) {
					num = a[la][i];
					cnt++;
				}
		if (cnt == 1)
			cout << num;
		else {
			if (cnt == 0)
				cout << "Volunteer cheated!";
			else cout << "Bad magician!";
		}
		cout <<endl;
	}
	return 0;
}
