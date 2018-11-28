#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <limits>
#include <string>
#include <cassert>

using namespace std;
typedef long long LL;
typedef long double LD;
typedef pair<int,int> pii;

#define forup(i,a,b) for(int i=a; i<b; ++i)
#define fordn(i,a,b) for(int i=a; i>b; --i)
#define rep(i,a) for(int i=0; i<a; ++i)

#define dforup(i,a,b) for(i=a; i<b; ++i)
#define dfordn(i,a,b) for(i=a; i>b; --i)
#define drep(i,a) for(i=0; i<a; ++i)

#define slenn(s,n) for(n=0; s[n]!=13 and s[n]!=0; ++n);s[n]=0

#define gi(x) scanf("%d",&x)
#define gl(x) cin>>x
#define gd(x) scanf("%lf",&x)
#define gs(x) scanf("%s",x)

#define pis(x) printf("%d ",x)
#define pin(x) printf("%d\n",x)
#define pls(x) cout<<x<<" "
#define pln(x) cout<<x<<"\n"
#define pds(x) printf("%.15Lf ",x)
#define pdn(x) printf("%.15Lf\n",x)
#define pnl() printf("\n")

#define fs first
#define sc second

#define pb push_back

const int inv=1000000000;
const int minv=-inv;

const int max_n=1000010;

int T;
int n;
LL p,q,r,s;
LL a[max_n];
LL pa[max_n+1];
LL res;

void update(int i, int j)
{
	LL q1=pa[i];
	LL q2=pa[j]-pa[i];
	LL q3=pa[n]-pa[j];
	LL q=max(q1,max(q2,q3));
	res=min(res,q);
}

int main()
{
	gi(T);

	rep(z,T)
	{
		printf("Case #%d: ",z+1);

		gi(n); gl(p); gl(q); gl(r); gl(s);

		pa[0]=0ll;
		rep(i,n)
		{
			a[i]=((LL(i))*p+q)%r+s;
			pa[i+1]=pa[i]+a[i];
		}

		res=pa[n];
		for(int i=0; i<n; ++i)
		{
			int l=i, r=n;
			while(l+1<r) //(l,r]
			{
				int mid=(l+r)/2;
				if(pa[mid]-pa[i]>=pa[n]-pa[mid]) r=mid;
				else l=mid;
			}

			update(i,l);
			update(i,r);
		}

		LD sol=1.0L-(LD(res))/(LD(pa[n]));
		pdn(sol);
	}
	
	return 0;
}