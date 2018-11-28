#include<bits/stdc++.h>
using namespace std;
 

#define pb push_back

 

 #define INF 1000000007
 
int solve(){
	int res = INF;
	int n; cin >> n;
 
	vector<int> V;
	for(int i = 0 ; i < n ; i++){
		int x; cin >> x;
		V.pb(x);
	}
 
	for(int lmt = 1 ; lmt <= 1000 ; lmt++){
		int tmp = lmt;
		for(int i = 0 ; i < V.size() ; i ++){
			tmp += (V[i]-1) / lmt;
		}
 
		res = min(res , tmp);
	}
 
	return res;
}
 
int main(){
	int t,no = 0; cin >> t;
	while(t--){
		cout << "Case #" << ++no << ": " << solve() << endl;
	}
 
	return 0;
}
