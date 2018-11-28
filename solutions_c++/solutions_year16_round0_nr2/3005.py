#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <string>
#include <cstring>
#include <queue>
#include <map>
#include <stack>

using namespace std;

string s;
int a[105];
int len;
void parse() {
	cin >> s;
	len = s.length();
	for (int i = 0; i < len; i++){
		if (s[i] == '+')
			a[i] = 1;
		else a[i] = 0;
	}
}

void solve() {
	int sign = 1;
	int sum = 0;
	
	for (int i = len-1; i>=0; i--){

		int ok = 1;
		for (int j =0; j <= i; j++)
			if (a[j]!=sign){
				ok = 0;
				break;
			}
		if (ok){
			cout << sum << endl;
			return;
		}

		if (a[i] != sign){
			sign = 1-sign;
			sum ++;
		}
	}

	cout << sum << endl;
}

int main() {
	int T;
	cin >> T;

	for (int i = 1; i <= T; i++){
		parse();
		cout << "Case #" << i << ": ";
		solve();
	}
	return 0;
}



