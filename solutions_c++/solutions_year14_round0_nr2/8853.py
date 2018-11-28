#include <algorithm> 
#include <iostream> 
#include <sstream> 
#include <string> 
#include <vector> 
#include <queue> 
#include <set> 
#include <map> 
#include <cstdio> 
#include <cstdlib> 
#include <cctype> 
#include <cmath> 
#include <list>
#include <cassert>
#include <conio.h>
using namespace std; 

#define PB push_back 
#define MP make_pair 
#define SZ(v) ((int)(v).size()) 
#define FOR(i,a,b) for(int i=(a);i<(b);++i) 
#define REP(i,n) FOR(i,0,n) 
#define FORE(i,a,b) for(int i=(a);i<=(b);++i) 
#define REPE(i,n) FORE(i,0,n) 
#define FORSZ(i,a,v) FOR(i,a,SZ(v)) 
#define REPSZ(i,v) REP(i,SZ(v)) 
typedef long long ll; 


int main() {
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);

	int T;	
	cin >> T;
	cin.get();
	cout.precision(7);
	REP(i, T)
	{
		//int cards[17];
		//memset(cards, 0, sizeof(int)*17);
		double c, f, x;
		cin >> c >> f >> x;
		double t1, t2;

		t1 = x/2;
		double delta = c/2;
		t2 = delta + x/(2 + f);
		int k = 1;
		while (t2 < t1) 
		{
			t1 = t2;
			delta += c/(2+k*f);
			t2 = delta + x/(2+(k+1)*f);
			++k;
		}
		cout << "Case #" << i+1 << ": " << fixed << t1 << endl;
		/*	
		t1 = x/2;
		delta = c/2;
		t2 = delta + x/(2 + f);
		k = 1;
		time = t1;
		if (t2 < time) time = t2;
		while (k <= 100000) 
		{
			t1 = t2;
			delta += c/(2+k*f);
			t2 = delta + x/(2+(k+1)*f);
			if (t2 < time) time = t2;
			++k;
		}
		cout << "Case #" << i+1 << ": " << fixed << time << " k=" << k << endl;
		*/
	}
	return 0;
}