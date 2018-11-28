#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
int main(){
	ifstream inp("./aLarge.in");
	ofstream out("./aLarge.out");
	int t;
	inp>>t;
	for(int i=1; i<=t; i++){
		out<<"Case #"<<i<<": ";
		ll n;
		inp>>n;
		if(n==0){
			out<<"INSOMNIA"<<endl;
		}
		else{
			set<ll> digits;
			ll mul = 1;
			ll num = 0;
			while(digits.size()<10){
				num = mul * n;
				while(num>0){
					ll dig = num%10;
					digits.insert(dig);
					num/=10;
				}
				mul++;
			}
			ll ans = (mul-1)* n;
			out<<ans<<endl;
		}
	}
}