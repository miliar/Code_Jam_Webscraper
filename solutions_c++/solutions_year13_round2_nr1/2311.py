#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#define FOR(i,a,b) for(int i=(a);i<(int)(b);i++)
#define REP(i,a) for(int i=0;i<(int)(a);i++)
#define ALL(i) i.begin(),i.end()
#define rALL(i) i.rbegin(),i.rend()
#define PB push_back

typedef vector<int> vi;
typedef vector<vector<int> > vvi;

template<class T> string i2a(T x) {ostringstream oss; oss<<x; return oss.str();}

void printvec(vector<int> a)
{
 cout<<"Vecteur:  ";
 REP(i,a.size()) cout<<a[i]<<"  ";
 cout<<endl;
}

int best;
vector<int> mm;


void solve(int index, int ops, int a) {
	if(index == (int)mm.size()) {
		if(ops < best) {
			best = ops;
		}
		return;
	}
	if(a > mm[index]) {
		solve(index + 1, ops, a + mm[index]);
	} else {
		solve(index + 1, ops + 1, a);
		solve(index, ops + 1, a * 2 - 1);
	}

}


int main()
{

   freopen("A-small-attempt5.in", "r", stdin);
   freopen("A-small-attempt5.out", "w", stdout);

	int cases;
	scanf("%d",&cases);
	REP(k, cases) {
		printf("Case #%d: ", k + 1);
		int a, n;
		//vector<int> m;
		mm.clear();
		scanf("%d %d",&a, &n);
		REP(i,n) {
			int tmp; scanf("%d",&tmp);
			mm.PB(tmp);
		}
		sort(ALL(mm));
		if(a == 1) best = mm.size();
		else {
			int ops = 0;
			best = 100000;
			solve(0, ops, a);
		}


		printf("%d\n", best);

	}
    return 0;
}
