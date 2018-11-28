#include<iostream>
#include<cstdio>
#include<string>
#include<cstring>
#include<vector>
#include<set>
#include<list>
#include<queue>
#include<cmath>
#include<functional>
#include<algorithm>
#define INF (1<<29)
#define EPS 1e-10
#define rep(i,n) for(int i=0;i<(n);i++)
using namespace std;

typedef unsigned long long ull;
vector<ull> v;

bool palindrome(ull a){
	string s;
	while(a){
		s+='0'+a%10;
		a/=10;
	}
	bool f=true;
	rep(i,s.size()/2){
		if(s[i]!=s[s.size()-1-i])f=false;
	}
	return f;
}
int main(){
	ios::sync_with_stdio(0);
	cin.tie(0);

	for(ull i=1;i<=10000000;i++){
		if(palindrome(i) && palindrome(i*i))v.push_back(i*i);
	}
	int t;
	ull a,b;
	cin>>t;
	rep(i,t){
		cin>>a>>b;
		int ans=upper_bound(v.begin(),v.end(),b)-lower_bound(v.begin(),v.end(),a);
		cout<<"Case #"<<i+1<<": "<<ans<<endl;
	}
	return 0;
}