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

int main()
{

   freopen("A-small-attempt0.in", "r", stdin);
   freopen("output.out", "w", stdout);

	int cases;
	scanf("%d",&cases);
	REP(k, cases) {
		int ans1, ans2;
		vector< vector<int> > a, b;
		scanf("%d",&ans1);
		REP(i, 4) {
			vector<int> atmp;
			REP(j, 4) {
				int tmp;
				scanf("%d",&tmp);
				atmp.PB(tmp);
			}
			a.PB(atmp);
		}

		scanf("%d",&ans2);
		REP(i, 4) {
			vector<int> atmp;
			REP(j, 4) {
				int tmp;
				scanf("%d",&tmp);
				atmp.PB(tmp);
			}
			b.PB(atmp);
		}

		vector<int> x = a[ans1 - 1], y = b[ans2 - 1];
		vector<int> match;
		REP(i, x.size()) {
			REP(j, y.size()) {
				if(x[i] == y[j]) match.PB(x[i]);
			}
		}
		printf("Case #%d: ", k + 1);
		if(match.size() == 0) printf("Volunteer cheated!");
		else if(match.size() > 1) printf("Bad magician!");
		else printf("%d", match[0]);

		printf("\n");
	}
    return 0;
}
