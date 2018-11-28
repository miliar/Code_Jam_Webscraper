#include <bits/stdc++.h>
typedef long long ll;

using namespace std;

ll K,S,C;
ll pw(ll a, ll b){
	ll x=1;
	for(int i=0;i<b;i++){
		x=x*a;
	}
	return x;
}
void solve(){
	ll num = pw(K,C-1);
	ll start=1;
	for(int i=0;i<S;i++){
		cout << start << " ";
		start+=num;
	}
}
int main(int argc, char const *argv[]){
	int T;
	cin >> T;
	for(int i=0;i<T;i++){
		cin >> K >> C >> S;
		printf("Case #%d: ",i+1);
		solve();
		cout << endl;
	}
	return 0;
}