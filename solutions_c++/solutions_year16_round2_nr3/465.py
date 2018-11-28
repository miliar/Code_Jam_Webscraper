#include <iostream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <cctype>
#include <algorithm>
#include <string>
#include <vector>
#include <deque>
#include <stack>
#include <queue>
#include <list>
#include <map>
#include <set>

using namespace std;
#define sz(a)  int((a).size())
#define pb  push_back
#define all(c)  (c).begin(),(c).end()
#define tr(i,c)  for(typeof((c).begin()) i=(c).begin(); i!=(c).end(); i++)
#define rep(var,n)  for(int var=0;var<(n);var++)
#define found(s,e)  ((s).find(e)!=(s).end())

// #include "cout.h"

int solve(vector<string>& w1, vector<string>& w2) {
	int N = w1.size(); // 1-16
	int P = 1 << N;

	int max_fake = 0;
	rep(p,P) {
		set<string> s1, s2;
		set<int> cand;
		for (int i=0,m=1; i<N; ++i,m<<=1) {
			if (p & m) {
				s1.insert(w1[i]);
				s2.insert(w2[i]);
			} else {
				cand.insert(i);
			}
		}
		int fake = 0;
		tr(it,cand) {
			int i=*it;
			if (found(s1, w1[i]) && found(s2, w2[i])) ++fake;
			else { fake = -1; break; }
		}
		if (fake > max_fake) max_fake = fake;
	}
	return max_fake;
}

int main(){
  int _T; cin>>_T; // 1-100
  rep(_t,_T){
  	int N; cin>>N;
  	vector<string> w1(N), w2(N);
  	rep(i,N){
  		cin >> w1[i] >> w2[i];
  	}

 answer:
    cout << "Case #" << (1+_t) << ": " << solve(w1,w2) << endl;
  }
}
