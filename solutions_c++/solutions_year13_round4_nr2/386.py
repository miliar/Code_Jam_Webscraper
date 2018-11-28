//#ifdef _MONYURA_
#pragma comment(linker,"/STACK:256000000")
//#endif

#include <iostream>
#include <iomanip>
#include <cstdio>
#include <bitset>
#include <memory>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <list>
#include <string>
#include <cstring>
#include <fstream>
#include <functional>
#include <stack>
#include <complex>
#include <wchar.h>
#include <wctype.h>
#include <cmath>
#include <queue>
#include <ctime>
#include <numeric>


using namespace std;

template<typename T> T mabs(const T &a){ return a<0?-a:a;}
#define rep(x,y,z) for(int x=(y),e##x=(z);x<e##x;x++)
#define SQR(x) ((x)*(x))
#define all(c) (c).begin(), (c).end()

typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;
typedef unsigned int ui;
typedef short int si;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;

const double PI = acos(-1.0);

ll getMax(ll to,int n)
{
	ll res = 0;
	for (int i=1;i<=52;i++)
	{
		ll curr = 1LL<<i;
		if (to/curr>0)
		{
			res|=1LL<<(n-i);
			to-=to%curr;
		}
	}
	return res;
}

ll rev(ll a,int n)
{
	return a^((1LL<<n)-1);
}

void test()
{
	ll n,p;
	cin>>n>>p;
	ll b = getMax(p,n);
	ll a = (1LL<<n)==p?(1LL<<n)-1 : rev(getMax((1LL<<n)-p,n),n)-1;
	cout<<a<<' '<<b<<endl;
}

void run()
{
	int t;
	cin>>t;
	rep(i,0,t)
	{
		printf("Case #%d: ",i+1);
		test();
		cerr<<i<<" done\n";
	}
}

#define problem "B-large"

int main()
{
#ifndef problem
	freopen("test.in","r",stdin);
	freopen("test.out","w",stdout);
#else
	freopen(problem".in","r",stdin);
	freopen(problem".out","w",stdout);
#endif
	time_t st=clock();
	run();
	fprintf(stderr, "=============\n");
	fprintf(stderr,"Time: %.2lf sec\n",(clock()-st)/double(CLOCKS_PER_SEC));
	return 0;
} 