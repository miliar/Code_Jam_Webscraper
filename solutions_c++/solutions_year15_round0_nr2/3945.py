/* Copyright 2015 Fyodor Dmitrievich Listvin */
#include <cassert>
#include <cstdlib>
#include <ctime>
#include <cstdio>
#include <iostream>
#include <set>
#include <map>
#include <string>
using namespace std;

#define fname "pancakes"
//#define DBG
#define DB(a) #a " == " << (a) << ";	"
#define REP(n) for (int i = 0; i < (int)(n); ++i)
#define FOR(i,n) for (int i = 0; i < (int)(n); ++i)
typedef long long int lli;

map <multiset<int>, int> mem;

int state(const multiset <int> & diner, string offset = ""){
	//~ if (offset.size() >= 10) return 11011997;
	//~ cerr << offset << DB(diner.size()); for (auto & it : diner) cerr << it << ", "; cerr << endl;
	// checking memory
		if (mem.find(diner) != mem.end())
			return mem[diner];
	
	// recalling all possible actions
		multiset <int> next;
		//non-special minute
			for (auto & it : diner) if (it+1 != 0) next.insert(it+1);
			int best = state(next, offset + " ");
		//special minute
			int l = -*diner.begin(), m = l/2;
			if (l != 1){
				next = diner;
				next.erase(next.begin());
				multiset <int> copy = next;
				REP(m){
					int pass = i+1;
					next = copy;
					next.insert(-l+pass); next.insert(-pass);
					best = min(best, state(next, offset + " "));
				}
			}
			
	mem[diner] = 1+best;
	return 1+best;
}
bool init = false;
int solve(){
	multiset <int> diner;
	if (!init) mem[diner] = 0, init = true;
	int D, p;
	cin >> D;
	REP(D) cin >> p, diner.insert(-p);
	
	int t = clock(); cerr << DB(D) "complete in ...";
	int result = state(diner);
	cerr << "\b\b\b" << (clock()-t)/(CLOCKS_PER_SEC/1000) << "ms" << endl;

	return result;
}

int main(){
	#ifdef DBG
		cerr << "	DBG defined, output will appear here\n\n";
		freopen(fname".in", "r", stdin);
	#else
		{
			string fn;
			cout << "Waiting for file name with input (\"'filename' \")...\n";
			getline(cin, fn);
			if (fn != ""){
				fn = fn.substr(1,fn.size()-3);
				freopen(fn.c_str(),"r",stdin),
				freopen((fn+".out").c_str(),"w",stdout);
			}
			else{
				cerr << "	No argument, output will appear here\n\n";
				//~ freopen(fname".in", "r", stdin);
			}
		}
	#endif

	int T;
	cin >> T;
	REP(T){
		printf("Case #%d: %d\n", i+1, solve());
	}

	return 0;	
}
