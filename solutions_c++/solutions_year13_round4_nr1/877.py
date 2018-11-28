#pragma warning(disable:4786)

#include <vector>
#include <string>
#include <map>
#include <set>
#include <cstdio>
#include <algorithm>
#include <queue>
#include <sstream>
#include <iostream>
#include <math.h>
#include <fstream>

using namespace std;

#define VT vector
typedef VT<int> VI;
typedef VT<VI> VVI;
typedef VT<string> VS;
typedef VT<double> VD;
typedef pair<int,int> PII;
#define REP(i,n) for (int i = 0; i < (n); i++)
#define ALL(c) c.begin(),c.end()
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define sz size()

ifstream ifs;
ofstream ofs;

typedef long long ll;

ll calcFee(int n, int d) {
	return ((((ll)n-d)*d) % 1000002013 + ((ll)d * (d+1)/2) % 1000002013) % 1000002013;
}

void testcase(int tst)
{
	int n, m;
	ifs >> n >> m;
	
	vector<PII> t;

	ll clean = 0;
	REP(i, m) {
		int o, e, p;
		ifs >> o >> e >> p;
		t.pb(mp(o, p));
		t.pb(mp(e, -p));
		clean += (calcFee(n, e - o) * p) % 1000002013;
	}
	sort(ALL(t));

	ll spent = 0;

	vector<PII> q;
	int oi = 0;
	REP(j, t.sz) {
		int i = t[j].fs;
		int p = t[j].sc;

		REP(l, q.sz) {
			int distance = i - oi;
			spent += (calcFee(q[l].fs, distance) * q[l].sc) % 1000002013;
			q[l].fs -= distance;
		}
		while (j+1 < t.sz && t[j+1].fs == i) {
			j++;
			p += t[j].sc;
		}
		oi = i;
		if (p > 0) {
			q.pb(mp(n, p));
		} else {
			p = -p;
			sort(ALL(q));
			int l = q.sz - 1;
			while (p > q[l].sc) {
				p -= q[l].sc;
				q.pop_back();
				l--;
			}
			q[l].sc -= p;
			if (q[l].sc == 0)
				q.pop_back();
		}
	}

	if (q.sz > 0)
		cout << "Error";

	ll result = clean - spent;
	while (result < 0)
		result += 1000002013;
	result %= 1000002013;
	ofs << "Case #" << tst+1 << ": " << result << endl;
}

int main()
{
	ifs.open("input.txt");
	ofs.open("output.txt");
	
	int t;
	ifs >> t;
	REP(tn, t)
	{
		testcase(tn);
	}

	return 0;
} 
