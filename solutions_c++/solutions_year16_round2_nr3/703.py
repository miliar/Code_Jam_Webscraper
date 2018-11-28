#include <bits/stdc++.h>
#define rf freopen("ioi.in", "r", stdin)
#define wf freopen("ioi.out", "w", stdout)
using namespace std;
const int MAX = 18;
int t, n;
string a[MAX], b[MAX];
int memo[1 << MAX];
int solve(int mask){
	if(memo[mask] != -1) return memo[mask];
	int res = 0;
	set < string > sa, sb;
	sa.clear(), sb.clear();
	for(int i = 1 ; i <= n ; ++i){
		if(mask & (1 << i)){
			sa.insert(a[i]);
			sb.insert(b[i]);
		}
	}
	for(int i = 1 ; i <= n ; ++i){
		if(!(mask & (1 << i))){
			res = max(res , solve(mask | (1 << i)));
			if(sa.find(a[i]) != sa.end()){
				if(sb.find(b[i]) != sb.end())
					res = max(res , 1 + solve(mask | (1 << i)));
			}
		}
	}
	return memo[mask] = res;
}
int main(){
	rf;
	wf;
	cin >> t;
	for(int qq = 1; qq <= t; qq++){
		cout << "Case #" << qq << ": "; 
		cin >> n;
		for(int i = 1 ; i <= n ; ++i){
			a[i] = b[i] = "";
			cin >> a[i] >> b[i];
		}
		memset(memo , -1 , sizeof(memo));
		cout << solve(0) << endl;
	}
}