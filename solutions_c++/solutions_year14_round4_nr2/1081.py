#include <cstdio>
#include <iostream>
#include <vector>
#include <list>
#include <queue>
#include <map>
#include <set>
#include <utility>
#include <functional>
#include <string>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cassert>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> pii;
typedef map<int,int> mii;
typedef vector<int> vi;
typedef vector< vector<int> > vvi;
typedef vector<string> vs;

#define rep(i,n) for(int i=0;i<(n);i++)
#define forup(i,a,b) for(int i=(a);i<(b);i++)
#define fordn(i,a,b) for(int i=(a);i>(b);i--)
#define all(x) x.begin(),x.end()
#define permute(x) next_permutation(all(x))
#define gi(x) scanf("%d",&x)
#define pb push_back
#define mp make_pair
#define fs first
#define sc second

struct BIT
{
	int bn; //bn>0
	vector<int> bA;
	
	BIT(){ bn=0; }
	BIT(int bn_){ bn=bn_; bA.resize(bn+1); fill(bA.begin(),bA.end(),0); }
	
	int prefix(int bposn)
	{
		if(bposn<=0) return 0;
		if(bposn>bn) bposn=bn;
		
		int ret=0;
		for(int i=bposn; i>0; i-=((i)&(-i)))
			ret+=bA[i];
		return ret;
	}
	
	void update(int bposn, int bincr)
	{
		if(bposn<=0) return;
		if(bposn>bn) return;
		
		for(int i=bposn; i<=bn; i+=((i)&(-i)))
			bA[i]+=bincr;
	}
	
	int query(int bl, int br)
	{
		if(br<=0 or bl>bn or bl>br) return 0;
		if(bl<=0) bl=1;
		if(br>bn) br=bn;
		return (prefix(br)-prefix(bl-1));
	}
};

const int max_n=1010;
int T;
int n;
int a[max_n];

int main() {
	gi(T);
	for(int z=1;z<=T;z++) {
		printf("Case #%d: ",z);
		gi(n);
		rep(i,n)
			gi(a[i]);
		int ans=(int)1e9;
		rep(mask,(1<<n)) {
			vi f,r;
			rep(i,n)
				if(mask&(1<<i)) f.pb(a[i]);
				else r.pb(a[i]);
			sort(all(f));
			sort(all(r));
			reverse(all(r));
			vi b;
			rep(i,(int)f.size()) b.pb(f[i]);
			rep(i,(int)r.size()) b.pb(r[i]);

			vi c(n);
			rep(i,n)
				rep(j,n)
					if(a[i]==b[j]) {
						c[i]=j+1;
						break;
					}
			int cnt=0;
			rep(i,n)
				rep(j,i)
					if(c[j]>c[i]) cnt++;
			ans=min(ans,cnt);
		}
		printf("%d\n",ans);
	}
	return 0;
}
