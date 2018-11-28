#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;
int main(){
	//std::ios::sync_with_stdio(false);  
	freopen("asmall1.in", "r", stdin);
	freopen("output2.txt", "w", stdout);
	int t;
	cin>>t;
	for(int a=1; a<=t; a++){
		int n;
		string s ;
		cin>>n>>s;
		ll num =0, cp=0;
		for(ll i=0; i<=n; i++){
			ll ch = ll(s[i]-'0');
			if(cp<i && ch>0){
				ll more = i-cp;
				num+=more;
				cp+=more;
			}
			cp+=ch;
		}
		cout<<"Case #"<<a<<": "<<num<<endl;
	}
}
