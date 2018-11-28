#include <cstdio>
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <complex>
#include <iterator>
#include <set>
#include <bitset>
#include <map>
#include <stack>
#include <list>
#include <queue>
#include <deque>

using namespace std;
typedef vector<int> VI;
typedef long long LL;
typedef vector<VI> VVI;
typedef vector<LL> VLL;
typedef vector<double> VD;
typedef vector<string> VS;
typedef pair<int, int> PII;
typedef vector<PII> VPII;
typedef long double LD;
#define FOR(x, b, e) for(int x = b; x <= (e); ++x)
#define FORD(x, b, e) for(int x = b; x >= (e); --x)
#define REP(x, n) for(int x = 0; x < (n); ++x)
#define VAR(v, n) typeof(n) v = (n)
#define ALL(c) (c).begin(), (c).end()
#define SIZE(x) ((int)(x).size())
#define FOREACH(i, c) for(VAR(i, (c).begin()); i != (c).end(); ++i)
#define PB push_back
#define ST first
#define ND second
#define MP make_pair
#define PF push_front

int t;
int k,n;
LD tab[202];
int maska;
VI zbior;
LD wyn,ans,ret;
bitset <202> v,vv;
void wyznacz()
{
	
	ret=0.0;
	
	REP(x,(1<<k))
	{
		if(__builtin_popcount(x)==(k/2))
		{
			v.reset();		
		
			maska=x;
			REP(i,k)
			{
				if(maska%2)
				{
					v[i]=1;
				}
				maska/=2;
			}
			wyn=(1.0);
			REP(i,k)
			{
				if(v[i]==1)
				{
					wyn*=(((1.0)-tab[zbior[i]]));
				}
				else
				{
					wyn*=tab[zbior[i]];
				}
			}
			ret+=wyn;
		}
	}
	ans=max(ret,ans);
}
int main()
{
	
	cin>>t;
	FOR(tt,1,t)
	{
	
		
		cin>>n>>k;
		ans=0.0;
		wyn=0.0;
		FOR(i,1,n)
		{
			cin>>tab[i];
		}
		REP(x,(1<<n))
		{
			if(__builtin_popcount(x)==k)
			{
				
				maska=x;
				zbior.clear();
				FOR(i,1,n)
				{
					if(maska%2==1)
					{
						
						zbior.PB(i);
					}
					maska/=2;
				}
				wyznacz();
			}
		}
		printf("Case #%d: ",tt);
		cout<<fixed;
		cout.precision(9);
		cout<<ans<<endl;;
	}

}






