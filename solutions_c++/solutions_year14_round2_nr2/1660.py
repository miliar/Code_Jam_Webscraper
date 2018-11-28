#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <list>
#include <vector>
#include <map>
using namespace std;

#define MS(A)	memset(A, 0, sizeof(A))
#define REP(i ,n) for(i = 0; i < (n); i++)
#define FOR(i, a, n) for(i = a; i < n; i++)

#define MAX 42
#define MOD 1000000007
#define INF (int(1e9))
#define PB push_back
#define M1 102
typedef long long int LL;
typedef vector <int> vi;

vi *v;

int main()
{
	int t,i,j,k,m,n;
	int x,y,z,ti;
	scanf("%d",&t);
	REP(ti,t)
	{
		int ans=0;
		scanf("%d%d%d",&x,&y,&k);
		REP(i,x)	REP(j,y)
		{
			z = i&j;
			if(z<k)		ans++;
		}		
		printf("Case #%d: %d\n",ti+1,ans);
	}
	return 0;
}
			
