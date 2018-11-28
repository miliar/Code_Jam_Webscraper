#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
#include<string>
#include<queue>
#include<cmath>
#include<set>
#include<map>
#include<vector>
#include<complex>

#define fi first
#define se second
#define mp make_pair
#define pb push_back

#define REP(_a,_b,_c) for(int _a=_b,_d=_c; _a<_d; _a++)
#define REPS(_a,_b,_c) for(int _a=_b,_d=_c; _a<=_d; _a++)
#define REPD(_a,_b,_c) for(int _a=_b,_d=_c; _a>=_d; _a--)
#define REPI(it,c) for(__typeof((c).begin()) it=(c).begin(); it!=(c).end(); it++)
#define RESET(a,b) memset(a,b,sizeof(a))
#define ALL(a) a.begin(),a.end()
using namespace std;
 
typedef long long LL;
typedef pair<int,int> pii;
typedef complex<double> pt;
typedef vector<int> vi;
 
const int INF = 1000000000;
const double EPS = 1e-9;
 
//sicasli's template

int rev(int x)
{
	int ret = 0;
	while (x)
	{
		ret = ret*10 + x%10;	
		x /= 10;
	}
	return ret;	
}

bool ispal(int x)
{
	return x==rev(x);
}

bool isquare[1005];

int main()
{
	REPS(i,1,1000)
	{
		if (i*i>1000) break;
		if (ispal(i) && ispal(i*i)) isquare[i*i] = 1;	
	}
	
	int t;
	scanf("%d",&t);
	
	int cas = 0;
	
	while (t--)
	{
		int a,b;
		scanf("%d %d",&a,&b);
		
		int ans = 0;
		
		REPS(i,a,b) ans += isquare[i];
		
		printf("Case #%d: %d\n",++cas,ans);
	}
		
	return 0;
}
