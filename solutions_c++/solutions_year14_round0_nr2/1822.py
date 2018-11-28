#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<ctime>
#include<cmath>
#include<iostream>
#include<sstream>
#include<algorithm>
#include<vector>
#include<set>
#include<map>
#include<bitset>
#include<string>
#include<queue>
#include<iomanip>
#include<limits>
#include<typeinfo>
#include<functional>
#include<numeric>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef double ld;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef pair<ld,ld> pdd;

#define X first
#define Y second



int main()
{
	freopen("try.in","r",stdin);
	freopen("try.out","w",stdout);
	int T;
	cin>>T;
	for (int TT=1;TT<=T;++TT)
	{
		printf("Case #%d: ",TT);
		ld C,F,X;
		cin>>C>>F>>X;
		ld d=2,t=0;
		ld ans=X/2;
		for (int cnt=1;cnt<=X;++cnt)
		{
			t+=C/d;
			d+=F;
			ans=min(ans,t+X/d);
		}
		printf("%.7f\n",ans);
	}
	return 0;
}
