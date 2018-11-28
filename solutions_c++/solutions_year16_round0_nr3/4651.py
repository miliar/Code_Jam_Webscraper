#include<bits/stdc++.h>

using namespace std;
typedef long long ll;
ll t,n,j,tc,x,tem,num;
vector<ll> dig;
vector<ll> s;

ll isprime(ll n){
	if(n%2 == 0){
		if( n == 2)
		return 0;
		else
		return 2;
	}
	for(ll i = 3;i*i <= n;i+=2){
		if(n%i == 0)
		return i;
	}
	return 0;
}

int main(){

tc = 1;
cin>>t;
while(t--){
	cin>>n>>j;
	x = ((1ll)<<(n-2));
	cout<<"Case #"<<tc<<":"<<endl;
	for(ll i = 0;i<x && j>0;i++){
		dig.clear();
		dig.push_back(1);
		tem = i;
		while(tem){
			dig.push_back(tem%2);
			tem/=2;
		}
		while(dig.size()<(n-1)){
			dig.push_back(0);
		}
		dig.push_back(1);
		s.clear();
		for(ll b = 2;b<=10;b++){
			num = 0;
			for(ll ii = dig.size() - 1;ii>=0;ii--){
					num+=dig[ii];
					num*=b;
			}
			num/=b;
			if(isprime(num))
			s.push_back(isprime(num));
		}
		if(s.size() == 9){
			for(ll ii = dig.size() - 1;ii>=0;ii--)
			cout<<dig[ii];
			cout<<" ";
			for(int it = 0;it<s.size();++it){
			cout<<s[it]<<" ";
		}
		cout<<endl;
		j--;
		}
	}
	tc++;
}
return 0;
}
