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
		int ans = 1234567890;
		int a[1001];
		for (int i = 1; i <= k; ++i){
			cin >> a[i];
		}
		for (int c = 1; c <= 1000; ++c){
			int cnt = 0;
			for (int i = 1; i <= k; ++i){
				cnt += max((a[i] + c - 1) / c - 1, 0);
			}
			ans = min(ans, cnt + c);
		}
		printf("Case #%d: %d\n", qq, ans);
	}


}