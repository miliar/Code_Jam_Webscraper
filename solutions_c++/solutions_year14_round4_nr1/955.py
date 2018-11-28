#include<stdio.h>
#include<string.h>
#include<math.h>
#include<ctype.h>
#include<assert.h>
#include<stdlib.h>
#include<time.h>
#include<assert.h>

#include<vector>
#include<queue>
#include<stack>
#include<map>
#include<set>
#include<iostream>
#include<algorithm>
#include<string>

using namespace std;

//#define DEBUG_MODE

#define FOR(i,n) for(int i=0;i<(n);++i)
#define REP(i,a,b) for(int i=(a);i<=(b);++i)
#define CLR(a,x) memset(a,(x),sizeof(a))

#ifdef DEBUG_MODE
#define DBG(X) X
#else
#define DBG(X)
#endif

inline int ___INT(){int ret; scanf("%d",&ret); return ret;}
#define INT ___INT()

typedef long long LL;
typedef pair<int,int> pii;
typedef vector<int> VI;

int a[10005];
bool used[10005];
int main() {
	freopen("A_large.in","r",stdin);
	freopen("A_large.out","w",stdout);

	int T=INT;
	REP(t,1,T){
		int n=INT;
		int cap=INT;
		FOR(i,n)
			a[i] = INT;
		sort(a,a+n);

		int ans = 0;

		CLR(used, 0);

		for(int i = n-1; i >= 0; --i){
			if(!used[i]){
				used[i]=1;
				++ans;
				for(int j = i-1; j >= 0; --j){
					if(!used[j] && a[i]+a[j] <= cap){
						used[j]=1;
						break;
					}
				}
			}
		}
		printf("Case #%d: %d\n",t,ans);
	}	

	return 0;
}

