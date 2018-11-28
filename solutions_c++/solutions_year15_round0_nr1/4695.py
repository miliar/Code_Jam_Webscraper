#include <iostream>
#include <cstdio>

using namespace std;

int main() {
	int nc;
	cin >> nc;
	for(int cid=1; cid<=nc; ++cid) {
		int n;
		cin >> n;
		string s;
		cin >> s;
		int ans = 0, cur = 0;
		for(int i=0; i<s.size(); ++i) {
			int num = s[i] - '0';
			if(cur < i) {
				ans += i-cur;
				cur = i;
			}
			cur += num;
		}
		printf("Case #%d: %d\n", cid, ans);
	}
	return 0;
}

