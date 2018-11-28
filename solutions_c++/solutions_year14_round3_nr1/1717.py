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

int
main()
{
	int T;
	ll P,Q;
	scanf("%d\n",&T);
	for(int t=1;t<=T;t++) {
		scanf("%I64d/%I64d\n", &P, &Q);
		int ans=-1;
		ll p=P;
		ll q=Q;
		bool valid1=true;
		ll q1=q;
		while(q1>1) {
			if(q1%2) {valid1=false;break;}
			q1 /= 2;
		}
		if(valid1) {
		rep(k,0,40) {
			if(2*p>=q) {ans=k;break;}
			p=p*2;
		}
		}
		if(ans==-1)

			printf("Case #%d: impossible\n", t);
		else
			{
			printf("Case #%d: ", t);
			cout<<ans+1<<endl;
			}
	}
}
