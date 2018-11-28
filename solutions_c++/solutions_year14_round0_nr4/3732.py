#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <cstring>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <stack>
#include <list>
#include <bitset>
#include <utility>
#include <ctime>
#include <cassert>
#include <climits>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef vector<vi> vvi;
typedef pair<int,int> pii;
typedef vector<pii > vii;
typedef pair<ll,ll> pll;
typedef vector<string> vs;

#define MOD 1000000007
#define pb push_back
#define mp make_pair
#define X first
#define Y second
#define MEM(a,b) memset(a,(b),sizeof(a))
#define pr(a) cout<<#a<<" = "<<(a)<<endl
#define cin(n) int (n); scanf("%d", &(n))
#define cin2(n,m) int (n),(m); scanf("%d%d",&(n),&(m))
#define sz(a) int((a).size())
#define all(a) a.begin(),a.end()
#define loop(x,a,b) for(int (x) = (a);(x)<(b);(x)++)
#define rep(x,n)   for(int (x)=0;(x)<(n);(x)++)
#define tr(c,it) for(typeof((c).begin()) it = (c).begin(); it != (c).end(); it++)
#define prc(a) tr(a, it) cout<<*(it)<<" "; cout<<endl
#define pra(a,n) for(int i=0; i<(n); i++) printf("%d ",((a)[i])); printf("\n") 
#define present(c,x) ((c).find(x) != (c).end()) 
#define cpresent(c,x) (find(all(c),x) != (c).end())
#define ain(a,n) double ((a)[(n)]); for(int i=0; i<(n); i++) scanf("%lf",&((a)[i])) 
#define vin(a,n) vector<int> (a); (a).resize((n)); for(int i=0; i<(n); i++) scanf("%d",&((a)[i])) 
#define TEST cin(test);	while(test--)
//#define FILE

int main()
{
	#ifdef FILE
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	#endif
	double t;
	set<double> a,b,c,d;
	int k = 0,count1,count2;
	TEST
	{
		k++;
		a.clear();
		b.clear();
		count1 = 0;
		count2 = 0;
		cin(n);
		rep(i,n)
		{
			scanf("%lf",&t);
			a.insert(t);
		}
		rep(i,n)
		{
			scanf("%lf",&t);
			b.insert(t);
		}
		c = a;
		d = b;
		rep(i,n)
		{
			if(*(--a.end()) - *(--b.end()) > 0)
			{
				a.erase(--a.end());
				b.erase(b.begin());
				count1++;
			}
			else
			{
				b.erase(b.upper_bound(*(--a.end())));
				a.erase(--a.end());
			}
		}
		a = c;
		b = d;
		rep(i,n)
		{
			if(*(--b.end()) - *(--a.end()) > 0)
			{
				b.erase(--b.end());
				a.erase(a.begin());
			}
			else
			{
				count2++;
				if(b.lower_bound(*(--a.end())) != b.begin())
					b.erase(--b.lower_bound(*(--a.end())));
				else
					b.erase(b.begin());
				a.erase(--a.end());
			}
		}
		printf("Case #%d: %d %d\n",k,count2,count1);
	}

	return 0;
}

