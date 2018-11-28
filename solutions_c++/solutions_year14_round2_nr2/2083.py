#include <sstream>
#include <algorithm>
#include <vector>
#include <map>
#include <queue>
#include <set>
#include <string>
#include <numeric>
#include <algorithm>

#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>
#include <limits.h>

using namespace std;

typedef long long ll;

#define mem(a,b) memset(a,b, sizeof a)
#define SZ(x)	(int)x.size()
#define FOREACH(it,x) for(__typeof((x).begin()) it=(x.begin());it!=(x.end());++it)
#define ERR 1e-7
#define PI (2.0*acos(0))
#define ALL(x) x.begin(),x.end()
#define pb push_back
#define rep(i,n,m) for(int i = (int)n,_m=(int)m;i<_m;++i)
#define bj(stat,b) (stat & (1<<b))
#define bc(stat,b) (stat & (~(1<<b)))
#define vi vector<int> 
#define vs vector<string>

template <class T> T Abs(T x) {return x<0?-x:x;}

#define MAXN 1010
int A,B,K;
int h[MAXN];
int
main()
{
	int T;
	scanf("%d\n",&T);
	for(int t=1;t<=T;t++) {
		cin>>A>>B>>K;
		mem(h,0);
		for(int a=0;a<A;a++) {
			for(int b=0;b<B;b++) {
				h[a&b]++;
			}
		}
		int ans = 0;
		for(int k=0;k<K;k++) ans += h[k];
		printf("Case #%d: %d\n", t, ans);
	}
}
