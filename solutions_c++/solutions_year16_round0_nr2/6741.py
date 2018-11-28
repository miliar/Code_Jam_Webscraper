# include <cstdio>
# include <iostream>
# include <vector>
# include <algorithm>
# include <cmath>
# include <queue>
# include <map>
# include <cstring>
# include <string>
# include <set>

using namespace std;

# define INF 1000000000

int dp[101][101];
string s;

int rec(int t, int pos){
	int& res = dp[t][pos];
	if(res != -1) return res;

	if(t == s.size()){
		if(pos == t) return 0;
		else return INF;
	}

	int curr = pos + ((s[t] == '+')? 1 : 0);
	res = rec(t+1, curr);
	res = min(res, 1 + rec(t+1, t - curr + 1));

	return res;

}

int main(){
	
	freopen("input.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int ttt;
	cin>>ttt;

	for(int tt = 1; tt <= ttt; tt++){

		cin>>s;

		memset(dp, -1, sizeof(dp));
		int res = rec(0, 0);

		cout<<"Case #"<<tt<<": "<<res<<endl;

	}

	return 0;
}