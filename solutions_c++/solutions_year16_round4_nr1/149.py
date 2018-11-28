#include<stdio.h>
#include<iostream>
#include<vector>
#include<cmath>
#include<algorithm>
#include<memory.h>
#include<map>
#include<set>
#include<queue>
#include<list>
#include<sstream>
#define mp make_pair
#define pb push_back      
#define F first
#define S second
#define SS stringstream
#define sqr(x) ((x)*(x))
#define m0(x) memset(x,0,sizeof(x))
#define m1(x) memset(x,63,sizeof(x))
#define CC(x) cout << (x) << endl
#define pw(x) (1ll<<(x))
#define M 1000000007
#define N 111111
using namespace std;
typedef pair<int,int> pt;

string al = "RPS";

string get(int x, int k) {
	if (k == 0) {
		return string()+al[x];
	}	
	string a = get(x, k - 1);
	string b = get((x + 2) % 3, k - 1);

	return min(a + b, b + a);
}

int main(){
	freopen("1.in","r",stdin);	
	freopen("1.out","w",stdout);
	int T;
	cin >> T;
	for (int tt = 1; tt <= T; tt++) {
		int k, R, P, S;
		cin >> k >> R >> P >> S;
/*		int n = R + P + S;
		int k = 0;
		while (pw(k) < n) k++;*/

		int ok = 0;
		string ans = "IMPOSSIBLE";
		
		for (int i = 0; i < 3; i++) {
			string t = get(i, k);
//			cout << t << endl;

			int r = 0, p = 0, s = 0;
			for (int j = 0; j < t.size(); j++) if (t[j] == 'R') r++; else if (t[j] == 'P') p++; else s++;
			if (r != R || p != P || s != S) continue;
			if (!ok || (t < ans)) {
				ok = 1;
				ans = t;
			}
		}

		cout << "Case #" << tt << ": ";
		cout << ans << endl;

	}
	return 0;
}