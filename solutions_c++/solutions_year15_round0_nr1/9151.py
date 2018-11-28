#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>
#include <limits.h>
using namespace std;

int main() {
	int t; cin >> t;
	for(int j = 0; j < t; j++){
		int n; cin >> n;
		string s; cin >> s;
		int a[10005], sum[10005];
		for (int i = 0; i < s.size(); ++i) a[i] = s[i] - '0';
		sum[0] = a[0];
		for (int i = 1; i < s.size(); ++i){
			sum[i] = sum[i - 1] + a[i];
		}
		int ans = 0;
		for (int i = 1; i < s.size(); ++i){
			if(a[i] > 0){
				if(sum[i - 1] + ans < i)ans += (i - sum[i - 1] - ans);
			}
		}
		cout << "Case #" << j + 1 << ": " << ans << endl;
	}
	return 0;
}