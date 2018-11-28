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

const int INF = 1e9;
const li INF64 = li(INF) * INF;

const int N = 1041;

int n;
char s[N];

bool read() {
   if(scanf("%d", &n) != 1)
        return false;
   scanf("%s", s);
    return true;
}

void solve(int test) {
    int cnt = 0;
	int add = 0;

	forn(i, n + 1){
		if(i > cnt + add)
			add = i - cnt;
		cnt += s[i] - '0';
	}

	printf("Case #%d: %d\n", test + 1, add);
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