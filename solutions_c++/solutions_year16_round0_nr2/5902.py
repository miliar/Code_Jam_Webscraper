#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	int t; cin >> t;
	for(int tloop = 1; tloop <= t; ++tloop) {
		string s; cin >> s;
		int slen = s.size();
		vector<bool> check(s.size());
		for(int i = 0; i < slen; ++i) {
			check[i] = (s[i] == '+'? 1: 0);
		}
		int idx = 0, cnt = 0;
		while(slen > 1) {
			for(idx = 0; idx < slen-1; ++idx) {
				if(check[idx] == check[idx+1]) continue;
				for(int i = 0; i <= idx; ++i) check[i] = !check[i];
				reverse(check.begin(), check.begin()+idx+1);
				++cnt;
				break;
			}
			if(idx == slen-1) break;
		}
		if(check[0] == 0) ++cnt;
		cout << "Case #" << tloop << ": " << cnt << endl;
	}
}
