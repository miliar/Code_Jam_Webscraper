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

void run() {
	double c, f, x, ans = 0.0;
	int nf = 0; //number of farms
	scanf("%lf %lf %lf", &c, &f, &x);
	while(true) {
		double secs = (2.0+(nf*1.0)*f);
		double withoutFarm = x/secs;
		double newFarm = c/secs;
		double withFarm = x/(2.0+((nf*1.0)+1.0)*f);
		if(ans+withoutFarm < ans+newFarm+withFarm) { 
			ans += withoutFarm;
			break;
		}
		//get one more farm
		ans += newFarm;
		nf++;
	}
	printf("%.7lf\n", ans);
}

int main() {
	freopen("b2.in","r",stdin);
	freopen("b2.out","w",stdout);
	int t = in();
	FOR(i, 1, t+1) 
	{
		printf("Case #%d: ", i);
		run();
	}
	return 0;
}




























//Author: Gabriel Menacho                      Handle: tzyirvo.