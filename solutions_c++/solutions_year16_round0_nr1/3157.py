#include <bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define F first
#define S second
using namespace std;
int slow(int n){
	set<int> seen;
	for(int j=n;j>0;j+=n){
		int k = j;
		while(k){
			seen.insert(k%10); k /= 10;
		} 
		if(seen.size() == 10) return j;
	}
	return -1;
}
int main(){
	ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
	int t; cin >> t;
	for(int T=1;T<=t;T++){
		int n; cin >> n;
		int ans = slow(n);
		cout << "Case #" << T << ": ";
		if(ans == -1) cout << "INSOMNIA\n";
		else cout << ans << "\n";
	}
	return 0;
}