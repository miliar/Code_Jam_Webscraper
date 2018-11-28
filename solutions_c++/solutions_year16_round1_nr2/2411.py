/* DIKRA */
/* DELAPAN.3gp */
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <algorithm>
#include <utility>
#include <numeric>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cassert>
using namespace std;

#ifdef DEBUG
	#define debug(...) printf(__VA_ARGS__)
	#define GetTime() fprintf(stderr,"Running time: %.3lf second\n",((double)clock())/CLOCKS_PER_SEC)
#else
	#define debug(...) 
	#define GetTime() 
#endif

//type definitions
typedef long long ll;
typedef unsigned long long ull;
typedef double db;
typedef pair<int,int> pii;
typedef vector<int> vint;

//abbreviations
#define A first
#define B second
#define MP make_pair
#define PB push_back

//macros
#define REP(i,n) for (int i = 0; i < (n); ++i)
#define REPD(i,n) for (int i = (n)-1; 0 <= i; --i)
#define FOR(i,a,b) for (int i = (a); i <= (b); ++i)
#define FORD(i,a,b) for (int i = (a); (b) <= i; --i)
#define FORIT(it,c) for (__typeof ((c).begin()) it = (c).begin(); it != (c).end(); it++)
#define ALL(a) (a).begin(),(a).end()
#define SZ(a) ((int)(a).size())
#define RESET(a,x) memset(a,x,sizeof(a))
#define EXIST(a,s) ((s).find(a) != (s).end())
#define MX(a,b) a = max((a),(b));
#define MN(a,b) a = min((a),(b));

inline void OPEN(const string &s) {
	freopen((s + ".in").c_str(), "r", stdin);
	freopen((s + ".out").c_str(), "w", stdout);
}

/* -------------- end of DELAPAN.3gp's template -------------- */

int ntc;
int n;


map<vector<int> , int> mapToId;
vector<int> h[200];
int nh[200];
int nid;

int m;

int ans[200];

int now;
int posnow;
int found;


int n_used[200];
int blankrow;

int valid(){
	vector<int> tv(n);
	RESET(n_used, 0);

	int chance = 1;

	if (posnow == 1){
		chance = 0;
		blankrow = 0;
	}

	FOR(i, posnow+1, n-1){
		
		REP(j, n) tv[j] = h[ans[j]][i];

		if (mapToId.count(tv) <= 0){
			if (chance > 0){
				chance--;
				blankrow = i;
				continue;
			}
			return 0;
		}

		int tvid = mapToId[tv];
		n_used[tvid]++;

		if (n_used[tvid] > nh[tvid]){
			if (chance > 0){
				chance--;
				n_used[tvid]--;
				blankrow = i;
				continue;
			}
			return 0;
		}
	}

	return 1;
}

void printAns(){
	REP(j, n){
		if (j) printf(" ");
		printf("%d", h[ans[j]][blankrow]);
	}
	printf("\n");
}

void dfs(int pos){
	if (found)
		return;

	if (pos >= n){
		if (valid()){
			printAns();
			found = 1;
			return;
		}
	}

	REP(i, nid){
		if (nh[i] <= 0)
			continue;
		if (h[now][pos] != h[i][posnow])
			continue;
		ans[pos] = i;
		nh[i]--;
		dfs(pos+1);

		if (found)
			return;

		nh[i]++;
	}
}

int getId(vector<int> vv){
	if (mapToId.count(vv) > 0){
		int vvid = mapToId[vv];
		nh[vvid]++;
		return mapToId[vv];
	} else {
		int vvid = nid++;
		mapToId[vv] = vvid;
		h[vvid].clear();
		REP(i, SZ(vv)) h[vvid].PB(vv[i]);
		//h[vvid] = vv;
		nh[vvid] = 1;
		return vvid;
	}
}



int main(){
	scanf("%d", &ntc);

	FOR(itc, 1, ntc){
		scanf("%d", &n);
		printf("Case #%d: ", itc);
		m = 2*n - 1;


		REP(i, nid){
			h[i].clear();
		}
		RESET(nh, 0);
		nid = 0;
		mapToId.clear();

		REP(i, m){
			vector<int> tempv(n);

			REP(j, n){
				scanf("%d", &tempv[j]);
			}

			getId(tempv);
		}


		// DFS IF X IS ON FIRST ROW
		found = 0;
		posnow = 0;
		REP(i, nid){
			now = i;
			ans[0] = i;
			nh[i]--;
			dfs(0);
			nh[i]++;

			if (found)
				break;
		}

		if (found)
			continue;

		// DFS IF X IS ON SECOND ROW
		found = 0;
		posnow = 1;
		REP(i, nid){
			now = i;
			ans[0] = i;
			nh[i]--;
			dfs(0);
			nh[i]++;

			if (found)
				break;
		}

		assert(found > 0);
	}

	return 0;
}


