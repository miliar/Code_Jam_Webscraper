#include <bits/stdc++.h>
#define ll unsigned long long
using namespace std;
void inc(bool c[], ll n){
	while(n>0){
		c[n%10]++;
		n /= 10;
	}
}
bool check(bool c[]){
	for(int i = 0; i<10; i++){
		if(c[i]==0)
			return false;
	}
	return true;
}
int main(){
	ios::sync_with_stdio(false);
	cin.tie(0);
	int t;
	cin>>t;
	for(int j = 1; j<=t; j++){
		bool c[10];
		for(int i = 0; i<10; i++){
			c[i] = 0;
		}
		ll n, ans, x;
		cin>>n;
		if(n!=0){
			inc(c, n);
			for(int i = 2; ;i++){
				if(check(c)){
					ans = x;
					break;
				}
				else{
					x = n*i;
					inc(c, x);
				}
			}
			cout<<"Case #"<<j<<": "<<ans<<endl;
		}
		else
			cout<<"Case #"<<j<<": "<<"INSOMNIA"<<endl;
	}
	return 0;
}
