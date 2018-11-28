#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <queue>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <memory.h>
#include <ctime>
#include <bitset>

using namespace std;

#define ABS(a) ((a>0)?a:-(a))
#define MIN(a,b) ((a<b)?(a):(b))
#define MAX(a,b) ((a<b)?(b):(a))
#define FOR(i,a,n) for (int i=(a);i<(n);++i)
#define MEMS(a,b) memset((a),(b),sizeof(a))
#define FI(i,n) for (int i=0; i<(n); ++i)
#define pnt pair <int, int>
#define mp make_pair
#define LL long long
#define U unsigned

vector<pair<string, int> > all, nall;

int main()
{
#ifdef Fcdkbear
        freopen("in.txt", "r", stdin);
        freopen("out.txt", "w", stdout);
        double beg = clock();
#else
        freopen("in.txt", "r", stdin);
        freopen("out.txt", "w", stdout);
#endif

        int tests;
        scanf("%d",&tests);
        FOR(testNumber, 1, tests+1) {
        	all.clear();
            all.push_back(mp("P",0));
            all.push_back(mp("R",1));
            all.push_back(mp("S",2));
        	int n,r,p,s;
        	cin>>n>>r>>p>>s;
			FOR(it,1,n+1) {
				nall.clear();
				FOR(i,0,all.size()) {
					FOR(j,i+1,all.size()) {
						if ((all[i].second == all[j].second)) {
							continue;
						}
						int who = 0;
						if (all[i].second == 0) {
							if (all[j].second == 1)
								who = 0;
							else
								who = 2;
						}
						if (all[i].second == 1) {
							if (all[j].second == 2)
								who = 1;
							else
								who = 0;
						}
						if (all[i].second == 2) {
							if (all[j].second == 0)
								who = 2;
							else
								who = 1;
						}
						nall.push_back(mp(min(all[i].first + all[j].first, all[j].first + all[i].first),who));
					}
				}
				all = nall;
			}
			string res = "";
			FOR(i,0,all.size()) {
				int cntr = 0;
				int cnts = 0;
				int cntp = 0;
				FOR(j,0,all[i].first.size()) {
					if (all[i].first[j] == 'P')
						cntp++;
					if (all[i].first[j] == 'R')
											cntr++;
					if (all[i].first[j] == 'S')
											cnts++;
				}
				if ((cntp == p) && (cnts == s) && (cntr == r)) {
					if ((res>all[i].first) || (res == ""))
						res = all[i].first;
				}
			}
			printf("Case #%d: ",testNumber);
			if (res == "")
				cout<<"IMPOSSIBLE"<<endl;
			else
				cout<<res<<endl;
        }

#ifdef Fcdkbear
        double end = clock();
        fprintf(stderr, "*** Total time = %.3lf ***\n", (end - beg) / CLOCKS_PER_SEC);
#endif
        return 0;
}
