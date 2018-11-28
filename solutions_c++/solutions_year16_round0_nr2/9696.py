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

ll conversion(string s){
	ll ans = 0;
	for(int i = 1; i < s.size(); i++){
		if(s[i] != s[i-1])
			ans++;
	}
	return ans;
}

int main(){
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t;
	cin>>t;
	for(int j = 1; j <= t; j++){
		string s;
		cin>>s;
		s.append("+");
		ll answer = conversion(s);			
		cout<<"Case #"<<j<<": "<<answer<<endl;
	}
	
	return  0;
}