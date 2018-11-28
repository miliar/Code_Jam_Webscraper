//

#include <cstdio>
#include <algorithm>
#include <cstring>
#include <utility>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <string>
#include <set>
#include <cmath>
#include <iostream>
#include <ctime>
#include <cassert>

using namespace std;

#define db(x) cout << #x " == " << x << endl
//#define _ << ", " <<
#define Fr(a,b,c) for( int a = b ; a < c ; ++a )
#define rF(a,b,c) for( int a = c-1 ; a >= b ; --a )
#define CL(a,b) memset(a,b,sizeof(a))
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> pii;
typedef vector<pair<int,int> > vpii;
typedef map<int,int> mii;
#define F first
#define S second
#define MP make_pair
#define PB push_back
#define INF 0x3f3f3f3f
#define LINF 0x3f3f3f3f3f3f3f3fLL
#define ULMAX 0xffffffffffffffffULL
#define y1 Y1

int t;
double c,f,x;

// t = x/v

// t = c/v + x/(v+f)
// t = (vc + fc + vx)/(vv + fv)

// x/v > (vc + fc + vx)/(vv + fv)	-	qual v
// vx(v+f)/v > vc + fc + vx
// xv + xf > vc + fc + vx
// vc < xf - fc
// v < xf/c - f

/*
c=500
f=4
x=2000

v < 8000/500 - 4
v < 16-4
v < 12

t = 1000
t = 250+333

t = 333
t = 83+200

t = 200
t = 50+142
---
t = 142
t = 35+111
//*/



int main() {
//	cin.sync_with_stdio(false);
	int _=1;
	for(scanf("%d",&t);t;t--){
		scanf("%lf%lf%lf",&c,&f,&x);
		double uh = x*f/c -f;
	//	printf("%lf\n",uh);
		double v = 2.0, resp=0;
		while(x/v > c/v+x/(v+f)) resp+=c/v, v+=f;
		resp += x/v;
		printf("Case #%d: %.7lf\n",_++,resp);
	}
	return 0;
}
