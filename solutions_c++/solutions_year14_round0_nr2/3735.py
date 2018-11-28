#include<set>
#include<map>
#include<cmath>
#include<queue>
#include<string>
#include<cstdio>
#include<vector>
#include<cassert>
#include<cstring>
#include<cstdlib>
#include<utility>
#include<iostream>
#include<algorithm>
#include<functional>
#define REP(x,y,z) for(int x=y;x<=z;x++)
#define FORD(x,y,z) for(int x=y;x>=z;x--)
#define MSET(x,y) memset(x,y,sizeof(x))
#define FOR(x,y) for(__typeof(y.begin()) x=y.begin();x!=y.end();x++)
#define F first
#define S second
#define MP make_pair
#define PB push_back
#define SZ size()
#define M 
using namespace std;
typedef long long LL;
int t;
long double cur,ans,c,f,x,spd,tmp;
int main()
{
	scanf("%d",&t);
	REP(tt,1,t)
	{
		cin >> c >> f >> x;
		
		spd=2.0;
		ans=x/spd;
		cur=0.0;
		
		while(1)
		{
			//do not build
			ans = min(ans, cur+x/spd);

			//build a farm
			tmp = c/spd;
			if(tmp + cur > ans)break;

			cur += tmp;
			spd += f;
		}

		printf("Case #%d: %.7f\n",tt, (double)ans);
	}
	return 0;
}

