# include <bits/stdc++.h>
using namespace std;

int main()
{		
	int T; cin >> T;
	for(int T_=1; T_<=T; ++T_) {
		string s; cin >> s;
		
		bool good = true;
		for(int i=0; i<s.size() && good; ++i) {
			good &= (s[i] == '+');
		}
		if (good) {
			printf("Case #%d: 0\n", T_);
			continue;
		}
		
		map<string, int> mp;
		mp[s] = 1;
		
		deque<string> dq = {s};
		while(!dq.empty()) {
			string t = dq.front(); dq.pop_front();
			int p = mp[t]+1;
			
			for(int i=1; i<=t.size(); ++i) {
				string t1 = t;
				for(int f=0; f<i; ++f) {
					t1[f] = (t1[f] == '+'? '-':'+');
				}
				for(int f1=0, f2=i-1; f1<f2; ++f1, --f2) {
					swap(t1[f1], t1[f2]);
				}
				
				if (mp[t1] == 0 or mp[t1] > p) {
					mp[t1] = p;
					dq.push_back(t1);
				}
			}
		}
		
		string et;
		for(int i=0; i<s.size(); ++i) {
			et += '+';
		}
		printf("Case #%d: %d\n", T_, mp[et]-1);
	}
	return 0;
}