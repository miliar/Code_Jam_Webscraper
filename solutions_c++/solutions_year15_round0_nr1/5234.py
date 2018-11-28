#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <vector>
#include <queue>
#include <cstring>

using namespace std;

int arr[1500];
int main() {
	if(fopen("input.in","r")) {
		freopen("input.in","r",stdin);
		freopen("output.out","w",stdout);
	}
	int casenum; cin >> casenum;
	string s;
	for(int i = 1; i <= casenum; i++) {
		int ans = 0; 
		int curadd = 0;
		memset(arr, 0, sizeof(arr));
		int mx; cin >> mx;
		cin >> s;
		for(int j = 0; j < s.length(); j++) {
			arr[j] = s[j] - '0';
			if(j > ans) {
				curadd += j-ans;
				ans += j-ans;
			}
			ans += arr[j];
		}
		cout << "Case #" << i << ": " << curadd << '\n';
	}
	return 0;
}