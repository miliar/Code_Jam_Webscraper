#include <bits/stdc++.h>
// iostream is too mainstream
#include <cstdio>
// bitch please
#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <list>
#include <cmath>
#include <iomanip>
#include <time.h>
#define dibs reserve
#define OVER9000 1234567890
#define ALL_THE(CAKE,LIE) for(auto LIE =CAKE.begin(); LIE != CAKE.end(); LIE++)
#define tisic 47
#define soclose 1e-8
#define chocolate win
// so much chocolate
#define patkan 9
#define ff first
#define ss second
#define abs(x) ((x < 0)?-(x):x)
#define uint unsigned int
#define dbl long double
#define pi 3.14159265358979323846
using namespace std;
// mylittledoge

#ifdef DONLINE_JUDGE
	// palindromic tree is better than splay tree!
	#define lld I64d
#endif

string wc ="PRS";

pair<vector<int>,string> cnt(int N, int w) {
	vector<int> ret(3,0);
	string s;
	if(N == 0) {
		ret[w]++;
		s =wc[w];
		return make_pair(ret,s);}
	if(w == 0) {
		pair<vector<int>,string> x =cnt(N-1,0), y =cnt(N-1,1);
		if(x.ss > y.ss) swap(x,y);
		for(int i =0; i < 3; i++) ret[i] +=x.ff[i];
		for(int i =0; i < 3; i++) ret[i] +=y.ff[i];
		s +=x.ss+y.ss;}
	else if(w == 1) {
		pair<vector<int>,string> x =cnt(N-1,1), y =cnt(N-1,2);
		if(x.ss > y.ss) swap(x,y);
		for(int i =0; i < 3; i++) ret[i] +=x.ff[i];
		for(int i =0; i < 3; i++) ret[i] +=y.ff[i];
		s +=x.ss+y.ss;}
	else {
		pair<vector<int>,string> x =cnt(N-1,0), y =cnt(N-1,2);
		if(x.ss > y.ss) swap(x,y);
		for(int i =0; i < 3; i++) ret[i] +=x.ff[i];
		for(int i =0; i < 3; i++) ret[i] +=y.ff[i];
		s +=x.ss+y.ss;}
	return make_pair(ret,s);}

int main() {
	cin.sync_with_stdio(0);
	cin.tie(0);
	cout << fixed << setprecision(10);
	int T;
	cin >> T;
	for(int t =0; t < T; t++) {
		cout << "Case #" << t+1 << ": ";
		int N,R,P,S;
		cin >> N >> R >> P >> S;
		string ans ="IMPOSSIBLE";
		for(int w =0; w < 3; w++) {
			pair<vector<int>,string> p =cnt(N,w);
			bool ok =true;
			if(p.ff[0] != P) ok =false;
			if(p.ff[1] != R) ok =false;
			if(p.ff[2] != S) ok =false;
			if(!ok) continue;
			if(ans[0] == 'I') ans =p.ss;
			else ans =min(ans,p.ss);}
		cout << ans << "\n";}
	return 0;}

// look at my code
// my code is amazing
