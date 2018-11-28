#include <bits/stdc++.h>
#define rep(i,n) for(int i = 0; i < n; i++)
#define INF 100000000
#define EPS 1e-10
#define MOD 1000000007
using namespace std;
typedef pair<int,int> P;

string s;
int cnt[26];
int ans[10];

void solve(){
	cin >> s;
	rep(i,26) cnt[i] = 0;
	rep(i,10) ans[i] = 0;
	rep(i,s.size()) cnt[s[i]-'A']++;
	ans[6] = cnt[23]; cnt[18] -= cnt[23]; cnt[8]  -= cnt[23]; cnt[23] = 0;
	ans[0] = cnt[25]; cnt[4]  -= cnt[25]; cnt[14] -= cnt[25]; cnt[17] -= cnt[25]; cnt[25] = 0;
	ans[2] = cnt[22]; cnt[19] -= cnt[22]; cnt[14] -= cnt[22]; cnt[22] = 0;
	ans[4] = cnt[20]; cnt[14] -= cnt[20]; cnt[5]  -= cnt[20]; cnt[17] -= cnt[20]; cnt[20] = 0;
	ans[1] = cnt[14]; cnt[13] -= cnt[14]; cnt[4]  -= cnt[14]; cnt[14] = 0;
	ans[5] = cnt[5];  cnt[8]  -= cnt[5];  cnt[21] -= cnt[5];  cnt[4]  -= cnt[5]; cnt[5] = 0;
	ans[7] = cnt[21]; cnt[18] -= cnt[21]; cnt[4]  -= cnt[21]; cnt[4]  -= cnt[21]; cnt[13] -= cnt[21]; cnt[21] = 0;
	ans[8] = cnt[6];  cnt[4]  -= cnt[6];  cnt[8]  -= cnt[6];  cnt[7]  -= cnt[6];  cnt[19] -= cnt[6]; cnt[6] = 0;
	ans[3] = cnt[17]; cnt[19] -= cnt[17]; cnt[7]  -= cnt[17]; cnt[4]  -= cnt[17]; cnt[4]  -= cnt[17]; cnt[17] = 0;
	ans[9] = cnt[8];  cnt[13] -= cnt[8];  cnt[13] -= cnt[8];  cnt[4]  -= cnt[8]; cnt[8] = 0;
	rep(i,10) rep(j,ans[i]) cout << i;
	cout << endl;
}

int main(){
	int t;
	cin >> t;
	rep(i,t){
		cout << "Case #" << i+1 << ": ";
		solve();
	}
}