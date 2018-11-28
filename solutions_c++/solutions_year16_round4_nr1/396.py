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

#define forsn(i,s, n) for(int i=(int)s; i<(int)(n); i++)
#define forn(i, n) forsn(i,0,n)
#define fore(i,n) forn(i,n.size())
#define fori(i, n) for(typeof n.begin() i=n.begin(); i!=n.end();i++)
#define RAYA cout<<"-----------------"<<endl;
#define dbg(x) cout<<#x<<":"<<(x)<<endl;

typedef long long int tint;
typedef long double ldouble;
typedef  pair <tint,tint> pii;
typedef  pair <string,string> pss;
typedef  pair <tint,pii> piii;
typedef  pair <piii,pss> piiiss;

#define pb push_back
#define mp make_pair
#define f first
#define s second
#define all(n) n.begin(),n.end()

const tint INF=2000000000;

string f(char c,int n){
	if(n==0){
		string s;
		s+=c;
		return s;
	}
	if(c=='P'){
		string s1=f('P',n-1);
		string s2=f('R',n-1);
		return min(s1+s2,s2+s1);
	}
	if(c=='R'){
		string s1=f('R',n-1);
		string s2=f('S',n-1);
		return min(s1+s2,s2+s1);
	}
	if(c=='S'){
		string s1=f('S',n-1);
		string s2=f('P',n-1);
		return min(s1+s2,s2+s1);
	}
}

char v[]={'P','S','R'};

int main(){
	int T;
	cin>>T;
	forn(caso,T){
		int N,R,P,S;
		cin>>N>>R>>P>>S;
		string str="Z";
		bool flag=false;
		forn(j,3){
			int r=0;
			int p=0;
			int s=0;
			string pal=f(v[j],N);
			fore(i,pal){
				if(pal[i]=='P')p++;
				if(pal[i]=='S')s++;
				if(pal[i]=='R')r++;
			}
			if(R==r && S==s && P==p){
				flag=true;
				str=min(str,pal);
			}
		}
		cout<<"Case #"<<caso+1<<": ";
		if(flag){
			cout<<str<<endl;			
		}else{
			cout<<"IMPOSSIBLE"<<endl;
		}		
	}
    return 0;
}
