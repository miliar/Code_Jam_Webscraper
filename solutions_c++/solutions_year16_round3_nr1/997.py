/*
ID: ahri1
PROG: A
LANG: C++
*/
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <ctime>
#include <fstream>
#include <iostream>
#include <map>
#include <set>
#include <sstream>
#include <string>
#include <queue>
#include <vector>

using namespace std;

typedef long long int64;
typedef unsigned long long uint64;
#define sz(X) ((int)(X).size())
#define foreach(i,c) for(__typeof((c).begin()) i=((c).begin());i!=(c).end();++i)
#define EXISTS(x, s) ( (s).find((x)) != (s).end() ) 
template<class T> vector<T> tokenize_to(const string &str) { vector<T> r; T x; istringstream is(str); while (is >> x) r.push_back(x); return r; }
template<typename T> string v_2_s(vector<T> &a) { stringstream sb; __typeof(a.begin()) i = a.begin(); if (i!=a.end()) { sb << *i; ++i; } for (; i!=a.end();++i) { sb << " " << *i; } return sb.str(); }

struct party {
	char c;
	int count;
	party(char _c, int _count) : c(_c), count(_count) {}
	
	const bool operator<(const party &other) const {
		return count != other.count ? (count > other.count) : (c < other.c);
	}
};

void solve() {
	int N;
	cin >> N;
	int X;
	set<party> S;
	for(int i = 0; i < N; ++i){
		cin >> X;
		S.insert(party('A' + i, X));
	}
	while (!S.empty()) {
		party p = *(S.begin());			
		if (sz(S) > 1) {
			party p2 = *(++S.begin());
			if (p.count == p2.count && !(p.count == 1 && sz(S) == 3)) {
				S.erase(p2);
				S.erase(p);
				p.count--;
				p2.count--;
				if (p.count) S.insert(p);
				if (p2.count) S.insert(p2);
				cout << p.c << p2.c << " ";
				continue;
			}
		}
		S.erase(p);
		p.count--;
		if (p.count) S.insert(p);
		cout << p.c << " ";
	}
	cout << endl;

}

int main() {

  cin.sync_with_stdio(0);
  int T;
  cin >> T;
  for (int i=0;i<T;i++) {
    cout << "Case #" << i+1 << ": ";
    solve();
  }
  
  return 0;
}
