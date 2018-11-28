#include<string>
#include<iostream>
#include<fstream>

using namespace std;

int dp[101][101][2][2], k;
string s;
int solve(int i, int j, int d, int sn){ 
	int &res = dp[i][j][d][sn];
	if(res != -1)
		return res;
	if( i == j ){
		return res = 0;
	}
	res = 100000000;
	k = i;
	while(k < j && s[k] == '+') 
		k++;
	if(d == 0){ // +++() -> (-)---
		if(sn == 0) 
			res = min(res, solve(k, j, 1, 1) + 2);
		else
			res = min(res, solve(k, j, 1, 1) + 1);
	}else{ // ()--- -> (-)--- 
		if(sn == 0)
			res = min(res, solve(k, j, 1, 1) + 1);
		else
			res = min(res, solve(k, j, 1, 1));
	}
	k = i;
	while(k < j && s[k] == '-') 
		k++;
	if(d == 0){ // ---() -> (+)+++
		if(sn == 0) 
			res = min(res, solve(k, j, 1, 0) + 1);
		else
			res = min(res, solve(k, j, 1, 0) + 2);
	}else{ // ()+++ -> (+)+++ 
		if(sn == 0)
			res = min(res, solve(k, j, 1, 0));
		else
			res = min(res, solve(k, j, 1, 0) + 1);
	}
	k = j - 1;
	while(k >= i && s[k] == '+')
		k--;
	if(d == 0){ // ()+++ -> (+)+++
		if(sn == 0)
			res = min(res, solve(i, k + 1, 0, 0));
		else
			res = min(res, solve(i, k + 1, 0, 0) + 1);
	}else { // ---() -> (+)+++
		if(sn == 0)
			res = min(res, solve(i, k + 1, 0, 0) + 1);
		else
			res = min(res, solve(i, k + 1, 0, 0) + 2);
	}

	k = j - 1;
	while(k >= i && s[k] == '-')
		k--;
	if(d == 0){ // ()--- -> (-)---
		if(sn == 0)
			res = min(res, solve(i, k + 1, 0, 1) + 1);
		else
			res = min(res, solve(i, k + 1, 0, 1));
	}else { // +++() -> (-)---
		if(sn == 0)
			res = min(res, solve(i, k + 1, 0, 1) + 2);
		else
			res = min(res, solve(i, k + 1, 0, 1) + 1);
	}
	return res;
}
int main(){
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int t;
	cin >> t;
	for(int i = 0; i < t ; i++){
		cin >> s;
		memset(dp, -1, sizeof dp);
		cout << "Case #" << i + 1 << ": ";
		cout << solve(0, s.length(), 0, 0) << endl;
	}

	return 0;
}