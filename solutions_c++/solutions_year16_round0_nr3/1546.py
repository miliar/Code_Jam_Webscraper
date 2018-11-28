#include <bits/stdc++.h>
using namespace std;
typedef long long               ll;
const int mod = 1e9+7;
#ifndef M_PI
#define M_PI acos(-1.0)
#endif


int main(){
	vector<int> primes;
	for(int i=2; i<1000; ++i){
		bool p=true;
		for(int j=2; j<i; ++j){
			if(!(i%j)){
				p=false;
			}
		}
		if(p){
			primes.push_back(i);
		}
	}
	int t, n, c;
	cin>>t;
	for(int ct=0; ct<t; ++ct){
		cin>>n>>c;
		cout<<"Case #"<<ct+1<<":\n";
		for(ll x=(1<<(n-1))+1; c>0; x+=2){
			vector<int> divs;
			for(int base=2; base<=10; ++base){
				int div_f=-1;
				for(int p : primes){
					int rem=0;
					for(int i=n-1; i>=0; --i){
						rem*=base;
						if(x&(1<<i)){
							rem+=1;
						}
						rem%=p;
					}
					if(rem==0){
						div_f=p;
						break;
					}
				}
				if(div_f==-1){
					break;
				}
				else{
					divs.push_back(div_f);
				}
			}
			if(divs.size()==9){
				if(n==16){
					cout<<(bitset<16>)x;
				}
				if(n==32){
					cout<<(bitset<32>)x;
				}
				for(int d : divs){
					cout<<" "<<d;
				}
				cout<<"\n";
				--c;
			}
		}
	}
	return 0;
}
