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

#define EPS 1e-6
#define N 10100

int t,n;
double ns[N], ms[N];
set<double> seti;

int esperto(){
	int it1=0, ret=0;
	Fr(i,0,n){
		if(ns[i]>ms[it1]) ret++, it1++;
	}
	return ret;
}

int besta(){
	seti.clear();
	Fr(i,0,n) seti.insert(ms[i]);
	int ret=0;
	Fr(i,0,n){
		set<double>::iterator it = seti.lower_bound(ns[i]);
		if(it == seti.end()) ret++;
		else seti.erase(it);
	}
	return ret;
}

int main() {
//	cin.sync_with_stdio(false);
	int _=1;
	for(scanf("%d",&t);t;t--){
		scanf("%d",&n);
		Fr(i,0,n) scanf("%lf",&ns[i]);
		Fr(i,0,n) scanf("%lf",&ms[i]);
		sort(ns,ns+n);
		sort(ms,ms+n);
	//	Fr(i,0,n) printf("%lf ",ns[i]); puts("");
	//	Fr(i,0,n) printf("%lf ",ms[i]); puts("");
		printf("Case #%d: %d %d\n",_++,esperto(),besta());
	}
	return 0;
}
