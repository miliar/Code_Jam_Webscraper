#include<bits/stdc++.h>
using namespace std;
#define pb push_back
typedef long long ll;

bool checkPrime(ll val, vector<ll> & div){
	for(ll i=2; i*i<=val; i++){
		if(val%i==0){
			div.pb(i);
			return false;
		}
	}
	return true;
}
int main(){
	ifstream inp("./cSmall.in");
	ofstream out("./cSmall.out");
	int t;
	inp>>t;
	for(int a=1; a<=t; a++){
		out<<"Case #"<<a<<":"<<endl;
		ll n,j;
		inp>>n>>j;
		ll ct = 0;
		for(ll i=0; i<(1<<(n-2)) && ct<j; i++){
			string rep = "1";
			for(ll k=(n-3); k>=0; k--){
				if(i&(1<<k)){
					rep.pb('1');
				}
				else{
					rep.pb('0');
				}
			}
			rep.pb('1');
			vector<ll> divisors;
			bool isPrime = false;
			for(ll b =2; b<=10; b++ ){
				ll val = 0;
				for(ll k = 0; k<rep.size(); k++){
					val = b*val + (rep[k]-'0');			
				}

				if(checkPrime(val, divisors)){
					isPrime = true;
					break;
				}

			}

			if(isPrime){
				continue;
			}
			else{
				ct++;
				out<<rep<<" ";
				for(ll k=0; k<divisors.size(); k++){
					out<<divisors[k];
					if(k==(divisors.size()-1)){
						out<<endl;
					}
					else out<<" ";
				}
			}
		}
	}
}