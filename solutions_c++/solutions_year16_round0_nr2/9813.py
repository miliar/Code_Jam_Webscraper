#include <bits/stdc++.h>
using namespace std;
int ans;
string s, g;


void bt(int indx, int cnt, string cur) {
	if(indx == s.size()) {
		if(cur == g) {
			ans = min(ans, cnt);
		}
		return ;
	}
	bt(indx + 1, cnt, cur);

}



int main() {
	freopen("B-large.in", "r", stdin);
	freopen("out.out", "w", stdout);
	int t, cas = 1;
	cin >> t;
	while(t--) {
		cin >> s;
		string tmp(s.size(), '+');
		g = tmp;
		ans = 0;
//		bt(0, 0, s);
		int i = 0;
		while(i < s.size() and s[i] == '-') {
			i++;
			ans = 1;
		}

		bool f = 0;
		while(i < s.size()) {
			if(s[i] == '+') {
				f = 1;
			}
			else {
				ans += f*2;
				f = 0;
			}
			i++;
		}

		printf("Case #%d: %d\n", cas++, ans);
	}
	return 0;
}





//
//int main() {
//	freopen("A-large.in", "r", stdin);
//	freopen("out.out", "w", stdout);
//	int t, cas = 1;
//	cin >> t;
//	while(t--) {
//		long long n;
//		cin >> n;
//		set<int>st;
//		int i = 1;
//		for(;i <= 1000000;i++) {
//			long long x = n * i;
//			while(x) {
//				st.insert(x % 10);
//				x /= 10;
//			}
//			if(st.size() == 10) {
//				break;
//			}
//		}
//		if(st.size() == 10) {
//			printf("Case #%d: %lld\n", cas, n * i);
//		} else {
//			printf("Case #%d: INSOMNIA\n", cas);
//		}
//		cas++;
//	}
//	return 0;
//}
