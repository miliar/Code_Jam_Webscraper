#include <iostream>
#include <sstream>
#include <cstdio>
#include <climits>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <cstring>
#include <string>
#include <deque>
#include <bitset>
#include <map>
#include <set>
#include <stack>
#include <list>
#include <vector>
#include <queue>

using namespace std;

#define CLR(a) memset(a, 0, sizeof(a))
#define ABS(X) ( (X) > 0 ? (X) : ( -(X) ) )
#define SZ(V) (int )V.size()
#define ALL(V) V.begin(), V.end()
#define RALL(V) V.rbegin(), V.rend()
#define FORN(i, n) for(i = 0; i < n; i++)
#define FORAB(i, a, b) for(i = a; i <= b; i++)
#define si(n) scanf("%d",&n)
#define ss(s) scanf("%s",s)
#define prin(n) printf("%d\n",n)
#define pll pair < long long int, long long int >
#define pii pair < int, int >
#define psi pair < string, int >
#define PB push_back  
#define MP make_pair
#define F first
#define S second
#define MOD 1000000007LL
#define sieve(a) ({int b=ceil(sqrt(a));vector<int> d(a,0);vector<int> e;int f=2;e.push_back(2);e.push_back(3);for(int x=1;x<b+1;x++){for(int y=1;y<b+1;y++){int n=(4*x*x)+(y*y);if(n<=a&&(n%12==1||n%12==5)){d[n]^=1;}n=(3*x*x)+(y*y);if(n<=a&&n%12==7){d[n]^=1;}n=(3*x*x)-(y*y);if(x>y&&n<=a&&n%12==11){d[n]^=1;}}}for(int r=5;r<b+1;r++){if(d[r]){for(int i=r*r;i<a;i+=(r*r)){d[i]=0;}}}for(int c=5;c<a;c++){if(d[c]){e.push_back(c);}}e;})

typedef pair<int,int> PII;
typedef pair<double, double> PDD;
typedef long long int LL;


int main()
{
	LL T;
	double C,F,X,ans,k,check;
	cin >> T;
	for (LL t = 0; t < T; ++t)
	{
		scanf("%lf%lf%lf",&C,&F,&X);
	//	cin >> C >> F >> X;
		ans=0;
		k=2.0;
		ans+=C/k;
		check = (X/k);
		int i=0;
		k+=F;
		while(check>ans+X/k)
		{
			check = ans + X/k;
			ans+=C/k;
			k+=F;
		}
		printf("Case #%lld: %.7lf\n",t+1,check);
	}
	return 0;
}
