#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
using namespace std;


int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int n;
	cin >> n;
	for (int i = 1; i <= n; i++){
		int t;
		cin >> t;
		string x;
		cin >> x;
		int already = 0;
		int ans = 0;
		for (int j = 0; j < x.length(); j++){
			int tek = x[j] - '0';
			if (already < j){
				int dif = j - already;
				ans += dif;
				already += dif;
			}
			already += tek;
		}
		cout << "Case #" << i << ": " << ans << endl;
	}
	return 0;
}