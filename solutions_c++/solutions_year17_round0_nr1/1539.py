#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <string>
#include <algorithm>
#include <cstdlib>
#include <vector>
#include <cmath>
#include <map>
#include <set>
#include <utility>
#include <sstream>
#include <queue>
#include <unordered_set>
#include <bitset>
using namespace std;




int main()
{
#ifndef ONLINE_JUDGE
	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);
#endif
	int t;
	cin >> t;
	for (int z = 1; z <= t; z++){
		string str;
		int k;
		cin >> str >> k;
		int n = str.length();
		int ans = 0;
		for (int i = 0; i <= n - k; i++){
			if (str[i] == '-'){
				ans++;
				for (int j = 0; j < k; j++) {
					str[i + j] = ((str[i + j] == '+') ? '-' : '+');
				}
			}
		}
		for (int i = 0; i < k; i++){
			if (str[n - 1 - i] == '-') ans = -1;
		}
		cout << "Case #" << z << ": ";
		if (ans == -1) cout << "IMPOSSIBLE"; 
		else cout << ans;
		cout << endl;
	}
	
	return 0;
}