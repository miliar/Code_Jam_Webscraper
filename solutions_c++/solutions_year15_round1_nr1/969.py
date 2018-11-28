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

#define REP(i,n) for(i=0;i<n;i++)
#define FOR(i,a,b) for(i=a;i<=b;i++)
#define DEC(i,a,b) for(i=a;i>=b;i--)
#define SKIP(i,a,b,k) for(i=a;i<=b;i+=k)
#define DEBUG printf("ok\n")
#define NL printf("\n")

#define MIN(a,b) (a<b?a:b)
#define MAX(a,b) (a>b?a:b)
#define SQR(x) (x)*(x)
#define MOD(a,b) ((a)%(b)+b)%(b)

#define N 1000
#define inf 2000000000

using namespace std;

int a[N+10];

int main()
{
	freopen("A-large.in","r",stdin); freopen("1.out","w",stdout);
	int T,n;
	int i,r;
	int ans1,ans2,maxx;
	scanf("%d",&T);
	FOR(r,1,T){
		scanf("%d",&n);
		ans1=ans2=0; maxx=0;
		FOR(i,0,n-1) scanf("%d",&a[i]);
		FOR(i,1,n-1){
			if(a[i]<a[i-1]){
				ans1+=a[i-1]-a[i];
				maxx=MAX(maxx,(a[i-1]-a[i]));
			}
		}
		FOR(i,0,n-2){
			if(a[i]<maxx) ans2+=a[i];
			else ans2+=maxx;
		}
		printf("Case #%d: %d %d\n",r,ans1,ans2);
	}
	return 0;
}