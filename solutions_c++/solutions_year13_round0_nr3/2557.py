#include <algorithm>
#include <numeric>
#include <string>
#include <string.h>
#include <map>
#include <set>
#include <vector>
#include <queue>
#include <iostream>
#include <fstream>
#include <cmath>
#include <math.h>
#include <iomanip>
#include <stdlib.h>
#include <time.h>
#include <sstream>
#include <stdio.h>
#include <stack>

using namespace std;

#define FOR(i,n) for (int i=0; i<n; ++i)
#define FORE(i,n) for (int i=0; i<=n; ++i)
#define REP(i,a,b) for (int i=a; i<b; ++i)
#define REPE(i,a,b) for (int i=a; i<=b; ++i)
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define mp make_pair
#define INF (1e9)

typedef pair<int, int> PII;
typedef vector<PII> VPII;
typedef long long int LL;
typedef vector<int> VI;
typedef vector<bool> VB;
typedef vector<VI> VVI;
const double pi = acos(-1.0);
const int inf =(int) 1e9;

const double eps = 1e-4;
const int ss=(int)1e6+3;
const int base=inf;

bool pred (const pair<int,int>& i, const pair<int,int>& j) 
{
    if (i.first==j.first)
        return i.second>j.second;
    else
        return i.first>j.first;
}

LL out[] = {1,4,9,121,484,10201,12321,14641,40804,44944,1002001,1234321,4008004,100020001,102030201,104060401,121242121,123454321,125686521,400080004,404090404,10000200001,10221412201,12102420121,12345654321,40000800004,1000002000001,1002003002001,1004006004001,1020304030201,1022325232201,1024348434201,1210024200121,1212225222121,1214428244121,1232346432321,1234567654321,4000008000004,4004009004004};

int main()
{
#ifdef _DEBUG
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
#else
	//freopen("island2.in","r",stdin);
   //freopen("island2.out","w",stdout);
#endif
	/*vector<LL> res;
	for(int i = 1; i<10000000; ++i)
	{
		LL z = i;
		vector<LL> a;
		while(z!=0)
		{
			a.push_back(z%10);
			z/=10;
		}
		bool t = true;
		int n = a.size();
		FOR(j,n/2) {
			if (a[j]!=a[n-j-1])
			{
				t = false;
				break;
			}
		}
		if (t)
		{
			LL z = i*1ll*i;
			vector<LL> b;
			while(z!=0)
			{
				b.push_back(z%10);
				z/=10;
			}
			bool t1 = true;
			int n = b.size();
			FOR(j,n/2) {
				if (b[j]!=b[n-j-1])
				{
					t1 = false;
					break;
				}
			}
			if (t1)
			{
				res.push_back(i*1ll*i);
				cout<<res.back()<<endl;
			}
		}
	}*/
	int t;
	scanf("%d",&t);
	LL l,r;
	FOR(z,t)
	{
		scanf("%lld%lld",&l,&r);
		int ans = 0;
		FOR(i,39)
		{
			if (out[i]>=l && out[i]<=r)
				++ans;
		}
		printf("Case #%d: %d\n",z+1,ans);
	}
#ifdef _DEBUG
    fprintf(stderr, "Time: %.2lf sec\n", (clock()*1./CLOCKS_PER_SEC));
#endif
    return 0;
}

