#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <vector>
#include <algorithm>
#include <set>
#include <stack>
#include <cstdio>
#include <ctime>
using namespace std;

int main(){
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	ios_base::sync_with_stdio(0);
	int q;
	cin >> q;
	for (int qq = 1; qq <= q; ++qq){
		int k;
		cin >> k;
		string s;
		cin >> s;
		int cnt = 0;
		int ans = 0;
		for (int i = 0; i <= k; ++i){
			int cur = s[i] - '0';
			if (!cur || cnt >= i){
				cnt += cur;
				continue;
			}
			ans += i - cnt;
			cnt += cur + ans;
		}
		cout << "Case #" << qq << ": " << ans << endl;
	}
}