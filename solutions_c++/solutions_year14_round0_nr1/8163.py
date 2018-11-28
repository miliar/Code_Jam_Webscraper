#include <iostream>
#include <stdio.h>
#include <memory.h>

using namespace std;

int t, n, idx = 1, arr[20], tmp;

void getInput() {
	cin >> n;
	for(int i = 0; i < 4; i++)
		for(int j = 0; j < 4; j++) {
			cin >> tmp;
			if(i + 1 == n) arr[tmp]++;
		}
}

void getRes() {
	int res, c = 0;
	for(int i = 0; i < 17; i++) if(arr[i] == 2) c++, res = i;
	if(!c) cout << "Volunteer cheated!";
	else if(c > 1) cout << "Bad magician!";
	else cout << res;
	cout << endl;
}


int main() {
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("output.out", "w", stdout);
	cin >> t;
	while(t--) {
		memset(arr, 0, sizeof arr);
		getInput();
		getInput();
		printf("Case #%d: ", idx++);
		getRes();
	}

	return 0;
}
