#include <iostream>
#include <cstdio>
using namespace std;
#define ll long long

bool check(bool a[]){
	for(int i=0;i<10;i++)
		if(!a[i])return false;
	return true;
}

void get(ll n, int idx){
	bool a[10]={false,false,false,false,false,false,false,false,false,false};
	for(ll i=1;i<=1000;i++){
		ll x=i*n;
		while(x){
			ll c=x%10;
			x=x/10;
			a[c]=true;
		}
		if(check(a)){
			cout<<"Case #"<<idx+1<<": "<<n*i<<endl;
			return;
		}
	}
	cout<<"Case #"<<idx+1<<": INSOMNIA"<<endl;
	return;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d",&t);
	for(int i=0;i<t;i++){
		int n;
		scanf("%d",&n);
		get(n,i);
	}
	return 0;
}
