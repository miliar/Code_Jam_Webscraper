#include <iostream>
#include <algorithm>
#include <vector>
#include <list>
#include <cstdio>
#include <cstring>

using namespace std;
#define REP(i,n) for(int i=0;i<(n);++i)
#define ZERO(x) memset(x,0,sizeof(x))
#define FOR(v,p,k) for(int v=p;v<k;++v)
#define FORE(v,p,k) for(int v=p;v<=k;++v)
#define FORD(v,p,k) for(int v=p;v>=k;--v)
#define FORC(i,c) for(__typeof(c.begin()) i=(c.begin());i!=(c).end();++i)
#define ALL(c) c.begin(),c.end()
//cout <<  __func__ << " : " << __LINE__ << endl;
//#define DEBUG
#ifdef DEBUG
#define D(x) x 
#else
#define D(x)
#endif


vector <int> a;
vector <int> c;
string inbuf;

int main(void)
{
	int tc, t;
	cin >> tc;
	REP(i, tc) {
		a.clear();
		c.clear();
		a.assign(26, 0);
		c.assign(10, 0);
		cin >> inbuf;
		FORC(ii, inbuf) {
			a[*ii - 'A']++;
		}
		if (a['Z'-'A']) {
			t = a['Z'-'A'];
			c[0] = t;
			a['Z'-'A']-= t;
			a['E'-'A']-= t;
			a['R'-'A']-= t;
			a['O'-'A']-= t;
		}
		if (a['W'-'A']) {
			t = a['W'-'A'];
			c[2] = t;
			a['T'-'A']-= t;
			a['W'-'A']-= t;
			a['O'-'A']-= t;
		}
		if (a['X'-'A']) {
			t = a['X'-'A'];
			c[6] = t;
			a['S'-'A']-= t;
			a['I'-'A']-= t;
			a['X'-'A']-= t;
		}
		if (a['G'-'A']) {
			t = a['G'-'A'];
			c[8] = t;
			a['E'-'A']-= t;
			a['I'-'A']-= t;
			a['G'-'A']-= t;
			a['H'-'A']-= t;
			a['T'-'A']-= t;
		}
		if (a['H'-'A']) {
			t = a['H'-'A'];
			c[3] = t;
			a['T'-'A']-= t;
			a['H'-'A']-= t;
			a['R'-'A']-= t;
			a['E'-'A']-= t;
			a['E'-'A']-= t;
		}
		if (a['R'-'A']) {
			t = a['R'-'A'];
			c[4] = t;
			a['F'-'A']-= t;
			a['O'-'A']-= t;
			a['U'-'A']-= t;
			a['R'-'A']-= t;
		}
		if (a['F'-'A']) {
			t = a['F'-'A'];
			c[5] = t;
			a['F'-'A']-= t;
			a['I'-'A']-= t;
			a['V'-'A']-= t;
			a['E'-'A']-= t;
		}
		if (a['V'-'A']) {
			t = a['V'-'A'];
			c[7] = t;
			a['S'-'A']-= t;
			a['E'-'A']-= t;
			a['V'-'A']-= t;
			a['E'-'A']-= t;
			a['N'-'A']-= t;
		}
		if (a['I'-'A']) {
			t = a['I'-'A'];
			c[9] = t;
			a['N'-'A']-= t;
			a['I'-'A']-= t;
			a['N'-'A']-= t;
			a['E'-'A']-= t;
		}
		if (a['O'-'A']) {
			t = a['O'-'A'];
			c[1] = t;
			a['O'-'A']-= t;
			a['N'-'A']-= t;
			a['E'-'A']-= t;
		}
		cout << "Case #" << i+1 << ": ";
		REP(ii, 10) {
			REP(iii, c[ii])
				cout << ii;
		}
		cout << endl;
	}
	return 0;
}
