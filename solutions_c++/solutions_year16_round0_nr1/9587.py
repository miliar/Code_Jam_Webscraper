#include<stdio.h>
#include<iostream>
#include<algorithm>
#include<string>
#include<vector>
#include<iomanip>
#define ll long long
//#define for(i,b,n) for(int (i)=(b);(i)<(n);(i)++)
#define endl "\n"
using namespace std;
bool num[10];

bool check(ll a){
	while(a!=0){
		num[a%10]=1;
		a/=10;
	}
	for(int i = 0; i < 10; i++){
		if(num[i] == 0)
			return false;
	}
	return true;
}

ll method(ll n){
	for(ll  i = 1; ;i++){
		ll a = n*i;
		if(check(a))
			return a;
	}
}

int main(){
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t;
	cin>>t;
	for(int j = 1; j <= t; j++){
		for(int i = 0; i < 10; i++)
			num[i] = 0;
		ll n;
		cin>>n;
		if(n==0)
			cout<<"Case #"<<j<<": "<<"INSOMNIA"<<endl;
		else{
			ll answer = method(n);
			cout<<"Case #"<<j<<": "<<answer<<endl;
		}
	}
	
	return  0;
}