#define _USE_MATH_DEFINES

#include <iostream>
#include <cstdio>
#include <vector>
#include <cmath>
#include <list>
#include <iomanip>
#include <stack>
#include <map>
#include <set>
#include <queue>
#include <string>
#include <algorithm>
#include <cstring>
#include <cstdlib>
#include <cassert>
#include <cstring>
#include <ctime>

#define all(a) a.begin(),a.end()
#define pb push_back
#define mp make_pair
#define forn(i,n) for(int i = 0; i < int(n); ++i)
#define sz(a) int(a.size())

using namespace std;

typedef long long li;
typedef long double ld;

typedef pair<int,int> pt;
#define ft first
#define sc second

//#define TASK_NAME "printing"
#define _DEBUG

const int INF = 1e9;
const li INF64 = li(INF) * INF;

const int N = 1005;

int n;
int a[N];

bool read() {
   if(scanf("%d", &n) != 1)
        return false;
   forn(i, n)
	   scanf("%d", &a[i]);
    return true;
}

bool dv(int seg, int mx){
	int cnt = 0;
	forn(i, n){
		cnt += a[i] / seg  + (a[i] % seg > 0) - 1;
		if(cnt > mx)
			return false;
	}

	return true;
}

inline bool can(int tm){
	bool ps = false;

	forn(k, tm){
		if(dv(tm - k, k)){
			ps = true;
			break;
		}
	}

	return ps;
}

void solve(int test) {
	int l = 0, r = 1005;
	while(r - l > 1){
		int mid = (l + r) / 2;

		if(can(mid))
			r = mid;
		else
			l = mid;
	}

	int ans = INF;
	for(int i = l; i <= r; i++){
		if(can(i)){
			ans = i;
			break;
		}
	}

	assert(ans < INF / 2);
	printf("Case #%d: %d\n", test + 1, ans);
}

int main() {
    //TASK_NAME;
#ifdef _DEBUG
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#else

#ifdef TASK_NAME
	freopen(TASK_NAME".txt", "r", stdin);
    freopen(TASK_NAME".txt", "w", stdout);
#endif

#endif

	int t;
	scanf("%d", &t);
	forn(i, t){
		read();
		solve(i);
	}
    
    return 0;
}