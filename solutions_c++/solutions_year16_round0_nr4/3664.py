#include <iostream>
#include <unordered_map>
#include <string>
#include <set>
#include <vector>
using namespace std;
typedef long long ll;

void foo(vector<ll> &v, int k, int c, int s){
	if(c==1){
		for(ll i=1;i<=k;i++) v.push_back(i);
	} else {
		ll l = pow(k,c);
		ll ml = pow(k, c-1);
		ll index = 1;
		for(ll i=1;i<=k;i++){
			v.push_back(index);
			index += ml;
		}
	}
}

int main(){
	int T,k,c,s;
	cin>>T;
	int x=0;
	while(T--){
		cin>>k>>c>>s;
		x++;
		if(s<k) cout << "Case #"<<x <<": IMPOSSIBLE"<<endl;
		else {
			vector<ll> v;
			foo(v,k,c,s);
			cout << "Case #"<<x<<":";
			for(auto x:v){
				cout<<" "<<x;
			}
			cout<<endl;
		}
	}
	return 0;
}
