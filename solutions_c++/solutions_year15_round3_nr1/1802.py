#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <bitset>
#include <cmath>
#include <numeric>
#include <iterator>
#include <iostream>
#include <cstdlib>
#include <functional>
#include <queue>
#include <stack>
using namespace std;
#define PB push_back
#define MP make_pair
#define SZ size()
#define ST begin()
#define ED end()
#define CLR clear()
#define ZERO(x) memset((x),0,sizeof(x))
typedef long long LL;
typedef unsigned long long ULL;
typedef pair<int,int> PII;
const double EPS = 1e-8;
const LL INF = 1e15+1;
const LL MAX_N = 1E14+11;

int T,R,C,W;

int f(int C,int W){
	if( C==W ) return C;
	if( W+W>C ){
		int t = C-W;
		return C-t-t+f(t+t,W-C+t+t);
	} else {
		return 1+f(C-W,W);
	}
}

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&T);
	for(int TE = 1; TE<=T; TE++){
		scanf("%d%d%d",&R,&C,&W);
		printf("Case #%d: %d\n",TE,R*f(C,W));
	}
	return 0;
}