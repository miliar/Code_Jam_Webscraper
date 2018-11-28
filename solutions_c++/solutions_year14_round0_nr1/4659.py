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
#define ERR 1e-5
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
	int first[17];
	int second[17];
	int frow;
	int srow;
	scanf("%d\n",&T);
	for(int t=1;t<=T;t++) {
		scanf("%d",&frow);
		int tmp;
		for(int i=0;i<4;i++) {
			for(int j=0;j<4;j++) {
				scanf("%d", &tmp);
				first[tmp]=i+1;
			}
		}
		scanf("%d", &srow);
		for(int i=0;i<4;i++) {
			for(int j=0;j<4;j++) {
				scanf("%d", &tmp);
				second[tmp]=i+1;
			}
		}
		vi ans;
		for(int i=1;i<=16;i++) {
			if(first[i]==frow && second[i]==srow) ans.pb(i);
		}
		printf("Case #%d:", t);
		if(SZ(ans)==1) printf(" %d\n",ans[0]);
		else if(SZ(ans) > 1) printf(" Bad magician!\n");
		else printf(" Volunteer cheated!\n");
	}
}
