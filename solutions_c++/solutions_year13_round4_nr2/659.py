#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<cmath>
#include<algorithm>
#include<cstring>
#include<cfloat>
#include<bitset>
#include<vector>
#include<stack>
#include<queue>
#include<deque>
#include<list>
#include<set>
#include<map>
#define Joshua using
#define ganteng namespace
#define sekali std
Joshua ganteng sekali;

typedef long long			ll;
typedef long double                     ld;
typedef pair<int,int>	  	        pi;
typedef pair<ll,ll>			pl;
typedef pair<double,double>	        pd;
typedef vector<int>			vi;
typedef vector<ll>			vl;
typedef vector<pi>			vii;
typedef vector<pl>			vll;
typedef vector<pd>			vdd;
typedef vector<vi>                      vvi;
typedef vector<vl>                      vvl;

#define fi first
#define se second
#define pq priority_queue
#define SORT(a) sort(a.begin(),a.end())
#define DEBUG(a) printf("DEBUG %s\n",#a)
#define VALUE(a) printf("value of %s is %d\n",#a,a)
#define VALUELL(a) printf("value of %s is %lld\n",#a,a)
#define FORU(a,b,c) for(int a=b;a<c;++a)
#define FORD(a,b,c) for(int a=b-1;a>=c;--a)
#define MP(a,b) make_pair(a,b)
#define bikin_popcorn __builtin_popcount
#define iswhite(a) (a==' '||a=='\n')
#define pb push_back
#define pf push_front
#define db pop_back
#define df pop_front
#define PI 3.14159265
#define INF 100000000
#define MOD 1000
#define EPS 1E-9
#define MXN 1000
//#define getchar getchar_unlocked

template <class T> inline void getint(T &num)
{
	bool neg=0;
	num=0;
	char c;
	while ((c=getchar()) && (!isdigit(c) && c!='-'));
	if (c=='-'){
		neg=1;
		c=getchar();
	}
	do num=num*10+c-'0';
	while ((c=getchar()) && isdigit(c));
	num*=(neg)?-1:1;
}

int t,n,p;
int main(){
    getint(t);
    FORU(it,0,t){
		int ans1,ans2;
		getint(n); getint(p);
		int maxlim=1<<n;
		FORU(i,0,maxlim){
			int less=i, mor=maxlim-i-1;
			int tmax,worst=0,best=0;
			tmax=maxlim;
			
			//printf("%d mor %d less %d",i,mor,less);
			while (less){
				tmax/=2;
				worst+=tmax;
				--less;
				less/=2;
			}
			tmax=maxlim;
			while (mor){
				tmax/=2;
				--mor;
				mor/=2;
			}
			while (tmax){
				tmax/=2;
				best+=tmax;
			}
			if (worst<p) ans1=i;
			if (best<p) ans2=i;
			//printf("  worst %d best %d\n",worst,best);
		}	
		printf("Case #%d: ",it+1);
		printf("%d %d\n",ans1,ans2);
	}
	scanf("%d\n",&n);
	return(0);
}
