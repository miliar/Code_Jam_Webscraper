#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <list>
#include <vector>
#include <map>
#include <set>
#include <utility>
using namespace std;

#define MS(A)	memset(A, 0, sizeof(A))
#define REP(i ,n) for( i = 0; i < (n); i++)
#define FOR(i, a, n) for( i = a; i < n; i++)

#define MAX 1562505
#define MOD 1000000007
#define INF (int(1e9))
#define PB push_back
typedef long long int LL;
typedef vector <int> vi;

vi *v;

int main()
{
	int t,n,m,i,j,k;
	scanf("%d",&t);
	int ti;
	double c,f,x;
	REP(ti,t)
	{
		scanf("%lf%lf%lf",&c,&f,&x);
		double i=2,j,k,ans=0;
		for(;;i+=f)
		{
			j = c/i + (x/(i+f));
			k = x/i;
			if(k-j >= 0)	ans+= (c/i);
			else		
			{
				ans+= (x/i);
				break;
			}
		}
		printf("Case #%d: %0.7lf\n",ti+1,ans);
	}
	return 0;
}








