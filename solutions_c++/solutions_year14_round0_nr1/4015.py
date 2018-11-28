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

int arr[4][4][2], ans[2];

void run() {
	F(i, 2) {
		ans[i] = in();
		F(j, 4) {
			F(k, 4) {
				arr[j][k][i] = in();
			}
		}
	}
	vi res;
	F(i, 4) {
		F(j, 4) {
			if(arr[ans[0]-1][i][0] == arr[ans[1]-1][j][1]) {
				res.PB(arr[ans[0]-1][i][0]);
			}
		}
	}
	if(res.S == 1) {
		printf("%d\n", res[0]);
	} else if(res.S == 0) {
		puts("Volunteer cheated!");
	} else {
		puts("Bad magician!");
	}
}

int main() {
	freopen("a1.in","r",stdin);
	freopen("a1.out","w",stdout);
	int t = in();
	FOR(i, 1, t+1) 
	{
		printf("Case #%d: ", i);
		run();
	}
	return 0;
}




























//Author: Gabriel Menacho                      Handle: tzyirvo.