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
#define inf 100000LL

using namespace std;

long long a[N+10];

int main()
{
	freopen("B-large.in","r",stdin); freopen("1.out","w",stdout);
	int T,n;
	int i,r;
	long long m;
	long long p,q,mid,cnt;
	scanf("%d",&T);
	FOR(r,1,T){
		scanf("%d %lld",&n,&m);
		p=0LL; q=inf;
		FOR(i,0,n-1){
			scanf("%lld",&a[i]);
			q=MIN(q,a[i]);
		}
		q=m*q+1LL;
		while(p<=q){
			mid=(p+q)/2; cnt=0LL;
			FOR(i,0,n-1) cnt+=1LL+mid/a[i];
			if(cnt<m) p=mid+1LL;
			else q=mid-1LL;
		}
		printf("Case #%d: ",r);
		if(p==0LL) printf("%lld\n",m);
		else{
			cnt=0LL;
			FOR(i,0,n-1) cnt+=1LL+q/a[i];
			FOR(i,0,n-1){
				cnt+=p/a[i]-q/a[i];
				if(cnt>=m){
					printf("%d\n",i+1); break;
				} 
			}
		}
	}
	return 0;
}