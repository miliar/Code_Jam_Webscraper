#include<iostream>
#include<string>
#include<algorithm>
#include<stdio.h>
#include<queue>
#include<vector>
#include<stack>
#include<cstdlib>
#include<sstream>
#include<cassert>
#include<fstream>
#include<ctime>
#include<list>
#include<cmath>
#include<set>
#include<map>
#include<cstring>

using namespace std;

#define s(n)					scanf("%d",&n)
#define sl(n) 					scanf("%lld",&n)
#define sf(n) 					scanf("%lf",&n)
#define ss(n) 					scanf("%s",n)
#define INF						(int)1e9
#define LINF					(long long)1e18
#define EPS						1e-9
#define maX(a,b)				((a)>(b)?(a):(b))
#define miN(a,b)				((a)<(b)?(a):(b))
#define abS(x)					((x)<0?-(x):(x))
#define FOR(i,a,b)				for(int i=a;i<=b;i++)
#define rep(i,n)				FOR(i,0,n-1)
#define foreach(v,c)            for( typeof((c).begin()) v = (c).begin();  v != (c).end(); ++v)
#define mp						make_pair
#define FF						first
#define SS						second
#define XX						first
#define YY						second.first
#define ZZ						second.second
#define pb						push_back
#define fill(a,v) 				memset(a,v,sizeof(a))
#define all(x)					x.begin(),x.end()
#define sz(v)					((int)(v.size()))
#define INDEX(arr,ind)			(lower_bound(all(arr),ind)-arr.begin())

typedef long long int lli;
typedef pair<int,int> pii;
typedef pair<lli,lli> pll;
typedef vector<int> vi;
typedef vector<lli> vlli;
typedef vector<pii> vii;

const int MAXN = 2015;
const int MOD  = 1000000007;

/*Main code begins now */
int inv[MAXN],tinv[MAXN];
int inversions;
void merges(int low,int high)
{
	if(low>=high) return;
	int mid = (low+high)/2;
	merges(low,mid);
	merges(mid+1,high);

	int i = low,j=mid+1;
	int siz = low;
	while(i<=mid && j<=high)
	{
		if(inv[i] < inv[j])
			tinv[siz++] = inv[i++];
		else
		{
			tinv[siz++] = inv[j++];
			inversions+=(mid-i+1);
		}
	}
	while(i<=mid)
		tinv[siz++] = inv[i++];
	while(j<=high)
	{
		tinv[siz++] = inv[j++];
		inversions+=(mid-i+1);
	}
	FOR(i,low,high)
	{
		inv[i] = tinv[i];
	}

}
map<int,int> M;
int a[MAXN],b[MAXN],final[MAXN];
int main()
{
	int t,n;
	#ifndef ONLINE_JUDGE
	freopen("input.txt","r",stdin);
	#endif	
	s(t);
	FOR(q,1,t)
	{
		s(n);
		rep(i,n)
		s(a[i]);
		int ans  = INF;
		rep(i,n)
		b[i] = a[i];

		sort(b,b+n);
		int bitmask = 1<<(n-1);
		int maxp;
		rep(i,bitmask)
		{
			int tot = 0;
			rep(j,n-1)
				if(i&(1<<j))
					final[tot++] = b[j];
			
			maxp = tot;
			final[tot++] = b[n-1];
			rep(j,n-1)
				if(!(i&(1<<j)))
					final[tot++] = b[j];
	

			sort(final,final+maxp);
			sort(final+maxp+1,final+n);
			reverse(final+maxp+1,final+n);
			M.clear();
			
			// rep(i,n)
			// cout<<" "<<final[i];
			// cout<<endl;

			rep(i,n)
			M[final[i]] = i;
			rep(i,n)
			inv[i] = M[a[i]];
			inversions = 0;
			merges(0,n-1);
			ans  = miN(ans,inversions);
		}
		
	printf("Case #%d: %d\n",q,ans);
	}
	return 0;
}
