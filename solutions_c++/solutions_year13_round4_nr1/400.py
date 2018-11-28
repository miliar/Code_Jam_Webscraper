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


struct elem
{
	int a,b;
	ll cnt;
	bool operator<(const elem &b) const
	{
		return a<b.a;
	}
};

const int mod  = 1000002013;

int N;
ll getCost(ll a)
{
	return (a*N-a*(a-1)/2)%mod;
}

ll getRes(elem *A,int n)
{
	ll res = 0;
	for (int i=0;i<n;i++)
		res+=(getCost(A[i].b-A[i].a)*A[i].cnt)%mod;
	res%=mod;
	return res;
}
typedef pair<int,long> pil;
void test()
{
	int n;
	cin>>n;
	N=n;
	int m;
	cin>>m;
	elem A[1001];
	for (int i=0;i<m;i++)
		cin>>A[i].a>>A[i].b>>A[i].cnt;
	ll res = getRes(A,m);
	pil O[1001],C[1001];
	rep(i,0,m)
	{
		O[i]=pil(A[i].a,A[i].cnt);
		C[i]=pil(A[i].b,A[i].cnt);
	}
	sort(O,O+m);
	sort(C,C+m);
	ll diff = 0;
	for (int i=0;i<m;i++)
	{
		int j = 0;
		while (j<m && O[j].first<=C[i].first)
			++j;
		for (j=j-1;j>=0;--j)
		{
			ll cnt = min(O[j].second,C[i].second);
			diff+=getCost(C[i].first-O[j].first)*cnt % mod;
			O[j].second-=cnt;
			C[i].second-=cnt;
		}
	}
	ll ans = ((res-diff)%mod + mod)%mod;
	cout<<ans<<endl;
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

#define problem "A-large"

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