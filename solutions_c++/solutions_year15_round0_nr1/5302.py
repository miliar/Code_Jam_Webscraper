#include <iostream>
#include <fstream>
#include <string>
#include <cstdio>
using namespace std;

int cs, n;
string s;
int main() {
//    ifstream cin("txt.in");
//    ofstream cout("txt.out");
	cin >> cs;
	for (int T = 1; T <= cs; T++) {
		cin >> n >> s;
		int ans = 0, sum = 0;
		for (int i = 0; i <= n; i++) {
			if (i > sum)
				ans += i - sum, sum += i - sum;
			sum += s[i] - '0';
		}
		cout << "Case #" << T << ": " << ans << endl;
	}
}
