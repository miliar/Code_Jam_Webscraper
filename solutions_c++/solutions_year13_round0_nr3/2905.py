#include <algorithm>
#include <functional>
#include <numeric>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <cassert>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <sstream>
using namespace std;

#define LL long long
#define LD long double
#define PR pair<int,int>

#define For(i,n) for (i=0; i<int(n); i++)
#define ForR(i,n) for (i=int(n)-1; i>=0; i--)
#define Sz(s) int((s).size())
#define All(s) (s).begin(),(s).end()
#define Fill(s,v) memset(s,v,sizeof(s))
#define pb push_back
#define mp make_pair
#define x first
#define y second

template<typename T> T Abs(T x) { return(x < 0 ? -x : x); }
template<typename T> T Sqr(T x) { return(x*x); }

const int INF = (int)1e9;
const LD EPS = 1e-9;
const LD PI = acos(-1.0);

#define DEBUG 0
#define LIMN 10000001
#define LIMA 250
//long long value[LIMN];
//long long rvalue[LIMN];
int tot[LIMN];
inline long long get_reverse(long long v)
{
	long long res=0;
	while(v!=0)
	{
		long long remaind=v%10;
		v=v/10;
		res=res*10+remaind;
	}
	return res;
}
void init()
{
	tot[0]=0;
	for(int i=1;i<=1e7;i++)
	{
		tot[i]=tot[i-1];
		long long irev=get_reverse(i);
		if(irev!=i) continue;
		long long t=i*i;
		//value[i]=t;
		long long rev=get_reverse(t);
		//rvalue[i]=rev;
		
		if(t==rev){ 
			tot[i]+=1;
		};
	}
}
int get_num(long long v)
{
	long double dv=v;
	long long t=sqrt(dv);
	long long b=t-5;
	if(b<1) b=1;
	long long e=t+5;
	long long rev=0;
	for(long long mt=b; mt<e;mt++)
	{
		if(mt*mt<=v)
		{
			rev=mt;
		}
	}
	if(rev==0) assert(0);
	return tot[rev];
}
int main()
{
	//files
	freopen("in.txt","r",stdin);
		if (!DEBUG)
			freopen("out.txt","w",stdout);
	//vars
	int tt,TT;
	long long A,B;
	init();
	//testcase loop
	scanf("%d",&TT);
		For(tt,TT)
		{
			//init
			printf("Case #%d: ",tt+1);
			//input
			scanf("%lld%lld",&A,&B);
			int ans=get_num(B);
			if(A!=1) ans-=get_num(A-1);
			printf("%d\n",ans);
		}
	return(0);
}