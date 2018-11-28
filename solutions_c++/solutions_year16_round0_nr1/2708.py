# include <bits/stdc++.h>
using namespace std;

int main()
{		
	int T; cin >> T;
	for(int T_=1; T_<=T; ++T_) {
		int64_t n; cin >> n;
		
		if (n == 0) {
			printf("Case #%d: INSOMNIA\n", T_);
			continue;
		}
		
		set<int> nums;
		
		for(int i=1 ;; ++i) {
			int64_t next_n = n*i;
			while(next_n) {
				nums.insert(next_n % 10);
				next_n /= 10;
			}
			
			if (nums.size() == 10) {
				printf("Case #%d: %lld\n", T_, n*i);
				break;
			}
		}
	}
	return 0;
}