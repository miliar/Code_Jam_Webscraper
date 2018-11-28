#include <vector>
#include <list>
#include <queue>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <malloc.h>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cstring>
#include <cctype>
#include <cmath>
#include <cstdlib>
#include <stdint.h>
#include <unistd.h>
#include <ctime>
#include <climits>
using namespace std;
#define EPS 		1e-8
#define FOR(i,a,b)  for(int i=(a);i<(b);i++)
#define F(i,a)      FOR(i,0,a)
#define PB          push_back
#define S           size()
#define MP          make_pair
#define MS(v, x)	memset(v, x, sizeof v)
#define ALL(v)      v.begin(),v.end()
#define LLA(v)      v.rbegin(),v.rend()
#define fi          first
#define se          second
#define NL 			printf("\n")
#define SP 			system("pause")
#define foreach(IT,C) for(typeof(C.begin())IT=C.begin();IT!=C.end();IT++)
const double PI = acos(-1.0);
#define BitSet(arg,posn) ((arg) | (1L << (posn)))
#define BitClr(arg,posn) ((arg) & ~(1L << (posn)))
#define BitTst(arg,posn) bool((arg) & (1L << (posn)))
#define BitFlp(arg,posn) ((arg) ^ (1L << (posn)))
int in(){int r=0,c;for(c=getchar();c<=32;c=getchar());if(c=='-') return -in();for(;c>32;r=(r<<1)+(r<<3)+c-'0',c=getchar());return r;}
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<ii> vii;
typedef vector<string> vs;
typedef long long   LL;
#define MAXN 1010

int shyness[MAXN];

void run() {
	int s_max = in();
	int ans = 0;
	int stand = 0;
	string s;
	int len;
	cin >> s;
	len = s.S;
	MS(shyness, 0);
	F(i, len) {
		shyness[i] = s[i] - '0';
	}
	F(i, MAXN) {
		if(stand < i && shyness[i] > 0) {
			ans += (i - stand);
			stand = i;
		}
		stand += shyness[i];
	}
	printf("%d\n", ans);
}

int main() {
	freopen("a_large.in","r",stdin);
	freopen("a_large.out","w",stdout);
	int T = in();
	for(int tc = 1; tc <= T; tc++) {
		printf("Case #%d: ", tc);
		run();
	}
	return 0;
}




























//Author: Gabriel Menacho                      Handle: tzyirvo.