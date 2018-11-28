#include <iostream>
#include <vector>
#include <map>
#include <math.h>
#include <cmath>
#include <set>
#include <algorithm>
#include <stack>
#include <stdio.h>
#include <string>
using namespace std;

#define forsn(i,s,n) for(int i=(int)s; i<(int)(n); i++)
#define forn(i,n) forsn(i,0,n)
#define fore(i,n) forn(i,n.size())
#define fori(i,n) for(typeof n.begin() i=n.begin(); i!=n.end();i++)
#define RAYA cout<<"-----------------"<<endl;
#define dbg(x) cout<<#x<<":"<<(x)<<endl;

typedef long long int tint;
typedef  pair <tint,tint> pii;

#define pb push_back
#define mp make_pair
#define f first
#define s second
#define all(n) n.begin(),n.end()


int main(){
	int T;
	cin>>T;
	forn(caso,T){
		int n,l;
		cin>>n>>l;
		vector<string> s (n);
		forn(i,n)cin>>s[i];
		string b;
		cin>>b;
		bool flag= false;
		forn(i,n){
			if(s[i]==b)flag=true;
		}
		if(flag){
			cout<<"Case #"<<caso+1<<": IMPOSSIBLE"<<endl;
		}else{
			string a;
			fore(i,b){
				if(b[i]=='0'){
					a+='1';
				}else{
					a+='0';
				}
			}
			cout<<"Case #"<<caso+1<<": ";
			forn(i,l)cout<<a[i]<<"?";
			cout<<" ";
			forn(i,l-1)cout<<a[i]<<b[i];
			cout<<a[l-1]<<endl;
		}

	}
    return 0;
}
