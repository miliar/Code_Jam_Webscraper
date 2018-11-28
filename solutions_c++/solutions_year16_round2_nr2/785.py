#include <bits/stdc++.h>
#define rf freopen("ioi.in", "r", stdin)
#define wf freopen("ioi.out", "w", stdout)
using namespace std;
int t;
string c, j;
void solve(string &s, int pos, int sum, int lim, vector < int > &v){
	if(pos == lim){
		v.push_back(sum);
		return;
	}
	if(s[pos] == '?'){
		for(int i = 0; i <= 9; i++) solve(s, pos + 1, sum * 10 + i, lim, v);
	}
	else{
		solve(s, pos + 1, sum * 10 + (s[pos] - '0'), lim, v);
	}
}
int main(){
	ios :: sync_with_stdio(false);
	rf, wf;
	cin >> t;
	for(int qq = 1; qq <= t; qq++){
		cout << "Case #" << qq << ": ";
		cin >> c >> j;
		int len = c.size();
		vector < int > vc, vj;
		solve(c, 0, 0, len, vc);
		solve(j, 0, 0, len, vj);
		int x = vc.size(), y = vj.size();
		pair < int , pair < int , int > > ans;
		ans.first = ans.second.first = ans.second.second = 1e9;
		for(int i = 0; i < x; i++){
			for(int j = 0; j < y; j++){
				pair < int , pair < int , int > > can;
				can.first = abs(vc[i] - vj[j]);
				can.second.first = vc[i];
				can.second.second = vj[j];
				if(can < ans) ans = can;
			}
		}
		string ans1 = to_string(ans.second.first);
		string ans2 = to_string(ans.second.second); 
		int add = len - ans1.size();
		for(int i = 1; i <= add; i++) cout << "0";
		cout << ans1;
		cout << " ";
		add = len - ans2.size();
		for(int i = 1; i <= add; i++) cout << "0";
		cout << ans2;
		cout << "\n";
	}
}