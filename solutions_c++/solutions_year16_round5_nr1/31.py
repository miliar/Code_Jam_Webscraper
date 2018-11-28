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

const tint INF=2000000000;


int main(){
	int T;
	cin>>T;
	forn(caso,T){
		string s;
		cin>>s;
		vector<char> v;
		fore(i,s){
			if(v.empty()){
				v.pb(s[i]);
			}else{
				if(s[i]==v.back()){
					v.pop_back();
				}else{
					v.pb(s[i]);
				}
			}			
		}
		int res=(s.size()-v.size())*5;
		res+=v.size()/2*5;
		cout<<"Case #"<<caso+1<<": "<<res<<endl;
	}
    return 0;
}
