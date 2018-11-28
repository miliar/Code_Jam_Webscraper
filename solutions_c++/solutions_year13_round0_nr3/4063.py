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
#define M 10000000
using namespace std;
typedef long long LL;
char tmp[100];
int t,ans;
LL n,m,ar[39]={1LL,4LL,9LL,121LL,484LL,10201LL,12321LL,14641LL,40804LL,44944LL,1002001LL,1234321LL,4008004LL,100020001LL,102030201LL,104060401LL,121242121LL,123454321LL,125686521LL,400080004LL,404090404LL,10000200001LL,10221412201LL,12102420121LL,12345654321LL,40000800004LL,1000002000001LL,1002003002001LL,1004006004001LL,1020304030201LL,1022325232201LL,1024348434201LL,1210024200121LL,1212225222121LL,1214428244121LL,1232346432321LL,1234567654321LL,4000008000004LL,4004009004004LL};
bool pal(LL x)
{
	sprintf(tmp,"%I64d",x);
	int len=strlen(tmp);
	REP(i,0,len-1)
		if(tmp[i] != tmp[len-1-i])
			return false;
	return true;
}

int f(LL x)
{
	int pos = upper_bound(ar,ar+39,x)-ar;
	return pos;
}
int main()
{
	//REP(i,1,M)
	//	if(pal(i) && pal((LL)i*i))
	//		printf("%I64dLL,",(LL)i*i);
	
	scanf("%d",&t);
	REP(tt,1,t)
	{
		scanf("%I64d %I64d",&n,&m);
		printf("Case #%d: %d\n",tt,f(m) - f(n-1));
	}
	return 0;
}

