#include<iostream>
#include<algorithm>
#include<stdio.h>
#include<cstdlib>
#include<sstream>
#include<string.h>
#include<set>
#include<map>
#include<assert.h>
#include<ctime>
#include<queue>
#include<vector>
#include<stack>
#include<list>
#include<math.h>
using namespace std;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int,int> pii;
typedef long long int lli;

#define MAXN 1000005
#define INF 2147483647
#define MOD 1000000007
#define pb push_back 
#define sz(a) int((a).size())
#define FOR(x,a,b) for(int (x) = (a);(x)<=(b);(x)++)
#define rep(x,n)   for(int (x)=0;(x)<(n);(x)++)
#define tr(c,it) for(typeof((c).begin()) it = (c).begin(); it != (c).end(); it++)
#define all(c) c.begin(),c.end()
#define mset(a,b) memset(a,b,sizeof(a))

double A[1500],B[1500],C[1500];

int main()
{
	int t,n;
	int deceit,normal;
	int ans1,ans2;
	scanf("%d",&t);
	rep(q,t)
	{
		
		scanf("%d",&n);
		rep(i,n)
			scanf("%lf",&A[i]);
		rep(i,n)
			scanf("%lf",&B[i]);

		sort(A,A+n);
		sort(B,B+n);

		rep(i,n)
			C[i]=B[i];

		deceit = normal = 0;
		rep(i,n)
			rep(j,n)
				if(A[i]>B[j] && B[j]!=INF)
				{
					deceit++;
					B[j]=INF;
					j=n;
				}
		
		rep(i,n)	
			rep(j,n)
				if(A[i]<C[j] && C[j]!=INF)
				{
					normal++;
					C[j]=INF;
					j=n;
				}
		
		 ans1=deceit;
		 ans2=n-normal;
		printf("Case #%d: %d %d\n",q+1,ans1,ans2);
	}
	return 0;
}