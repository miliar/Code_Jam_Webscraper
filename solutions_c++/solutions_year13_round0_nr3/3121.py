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

int pals[10001]={0};

bool isPal(ll a)
{
	ll ten = 1;
	int cnt = 1;
	while (ten*10<=a)
	{
		ten*=10;
		++cnt;
	}
	rep(j,0,cnt/2)
		if (a/ten!=(a%10)) 
			return false;
		else
		{
			a/=10;
			ten/=10;
		}
	return true;
}
void precalc()
{
	for (int i=1;i<10001;i++)
		if (isPal(i) && isPal(ll(i)*i))
		{
			pals[i] = 1;
			//printf("%d %lld\n",i,ll(i)*i);
		}
	rep(i,1,10001)
		pals[i]+=pals[i-1];
}

int getRoot(ll a)
{
	ll sq = sqrt(double(a))+0.0005;
	while (sq*sq<a) ++sq;
	while (sq*sq>a) --sq;
	return sq;
}

int getCnt(char *A,char *B)
{
	ll a,b;
	if (strlen(A)>=6) 
		a=1000000;
	else
		sscanf(A,"%lld",&a);
	if (strlen(B)>=6)
		b=1000000;
	else
		sscanf(B,"%lld",&b);
	int fra = getRoot(a-1);
	int frb = getRoot(b);
	return pals[frb]-pals[fra];
}

char A[200],B[200];
void test()
{
	scanf(" %s %s",A,B);
	int res = getCnt(A,B);
	printf("%d\n",res);
}

void run()
{
	precalc();
	int t;
	cin>>t;
	rep(i,0,t)
	{
		printf("Case #%d: ",i+1);
		test();
	}
}

#define problem "C-small-attempt0"

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