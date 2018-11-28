#include <cstdio>
#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <cstring>
#include <string>
#include <set>
#include <cmath>
#include <queue>
#include <stack>
#include <cstdlib>

using namespace std;

#define S(n) scanf("%d",&n)
#define P(n) printf("%d\n",n)
#define SS(str) scanf("%s",str)
#define PS(str) printf("%s\n",str)
#define SLL(n) scanf("%lld",&n)
#define PLL(n) printf("%lld\n",n)
#define PB(n) push_back(n)
#define MP(a,b) make_pair(a,b)
#define rep(i,n) for(i=0;i<n;i++)
#define rep1(i,n) for(i=1;i<=n;i++)
#define rep2(i,a,b) for(i=a;i<b;i++)
#define LL long long
#define MOD 1000000007LL
#define sortt(v) sort(v.begin(),v.end())
#define pii pair<int,int>
#define SZ(v) v.size()
#define blank printf("\n")

#define sieve(a) ({int b=ceil(sqrt(a));vector<int> d(a,0);vector<int> e;int f=2;e.push_back(2);e.push_back(3);for(int x=1;x<b+1;x++){for(int y=1;y<b+1;y++){int n=(4*x*x)+(y*y);if(n<=a&&(n%12==1||n%12==5)){d[n]^=1;}n=(3*x*x)+(y*y);if(n<=a&&n%12==7){d[n]^=1;}n=(3*x*x)-(y*y);if(x>y&&n<=a&&n%12==11){d[n]^=1;}}}for(int r=5;r<b+1;r++){if(d[r]){for(int i=r*r;i<a;i+=(r*r)){d[i]=0;}}}for(int c=5;c<a;c++){if(d[c]){e.push_back(c);}}e;})

int main()
{
	int i,j,k,l,m,n,t,u,a,b,ans;
	int A[4][4],B[4][4],count[16];
	set<int> s;
	S(t);
	rep(u,t)
	{
		rep(i,16)
			count[i] = 0;

		s.clear();
		S(a);
		rep(i,4)
			rep(j,4)
				S(A[i][j]);
		S(b);
		rep(i,4)
			rep(j,4)
				S(B[i][j]);
		rep(i,4)
		{
			s.insert(A[a-1][i]);
			count[A[a-1][i]-1]++;
		}
		
		rep(i,4)
		{
			s.insert(B[b-1][i]);
			count[B[b-1][i]-1]++;
		}


		if(s.size() == 7)
		{
			rep(i,16)
			{
				if(count[i] == 2)
				{
					ans = i+1;
					break;
				}
			}
			printf("Case #%d: %d\n",u+1,ans);
		}
		else if(s.size() == 8)
			printf("Case #%d: Volunteer cheated!\n",u+1);
		else
			printf("Case #%d: Bad magician!\n",u+1);
	}
	return 0;
}
