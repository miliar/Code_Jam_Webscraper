#include "template.h"


/*
	정리
	1.
	G가 1개씩만 들어간 original seq들의 G를 찾을 수 있는 것이 가장 중요
	얘네를 찾는게 가능하면 나머진 당연히 된다

	2.
	k, c=1
	: s는 k만큼 필요하다. 모든 칸을 봐야 한다.
	
	3.
	c가 1씩 늘어나면 1칸으로 구경해볼 수 있는 경우의 수가 +1씩 늘어난다
	
	즉
	k=6 c=1 : s는 6필요
	k=6 c=2 : s는 3필요
	k=6 c=3 : s는 2필요
	
	k=3 c=3 : s는 1필요
	즉 c*s >= k여야 한다 ㅇㅈ?


*/


int main() {
	freopen("D-small-attempt0_.in", "r", stdin);
	freopen("output_D.txt", "w", stdout);
	int TC; cin >> TC;
	for (int tc = 1; tc <= TC; ++tc) {
		long long k, c, s;
		cin >> k >> c >> s;
		long long kc = 1;
		for (long long i = 0; i < c; ++i) {
			kc *= k;
		}
		vector<long long> ans;


		if (k == s) {
			long long kc_1 = kc / k;
			for (long long i = 0; i < k; ++i) {
				ans.push_back(i * kc_1 + 1);
			}
		}
		else if(c*s >= k){

		}
		
		printf("Case #%d: ", tc);
		if (ans.empty()) {
			printf("IMPOSSIBLE\n");
		}
		else {
			for (auto l : ans) {
				cout << l << ' ';
			}cout << endl;
		}
	}
	return 0;
}