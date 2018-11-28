#include <iomanip>
#include <algorithm>
#include <numeric>
#include <fstream>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <deque>
#include <list>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <cstring>
#include <complex>
#include <cassert>
#include <bitset>
using namespace std;

#define forn(i,n) for(int i=0;i<(int)(n);i++)
#define si(c) ((int)(c).size())
#define forsn(i,s,n) for(int i = (int)(s); i<((int)n); i++)
#define dforsn(i,s,n) for(int i = (int)(n)-1; i>=((int)s); i--)
#define decl(v, c) typeof(c) v = c
#define forall(i, c) for(decl(i, c.begin()); i!=c.end(); ++i)
#define dforall(i, c) for(decl(i, c.rbegin()); i!=c.rend(); ++i)
#define all(c) (c).begin(), (c).end()
#define rall(c) (c).rbegin(), (c).rend()
#define D(a) cout << #a << "=" << a << endl;
#define pb push_back
#define mp make_pair

typedef long long int tint;

int T, total, firstequal;
bool first[32];

int main () {
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	cin >> T;
	forn(caso,T) {
		total  = 0;
		firstequal = -1;
		forn(i,32) first[i] = false;
		
		int ans1; cin >> ans1;
		forn(i,4) forn(j,4) {
			int tmp; cin >> tmp;
			if (i+1 == ans1) first[tmp] = true;
		}
		
		int ans2; cin >> ans2;
		forn(i,4) forn(j,4) {
			int tmp; cin >> tmp;
			if (i+1 == ans2 && first[tmp] == true) {
				total++;
				firstequal = tmp;
			}	
		}
		cout << "Case #" << caso+1 << ": ";
		if (total == 0) cout << "Volunteer cheated!" << endl;
		else if (total == 1) cout << firstequal << endl;	
		else if (total>1) cout << "Bad magician!" << endl;
			
	
	}	



	return 0;
}
