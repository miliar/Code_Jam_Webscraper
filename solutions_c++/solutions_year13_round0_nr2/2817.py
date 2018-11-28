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

   freopen("B-small-attempt0.in","r",stdin);
   freopen("B-small-attempt0.out","w",stdout);


	int cases;
	scanf("%d",&cases);

	REP(k, cases) {
		printf("Case #%d: ", k + 1);
		int n, m;
		scanf("%d %d", &n, &m);
		vector< vector<int> > grid;
		REP(i,n) {
			vector<int> a;
			REP(j,m) {
				int tmp;
				scanf("%d",&tmp);
				a.PB(tmp);
			}
			grid.PB(a);
		}

		int mn = grid[0][0];
		REP(i, grid.size()) {
			REP(j, grid[i].size()) {
				mn = min(grid[i][j], mn);
			}
		}

		bool valid = true;
		REP(i,grid.size()) {
			REP(j,grid[i].size()){
				int x = grid[i][j];
				if(x == mn) {
					bool found1 = true, found2 = true;
					for(int k = 0; k < grid.size(); k++) {
						if(x != grid[k][j]) {
							found1=false; break;
						}
					}

					for(int k = 0; k < grid[0].size(); k++) {
						if(x != grid[i][k]) {
							found2=false; break;
						}
					}
					if(!found1 && !found2) valid = false;
				}
				if(!valid) break;
			}
			if(!valid) break;
		}

		if(valid) printf("YES\n");
		else printf("NO\n");


	}

    return 0;
}
