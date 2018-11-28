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
#include <complex>

#define all(a) a.begin(),a.end()
#define sqr(a) ((a) * (a))
#define pb push_back
#define mp make_pair
#define forn(i,n) for(int i = 0; i < int(n); ++i)

using namespace std;

typedef long long li;
typedef double ld;

typedef pair<li, li> pt;
typedef complex< ld > cd;

#define ft first
#define sc second

//#define TASK_NAME x
#define _DEBUG

const int INF = 1e9;
const li INF64 = li(INF) * INF;
const ld eps = 1e-9;
const ld PI = (ld)(3.1415926535897932384626433832795);

inline int myrand(){
	return (rand() << 16) ^ rand();
}

const int N = 1e4 + 55;

int l, x;

char s[N];

bool read() {
	if(scanf("%d %d", &l, &x) != 2)
		return false;
	scanf("%s", s);
	return true;
}

int conv[5][5] = {  {0, 0,  0,  0,  0}, 
					{0, 1,  2,  3,  4}, 
					{0, 2, -1,  4, -3},
					{0, 3, -4, -1,  2},
					{0, 4,  3, -2, -1}  };

int tof[] = {2, 3, 4};

int getv(char c){
	if(c == 'i')
		return 2;
	if(c == 'j')
		return 3;
	if(c == 'k')
		return 4;
}

void solve(int test) {

	int nl = l;
	forn(i, x - 1){
		forn(j, l)
			s[nl++] = s[j];
	}

	int pos = 0;
	int cur = 1; bool ot = false;
	forn(i, nl){
		cur = conv[cur][getv(s[i])];
		if(cur < 0)
			cur = abs(cur), ot ^= true;


		if(!ot && pos < 2 && cur == tof[pos])
			pos++, cur = 1, ot = false;
	}

	if(pos == 2 && cur == tof[pos] && !ot)
		pos++;

	if(pos >= 3)
		printf("Case #%d: YES\n", test);
	else
		printf("Case #%d: NO\n", test);
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
	srand(time(NULL));

	int t;
	scanf("%d", &t);

	forn(i, t){
		read();
		solve(i + 1);
	}

	//cout << endl << clock() / (ld)CLOCKS_PER_SEC << endl;
	return 0;
}