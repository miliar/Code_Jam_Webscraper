#include<iostream>
#include<fstream>
#include<algorithm>
#include<vector>
#include<string>
using namespace std;
/*
int main(){
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("B-small-attempt0.out", "w", stdout);
	int t;
	cin >> t;
	for(int i = 0; i < t; i++){
		int a, b, k;
		cin >> a >> b >> k;
		int ans = 0;
		for(int i = 0; i < a; i++)
			for(int j = 0; j < b; j++)
				if((i & j) < k)
					ans++;
		cout << "Case #" << i + 1 << ": " << ans << endl;
	}
	return 0;
}
*/
#define LL long long
LL dp[100][3][3][3];
vector<int> x1, x2, x3;
int n;
LL solve(int idx, int c1, int c2, int c3){
	if(idx == -1){
		if(c1 && c2 && c3)
			return 1;
		else
			return 0;
	}
	LL &res = dp[idx][c1][c2][c3];
	if(res != -1)
		return res;
	res = 0;
	for(int i = 0; i < 2; i++)
		for(int j = 0; j < 2; j++){
			int c = i & j;

			if(c1 +( i <= x1[idx]) > 0){
				if(c2 + (j <= x2[idx]) > 0)
					if(c3 + (c <= x3[idx]) > 0)
						res += solve(idx - 1, c1 | (i < x1[idx]), c2 | (j < x2[idx]), c3 | (c < x3[idx]));
			}
		}
	return res;
}

				


int main(){
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int t;
	cin >> t;
	for(int i = 0; i < t; i++){
		int a, b, k;
		cin >> a >> b >> k;
		memset(dp, -1, sizeof dp);
		x1.clear();
		x2.clear();
		x3.clear();
		while(a){
			x1.push_back(a % 2);
			a /= 2;
		}
		while(b){
			x2.push_back(b % 2);
			b /= 2;
		}
		while(k){
			x3.push_back(k % 2);
			k /= 2;
		}
		int n = max(x1.size(), max(x2.size(), x3.size()));
		while(x1.size() < n)
			x1.push_back(0);
		while(x2.size() < n)
			x2.push_back(0);
		while(x3.size() < n)
			x3.push_back(0);
		LL ans = solve(n - 1, 0, 0, 0);
		cout << "Case #" << i + 1 << ": " << ans << endl;
	}
	return 0;
}