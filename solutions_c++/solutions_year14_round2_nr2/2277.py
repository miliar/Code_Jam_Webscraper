/*
 *	Category: tempo
 *  Problem: B.cpp
 *  Status: 
 * 	Date: May 3, 2014
 * 	Start: 7:38:58 PM	End: 		Duration: 
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

int main() {
#ifndef ONLINE_JUDGE 
	//INs(); //OUs();
#endif
	freopen("in", "rt", stdin);
	freopen("out", "wt", stdout);
	int tc, t = 0, A, B, K;
	cin >> tc;
	while(tc--){
		printf("Case #%d: ",++t);
		cin >> A >> B >> K;
		if(B > A) swap(A,B);
		int cnt = 0;
		for(int i = 0; i < A; i++){
			for(int j = 0; j < B; j++){
				if((i&j) < K)
					cnt++;
			}
		}
		cout << cnt << "\n";
	}
	return 0;
}
