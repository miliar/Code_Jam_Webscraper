#define _GLIBCXX_DEBUG
#include<iostream>
#include<cstdio>
#include<bits/stdc++.h>//"geometry.cpp"
#include<iomanip>//"cout<<fixed<<setprecision(n)<<sth<<endl;"
#include<queue>
#include<string>
#include<vector>
#include<utility>
#include<set>
#include<map>
#include<algorithm>//"lower_bound(it,it,v)", "next_permutation(a,a+n)"
#include<functional>//"greater<T>" Ex. sort(a,a+n,greater<int>());
#include<cmath>//"abs", "sqrt"
using namespace std;
#define pb push_back
#define fi first
#define sc second
#define mp make_pair
#define is insert
typedef pair<int,int> pii;//Add other types in the same way.

void solve(int q){
	string s;
	int a[1000],k,ans=0;
	cin>>s>>k;
	for(int i=0;i<s.size();++i){
		if(s[i]=='+'){
			a[i]=0;
		}else{
			a[i]=1;
		}
	}
	for(int i=0;i<=s.size()-k;++i){
		if(a[i]%2==1){
			++ans;
			for(int di=1;di<k;++di){
				++a[i+di];
			}
		}
	}
	cout<<"Case #"<<q<<": ";
	bool f=false;
	for(int i=s.size()-k+1;i<s.size();++i){
		if(a[i]%2==1){
			f=true;
			cout<<"IMPOSSIBLE"<<endl;
			break;
		}
	}
	if(!f){
		cout<<ans<<endl;
	}
}

int main(){
	int Q;
	cin>>Q;
	for(int q=1;q<=Q;++q){
		solve(q);
	}
}
