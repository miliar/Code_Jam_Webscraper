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
#include <complex>

using namespace std;

typedef vector<int> vi; 
typedef vector<vi> vvi;
typedef vector<string> vs;
typedef set<int> se;
typedef pair<int,int> pii;
typedef long long int tint;

#define forsn(i,s,n) for(int i = (int)(s); i<((int)n); i++)
#define dforsn(i,s,n) for(int i = (int)(n)-1; i>=((int)s); i--)
#define forn(i,n) for(int i=0;i<(int)(n);i++)
#define decl(v, c) typeof(c) v = c
#define forall(i, c) for(decl(i, c.begin()); i!=c.end(); ++i)
#define rall(c) (c).rbegin(), (c).rend()
#define all(c) (c).begin(), (c).end()
#define D(a) << #a << "=" << a << " "


#define si(a) int((a).size())
#define pb push_back
#define mp make_pair

//int M [4][4];


int main () {
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
    
	ios_base::sync_with_stdio(false);
	
	int T,f,x; 
	cin >> T;
	
	forn(caso,T) {
		
		int index;
		int tot = 0;
		
		vector<bool> may(20,false);
		
		cin >> f; f--;
		forn(i,4) forn(j,4) {
			cin >> x;
			if (i == f) may[x] = true;
		}
		
		cin >> f; f--;
		forn(i,4) forn(j,4) {
			cin >> x;
			if (i == f) 
				if (may[x]) {
					index = x;
					tot++;
				}
		}
				
		if (tot == 0) cout << "Case #" << caso + 1 << ": " << "Volunteer cheated!" << endl;
		else if (tot == 1) cout << "Case #" << caso + 1 << ": " << index << endl;
		else cout << "Case #" << caso + 1 << ": " << "Bad magician!" << endl;
		 
	}

  return 0;

}


