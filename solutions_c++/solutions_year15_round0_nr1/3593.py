#include<bits/stdc++.h>
#define rep(i,k,n) for(int i = k; i < (int) n; i++)
#define mp make_pair
#define pb push_back
#define ft first
#define sd second
typedef long long ll;
const long long inf = 9223372036854775807;
const int iinf = 2147483647;
const int limit = 1048576;
using namespace std;

int main(){
	freopen("Standing_Ovation.txt","w",stdout);
	freopen("A-large.in","r",stdin);
	int t; cin >> t;
	
	rep(j, 1, t + 1){
		int s_max; cin >> s_max;
		string s; cin >> s;
		
		int res = 0, pref = 0;
		rep(i, 0, s_max + 1){
			res = max(res, i - pref);
			pref += s[i] - '0';
		}
		
		cout << "Case #" << j << ": " << res <<"\n";
	}

	return 0;
}
