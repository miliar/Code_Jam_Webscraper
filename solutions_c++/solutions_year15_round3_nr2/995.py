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
#define tr(i,c)  for(auto i=(c).begin(); i!=(c).end(); i++)
#define rep(var,n)  for(int var=0;var<(n);var++)
#define found(s,e)  ((s).find(e)!=(s).end())

//#define DEBUG 1
//#include "cout11.h"

int main()
{
  int _T; cin >> _T; // 1-100
  for (int _t=1; _t<=_T; ++_t) {
  	int K,L,S; // 1-7 or 1-100
  	cin >> K >> L >> S;
  	string kbd; cin >> kbd;
  	string target; cin >> target;
#ifdef DEBUG
  	//printf("%d %d %d | %s | %s\n", K,L,S, kbd.c_str(), target.c_str());
#endif
  	set<char> a_;
  	map<char,int> st_;
  	rep(i,K) {
  		char ch = kbd[i];
  		a_.insert(ch);
  		st_[ch]++;
  	}
  	map<char,double> st;
  	tr(it,st_){
  		char c = it->first;
  		st[c] = log((double)it->second / K);
  	}
#ifdef DEBUG
  	//cout << st << endl;
#endif
  	vector<char> alphabet(all(a_));
  	int A = sz(alphabet);
  	queue< pair<vector<char>,double> > q;
  	q.push( make_pair(vector<char>(), 0.0) );

  	vector<pair<string,double> > words;
  	while (!q.empty()){
  		vector<char> x = q.front().first;
  		double d = q.front().second;
  		q.pop();
  		if (sz(x) == S){
  			words.pb(make_pair(string(all(x)),d));
  			continue;
  		}
  		tr(it,st){
  			char c = it->first;
  			double r = it->second;
  			x.push_back(c);
  			q.push(make_pair(x,d+r));
  			x.pop_back();
  		}
  	}

  	int max_bananas = 0;
  	int mp = S - L + 1;

  	double expected = 0;
  	tr(it,words){
  		int b = 0;
  		for (int i=0; i<mp; ++i) {
  			int m = 0;
  			for (int j=0; j<L; ++j) {
  				if (target[j] != it->first[i+j]) break;
  				++m;
  			}
  			if (m == L) ++b;
  		}
  		if (b) {
  			max_bananas = max(max_bananas, b);
  			double r = exp(it->second);
  			double e = r * b;
#ifdef DEBUG
  			printf("! %s : %g * %d = %g\n", it->first.c_str(), r,b,e);
#endif
  			expected += e;
  		}
  	}

  	// cout << alphabet << endl;

 answer:
    double ans = (double)max_bananas - expected;
    printf("Case #%d: %.7f\n", _t, ans);
  }
}
