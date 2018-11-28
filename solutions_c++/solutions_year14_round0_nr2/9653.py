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

#define FOR(i,a,b)  for(int i=(a);i<(b);++i)
#define F(i,a)      FOR(i,0,a)
#define PB          push_back
#define MP          make_pair
#define MS(a, v)	memset(a, v, sizeof a)
#define ALL(x)      x.begin(), x.end()
#define UNIQUE(c)	(c).resize(unique(ALL(c)) - (c).begin())
#define NL 			printf("\n")
#define INF 		(1 << 28)
#define S           size()
#define T           top()
#define P           pop()
#define foreach(IT,C) for(typeof(C.begin())IT=C.begin();IT!=C.end();IT++)
#define length(x)	(sizeof(x)/sizeof(x[0]))

const double PI = acos(-1.0);
const double PI2 = 2 * acos(0.0);
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> ii;
typedef vector<ii> vii;
typedef long long   LL;

double eval(double c, double f, double x,int cf){
double res=0, pr=2;
F(i,cf){
res+=(c/pr); pr+=f;
}
res+=(x/pr);
return res;
}

int main (){
	int t,k=0;
	double c,f,x,r,a,b;
//freopen("inCookie2.txt","r",stdin);
scanf("%d", &t);
while(t--){
scanf("%lf %lf %lf",&c,&f,&x);
++k;
int ff=1;
a=x/2;
b=eval(c,f,x,ff);
while(a>b){
++ff;
a=b;
b=eval(c,f,x,ff);
}
printf("Case #%d: %.7f\n",k, a);
}

}



