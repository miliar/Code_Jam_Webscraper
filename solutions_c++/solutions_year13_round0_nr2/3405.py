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

void test()
{
	int A[101][101];
	int Row[101]={0},Col[101]={0};;
	int n,m;
	cin>>n>>m;
	rep(i,0,n)
		rep(j,0,m)
		{
			scanf("%d",&A[i][j]);
			Row[i]=max(Row[i],A[i][j]);
			Col[j]=max(Col[j],A[i][j]);
		}
	rep(i,0,n)
		rep(j,0,m)
			if (A[i][j]<min(Row[i],Col[j]))
			{
				puts("NO");
				return;
			}
	puts("YES");
}

void run()
{
	int t;
	cin>>t;
	rep(i,0,t)
	{
		printf("Case #%d: ",i+1);
		test();
	}
}

#define problem "B-large"

int main()
{
#ifdef _DEBUG
	freopen("test.in","r",stdin);
	freopen("test.out","w",stdout);
	time_t st=clock();
#else
	freopen(problem".in","r",stdin);
	freopen(problem".out","w",stdout);
#endif
	run();
#ifdef _MONYURA_
	printf( "=============\n");
	printf("Time: %.2lf sec\n",(clock()-st)/double(CLOCKS_PER_SEC));
#endif

	return 0;
} 