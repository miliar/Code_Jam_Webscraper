#include <bits/stdc++.h>
/*
#include<iostream>
#include<algorithm>
#include<string>
#include<vector>
#include<set>
#include<map>
#include<queue>
#include<deque>
#include<stack>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cassert>
*/
using namespace std;

typedef long long ll;
typedef pair<int,int> pint;
typedef vector<int> vint;
typedef vector<ll> vll;

#define mp make_pair
#define pb push_back

#define fi first
#define se second

#define repp(i,a,b) for(int i=(int)(a);i<=(int)(b);++i)
#define rep(i,n) repp(i,0,(n)-1)

typedef pair<int, pint> tint;
#define one first
#define two second.first
#define thr second.second

typedef pair<tint, string> T;

T emp = mp(mp(-1,mp(-1,-1)), "");

T p(int);
T r(int);
T s(int);

tint tasu(const tint &a, const tint &b){
	tint res;
	res.one = a.one + b.one;
	res.two = a.two + b.two;
	res.thr = a.thr + b.thr;
	return res;
}

bool comp(string a, string b){ // a <= b
	rep(i, a.length()){
		if(a[i] != b[i]) return (a[i] < b[i]);
	}
	return true;
}

vector<T> pmemo, rmemo, smemo;
T p(int n){
	if(n == 0){
		return (pmemo[0] = mp(mp(1,mp(0,0)), "P") );
	}
	if(pmemo[n] != emp){
		return pmemo[n];
	}
	T pp = p(n-1);
	T rr = r(n-1);
	tint res1 = tasu(pp.fi, rr.fi);
	string res2;
	if( comp(pp.se, rr.se) ){
		res2 = pp.se + rr.se;
	}else{
		res2 = rr.se + pp.se;
	}
	return (pmemo[n] = mp(res1, res2));
}
T r(int n){
	if(n == 0){
		return (rmemo[0] = mp(mp(0,mp(1,0)), "R") );
	}
	if(rmemo[n] != emp){
		return rmemo[n];
	}
	T pp = s(n-1);
	T rr = r(n-1);
	tint res1 = tasu(pp.fi, rr.fi);
	string res2;
	if( comp(pp.se, rr.se) ){
		res2 = pp.se + rr.se;
	}else{
		res2 = rr.se + pp.se;
	}
	return (rmemo[n] = mp(res1, res2));
}
T s(int n){
	if(n == 0){
		return (smemo[0] = mp(mp(0,mp(0,1)), "S") );
	}
	if(smemo[n] != emp){
		return smemo[n];
	}
	T pp = p(n-1);
	T rr = s(n-1);
	tint res1 = tasu(pp.fi, rr.fi);
	string res2;
	if( comp(pp.se, rr.se) ){
		res2 = pp.se + rr.se;
	}else{
		res2 = rr.se + pp.se;
	}
	return (smemo[n] = mp(res1, res2));
}

void main2(){
	int N, R, P, S;
	cin >> N >> R >> P >> S;
	T ppp = p(N);
	T rrr = r(N);
	T sss = s(N);
	if(ppp.fi == mp(P, mp(R, S))){
		cout << ppp.se << endl;
	}else if(sss.fi == mp(P, mp(R, S))){
		cout << sss.se << endl;
	}else if(rrr.fi == mp(P, mp(R, S))){
		cout << rrr.se << endl;
	}else{
		cout << "IMPOSSIBLE" << endl;
	}
}

int main(){
	pmemo.assign(20,emp);
	rmemo.assign(20,emp);
	smemo.assign(20,emp);
	int casenum; cin >> casenum;
	rep(casenow, casenum){
		printf("Case #%d: ", casenow+1);
		main2();
	}
	return 0;
}

