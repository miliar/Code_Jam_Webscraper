#include <iostream>
#include <algorithm>
#include <list>
#include <cmath>
#include <vector>
#include <string>
#include <cstring>
#include <climits>
#include <cstdio>
#include <set>
#include <map>
using namespace std;

#define forn(a,n) for(int a = 0; a<(n); ++a)
#define forsn(a,s,n) for(int a = (s); a<(n); ++a)
#define forall(a,all) for(__typeof(all.begin()) a = all.begin(); a != all.end(); ++a)

typedef long long tint;

int T, m, n;

vector<string> str;

struct trie {
	map<char,trie> ady;
	trie() {ady.clear();}

	void add(const string &s, int pos) {
		if(pos == s.size()) return;
		ady[s[pos]].add(s,pos+1);
	}

	int count() {
		int ret = 1;
		forall(i, ady)
			ret += i->second.count();
		return ret;
	}
};

int arbol[16];

int make_trie(int id) {
	trie root;
	forn(i, m) if(arbol[i] == id){
		root.add(str[i], 0);
	}
	return root.count();
}

int worst, cc;

void perm(int pos) {
	if(pos == m) {
		int rr = 0;
		forn(i,n) {
			bool hayUno = false;
			forn(j,m) if(arbol[j] == i) hayUno = true;
			if(!hayUno) return;
		}
		forn(i,n) rr += make_trie(i);

		if(rr > worst) {
			worst = rr;
			cc = 1;
		} else if(rr == worst)
			cc++;
	} else {
		forn(i,n) {
			arbol[pos] = i;
			perm(pos+1);
		}
	}
}

int main(){
	freopen("D-small.in", "r", stdin);
	freopen("D-small.out", "w", stdout);

	cin >> T;

	forn(t, T) {
		cin >> m >> n;
		str.resize(m);
		forn(i,m) cin >> str[i];

		worst = -1;
		perm(0);

		printf("Case #%i: %i %i\n", t+1, worst, cc);

	}

	return 0;
}
