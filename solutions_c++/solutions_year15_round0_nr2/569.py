#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>
#include <ctime>

#include <algorithm>
#include <iostream>
#include <string>
#include <utility>

#include <vector>
#include <stack>
#include <queue>
#include <deque>
#include <set>
#include <map>


#define FOR(i,a,b) for(i=a;i<=b;i++)
#define DEC(i,a,b) for(i=a;i>=b;i--)
#define NL printf("\n")
#define MIN(a,b) (a<b?a:b)
#define MAX(a,b) (a>b?a:b)
#define QUAD(x) (x)*(x)
#define MOD(a,b) ((a)%(b)+b)%(b)

#define VI vector<int>
#define ST stack<int>
#define QI queue<int>
#define PQ priority_queue<int>
#define DQ deque<int>
#define SI set<int>
#define PII pair<int,int>
#define LL long long
#define DB double

#define N 1000

using namespace std;

int a[N+10];

int main()
{
	freopen("B-large.in","r",stdin); freopen("1.out","w",stdout);
	int T,n;
	int i,j,k,t,h,r;
	int ans;

	scanf("%d",&T);
	FOR(r,1,T){
		ans=N;
		scanf("%d",&n);
		FOR(i,0,n-1) scanf("%d",&a[i]);
		FOR(i,1,N){
			k=0;
			FOR(j,0,n-1) k+=(a[j]-1)/i;
			ans=MIN(ans,i+k);
		}
		printf("Case #%d: %d\n",r,ans);
	}
	return 0;
}
