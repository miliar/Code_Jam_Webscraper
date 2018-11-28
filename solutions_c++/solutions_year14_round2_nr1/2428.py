/*
 *	Category: tempo
 *  Problem: A.cpp
 *  Status: 
 * 	Date: May 3, 2014
 * 	Start: 6:04:24 PM	End: 		Duration: 
 * 	Author: Hossam Yousef
 */

#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int, int> pi;
typedef vector<pi> vpi;

#define OO (int)1e9
#define sz(v) (int)v.size()
#define all(c) (c).begin(),(c).end()
#define mems(s,v) memset(s,v,sizeof(s))

int n;
int cost[102][102];
string str[102];
int dp[102][102];

pi solve(int x, int y){
	vi v1(1,0), v2(1,0);
	string s1 = "", s2 = "";
	for(int i = 0; i < sz(str[x]); i++){
		if(!sz(s1)){
			s1 += str[x][i];
			v1[0]++;
			continue;
		}
		if(str[x][i] == s1[sz(s1)-1]){
			v1[sz(s1)-1]++;
			continue;
		}else{
			s1 += str[x][i];
			v1.push_back(1);
		}
	}
	for(int i = 0; i < sz(str[y]); i++){
		if(!sz(s2)){
			s2 += str[y][i];
			v2[0]++;
			continue;
		}
		if(str[y][i] == s2[sz(s2)-1]){
			v2[sz(s2)-1]++;
			continue;
		}else{
			s2 += str[y][i];
			v2.push_back(1);
		}
	}
	if(s1 != s2)
		return make_pair(-1,-1);
	int res = 0;
	str[n] = s1;
	for(int i = 0; i < sz(v1); i++)
		res += abs(v1[i]-v2[i]);
	return make_pair(res,sz(s1));
}

int main() {
	freopen("in", "rt", stdin);
	freopen("out", "wt", stdout);
	int tc, t = 0;
	cin >> tc;
	while(tc--){
		printf("Case #%d: ",++t);
		cin >> n;
		for(int i = 0; i <= n; i++)
			for(int j = 0; j <= n; j++)
				cost[i][j] = OO;
		for(int i = 0; i < n; i++) cin >> str[i];
		bool flag[4] = {0};
		for(int i = 0; i < n; i++){
			for(int j = i+1; j < n; j++){
				mems(dp,-1);
				pi x = solve(i,j);
				if(x.first == -1){
					cout << "Fegla Won\n";
					flag[0] = 1;
					break;
				}
				cost[i][n] = sz(str[i]) - x.second;
				cost[j][n] = sz(str[j]) - x.second;
				cost[n][i] = sz(str[i]) - x.second;
				cost[n][j] = sz(str[j]) - x.second;
				cost[i][j] = cost[j][i] = x.first;
				if(str[n] == str[i] || str[n] == str[j])
					flag[1] = 1;
				if(n == 2){
					cout << min(x.first,(sz(str[i]) - x.second) + (sz(str[j]) - x.second)) << endl;
					flag[0] = 1;
					break;
				}
			}
			if(flag[0])
				break;
		}
		if(flag[0])
			continue;
		if(!flag[1])
			n++;
		int res = OO;
		for(int i = 0; i < n; i++){
			int sum = 0;
			for(int j = 0; j < n; j++){
				if(i == j)
					continue;
				sum += cost[i][j];
			}
			res = min(res,sum);
		}

		cout << res << "\n";
	}
	return 0;
}
