#include <iostream>
#include <ctime>
#include <fstream>
#include <cmath>
#include <cstring>
#include <cassert>
#include <cstdio>
#include <algorithm>
#include <iomanip>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <complex>
#include <utility>
#include <cctype>
#include <list>
#include <bitset>

using namespace std;

#define FORALL(i,a,b) for(int i=(a);i<=(b);++i)
#define FOR(i,n) for(int i=0;i<(n);++i)
#define FORB(i,a,b) for(int i=(a);i>=(b);--i)

typedef long long ll;
typedef long double ld;
typedef complex<ld> vec;

typedef pair<int,int> pii;
typedef map<int,int> mii;

#define pb push_back
#define mp make_pair

#define MAXN 2000
#define INF 1000000000
#define BIG 1000
int A[MAXN];

int f(int n, int b) {
	return max(0, (n-1)/b);
}

int main() {
	int TEST,N;
	scanf("%d",&TEST);
	FOR(test,TEST) {
		scanf("%d",&N);
		FOR(i,N) scanf("%d",&A[i]);
		
		int ans = INF;
		FORALL(v,1,BIG) {
			int here = v;
			FOR(i,N) here += f(A[i],v);
			ans = min(ans,here);
		}
		
		printf("Case #%d: %d\n",(test+1),ans);
	}
}















