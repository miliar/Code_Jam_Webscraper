#include <iostream>
#include <stdio.h>

using namespace std;

int a[4][4], b[4][4];
int r1, r2;

void read() {
	cin >> r1;
	r1 --;
	for(int i = 0; i < 4; i ++)
		for(int j = 0; j < 4; j ++)
			cin >> a[i][j];
	cin >> r2;
	r2 --;
	for(int i = 0; i < 4; i ++)
		for(int j = 0; j < 4; j ++)
			cin >> b[i][j];
}

void solve() {
	int cnt = 0;
	for(int i = 0; i < 4; i ++)
		for(int j = 0; j < 4; j ++)
			if(a[r1][i] == b[r2][j]) {
				cnt ++;
				break;
			}
	
	if(cnt == 0) cout << "Volunteer cheated!\n";
	else if(cnt > 1) cout << "Bad magician!\n";
	else {
		for(int i = 0; i < 4; i ++)
			for(int j = 0; j < 4; j ++)
				if(a[r1][i] == b[r2][j]) {
					cout << a[r1][i] << endl;
					break;
				}
	}
}

int main()
{
	int t;
	cin >> t;
	for(int i = 1; i <= t; i ++) {
		printf("Case #%d: ", i);
		
		read();
		solve();
	}

    return 0;
}
