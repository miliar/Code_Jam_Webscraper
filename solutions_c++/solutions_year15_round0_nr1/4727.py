#include<iostream>
#include<string>
#include<vector>
#include<algorithm>

#define REP(a, b, c) for(long long a=(b); a<(c); a++)

using namespace std;

int main(){
	std::ios::sync_with_stdio(false);
	int T;
	cin >> T;
	REP(t, 1, T+1){
		cout << "Case #" << t << ": ";
		int cnt = 0, N;
		string s;
		cin >> N >> s;
		vector<int> v;
		REP(i, 0, N+1)
			REP(j, 0, s[i]-'0')
				v.push_back(i);
		REP(i, 0, v.size()){
			int diff = 0;
			if(v[i]>i) diff = v[i] - i;
			cnt = max(cnt, diff);
		}
		cout << cnt << "\n";
	}
	return 0;
}
