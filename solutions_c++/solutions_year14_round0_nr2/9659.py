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

double C,F,X;
double time;
double cps;
double cookies;
double epsilon = 0.00000001;

void init() {	
	time = 0;
	cps = 2;
}

inline double wait() {
	return (X-C) / cps;
}

inline double buy() {
	return (X / (cps + F));
}

//cookies == C y tengo que decidir entre comprar 1 o no comprar nunca mas
inline bool sigo() {
	//cout << "wait " << wait() << endl;
	//cout << "buy " << buy() << endl;
	
	if (wait() < buy() + epsilon) {
		time += wait();
		return false;
	}
	
	cps += F;
	return true; 
}


int main () {
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
    
	ios_base::sync_with_stdio(false);
		
	int T; 
	
	 
	cin >> T;
	
	forn(caso,T) {
		
		init();
		
		cin >> C >> F >> X;
		
		if (C + epsilon > X) {
			cout << fixed << setprecision(7) << "Case #" << caso + 1 << ": " << (X / 2) << endl;
			continue;
		}
		
		time += C / cps;
		
		while(sigo()) {
			time += C / cps;			
		}
		
		cout << fixed << setprecision(7) << "Case #" << caso + 1 << ": " << time << endl;
		 
	}

  return 0;

}


