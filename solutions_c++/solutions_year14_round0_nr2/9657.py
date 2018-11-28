#include<cstdio>
#include<iostream>
#include<cstring>
#include<string>
#include<cstdlib>
#include<cmath>
#include<cassert>
#include<ctime>
#include<algorithm>
#include<vector>
#include<stack>
#include<queue>
#include<deque>
#include<list>
#include<set>
#include<map>
using namespace std;

#define sc(x)  scanf("%c",&x)
#define si(x)  scanf("%d",&x)
#define sl(x)  scanf("%lld",&x)
#define sf(x)  scanf("%f",&x)
#define sd(x)  scanf("%lf",&x)
#define sld(x) scanf("%Lf",&x)
#define ss(x)  scanf("%s",x)
#define pc(x)  printf("%c",x)
#define pi(x)  printf("%d ",x)
#define pl(x)  printf("%lld ",x)
#define pf(x)  printf("%f ",x)
#define pd(x)  printf("%lf ",x)
#define pld(x) printf("%Lf ",x)
#define ps(x)  printf("%s ",x)
#define pin(x)  printf("%d\n",x)
#define pln(x)  printf("%lld\n",x)
#define pfn(x)  printf("%f\n",x)
#define pdn(x)  printf("%lf\n",x)
#define pldn(x) printf("%Lf\n",x)
#define psn(x)  printf("%s\n",x)
#define pn() printf("\n")
#define _p() printf(" ")
#define FOR(i,a,b) for(int i=a;i<=b;i++)
#define REP(i,n) for(int i=0;i<n;i++)
#define REV(i,a,b) for(int i=a;i>=b;i--)
#define fec(i,a) for(__typeof((a).end())i=(a).begin();i!=(a).end();++i)
#define fpc(i,j,v) for(int i=a[v],j;j=to[i],i;i=nx[i])
#define test int T;si(T);FOR(Test,1,T)
#define MEM(a,v) memset(a,v,sizeof(a))
#define MAX(x,y) (x)>(y)?(x):(y)
#define MIN(x,y) (x)<(y)?(x):(y)
#define pb push_back
#define pob pop_back
#define b() begin()
#define e() end()
#define s() size()
#define cl() clear()
#define mp make_pair
#define fi first
#define se second
#define All(X) X.b(),X.e()
#define ub upper_bound
#define lb lower_bound

#define LD long double
#define P_Q priority_queue
#define PI pair< int,int >
#define TRI pair< int,PI >
#define TR_I pair< PI,int >
#define VI vector< int >
#define VP vector< PI >
#define VT vector< TRI >
#define MI map< int,int >
#define MP map< PI,int >
#define MS map< string,int >
#define MOD 1000000009
#define SZ 400000

#define mat_mul(c,a,b,n){long long temp[10][10],k;for(int i=0;i<n;i++)for(int j=0;j<n;j++)for(k=temp[i][j]=0;k<n;k++)temp[i][j]=(temp[i][j]+a[i][k]*b[k][j])%mod;for(int i=0;i<n;i++) for(int j=0;j<n;j++)c[i][j]=temp[i][j];}
#define get getchar_unlocked
#define LL long long int
/*----------------------------------------------------------------------------*/

int main()
{
	//freopen("input.txt","r",stdin);
	//freopen("output.txt","w",stdout);
	int t,x1;
	double tim=0.0;
	double c,f,x,rate,v,a,b,a1,b1;
	cin>>t;
	x1=1;
	std::cout.precision(7);
	std::cout.setf( std::ios::fixed, std:: ios::floatfield );
	while(x1<=t)
	{
		cin>>c>>f>>x;
		
		rate=2.0;
		a=(c/rate)+(x/(rate+f));
		a1=(c/rate);
		b=(x/rate);
		b1=(c/rate);
		v=0.0;
		//std::cout.precision(10);
		while(a<b)
		{
			v=v+a1;
			rate+=f;
			b=a;
			a=v+(c/rate)+(x/(rate+f));
			a1=(c/rate);
			//b=v+(x/rate);
			if(fabs(a-b)<=0.0000001)
				break;
		}
		cout<<"Case #"<<x1<<": "<<b<<endl;
		x1++;
	}
	
	return 0;
}
