#include <bits/stdc++.h>

using namespace std;

int testcase;
void init(bool flag[]) {
	for(int i = 0; i < 10; i++)
		flag[i] = 0;
}

bool check(bool flag[]) {
	for(int i = 0; i < 10; i++)
		if(flag[i] == 0) return false;
	return true;
}

void work(int n) {
	if(n == 0) {
		cout << "Case #" << testcase << ": INSOMNIA" << endl;
	}
	else {
		bool flag[10]; init(flag);
		int j;
		for(j = 1; !check(flag); j++) {
			int temp = j * n;
			assert(temp <= (int)1e8);
			assert(temp >= 0);
			while(temp) {
				flag[temp%10] = 1;
				temp /= 10;
			}
		}
		cout << "Case #" << testcase << ": " << n*(j-1) << endl;
	}
}

int main() {
	int t, n;
	cin >> t;
	for(testcase = 1; testcase <= t; testcase++) {
		cin >> n;
		work(n);
	}
	return 0;
}