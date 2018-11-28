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

int n,t,a[3000],b[3000],amod[3000],bmod[3000],ans[3000];
bool found;

void find(int cnt){ 
	if (found) return;
	if (cnt>n){
		found=true;
		return;
	}
	//puts("");
	//FORU(i,0,n) printf("%d ",ans[i]); puts("");
	//FORU(i,0,n) printf("%d ",a[i]-amod[i]); puts("");
	//FORU(i,0,n) printf("%d ",b[i]-bmod[i]); puts("");
	vi pot;
	pot.clear();
	FORU(i,0,n){
		if (a[i]-amod[i]==1&&b[i]-bmod[i]==1){
			pot.pb(i);
		}
	} 
	int ta[3000],tb[3000],tans[3000];
	FORU(i,0,n){
		tans[i]=ans[i];
		ta[i]=amod[i];
		tb[i]=bmod[i];
	}
	FORU(i,0,pot.size()){
		if (found) return;
		FORU(ij,0,n){
			ans[ij]=tans[ij];
			amod[ij]=ta[ij];
			bmod[ij]=tb[ij];
		}
		ans[pot[i]]=cnt;
		FORU(j,0,pot[i]){
			bmod[j]=max(bmod[j],bmod[pot[i]]+1);
		}
		FORU(j,pot[i]+1,n){
			amod[j]=max(amod[j],amod[pot[i]]+1);
		}
		int tmpa=a[pot[i]],tmpb=b[pot[i]];
		a[pot[i]]=-100;
		b[pot[i]]=-100;
		find(cnt+1);
		a[pot[i]]=tmpa;
		b[pot[i]]=tmpb;
	}
}
int main(){
	getint(t);
	FORU(it,0,t){
		memset(ans,0,sizeof ans);
		memset(amod,0,sizeof amod);
		memset(bmod,0,sizeof bmod);
		getint(n);
		FORU(i,0,n) getint(a[i]);
		FORU(i,0,n) getint(b[i]);
		int cnt=0;
		found=false;
		find(1);
		printf("Case #%d:",it+1);
		FORU(i,0,n) printf(" %d",ans[i]);
		puts("");
		//FORU(i,0,n) printf("%d ",a[i]-amod[i]); puts("");
		//FORU(i,0,n) printf("%d ",b[i]-bmod[i]); puts("");
	}
    scanf("%d",&n);
    return(0);
}
