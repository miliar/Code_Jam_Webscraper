//Orz Sevenkplus
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<ctime>
#include<cctype>
#include<complex>
#include<algorithm>
#include<vector>
#include<queue>
#include<set>
#include<map>
#include<bitset>
#define un using namespace
un std;
#define pb push_back
#define pf pop_front

#define mp make_pair

#define c0 first
#define c1 second
#define sqr(x)((x)*(x))
#define clr(x)memset(x,0,sizeof(x))
#define clr1(x)memset(x,-1,sizeof(x))
#define clr80(x)memset(x,0x80,sizeof(x))
#define clr7F(x)memset(x,0x7F,sizeof(x))

#define ll long long
#ifdef __unix__
#define llD "%lld"
#else
#define llD "%I64d"
#endif
#define pii pair<int,int>
#define pip pair<int,pii>
#define vi vector<int>
#define vpi vector<pii>
#define pq priority_queue

template<typename T>inline bool chkmin(T&a,T&b){return a>b?a=b,1:0;}
template<typename T>inline bool chkmax(T&a,T&b){return a<b?a=b,1:0;}
#define modadd(a,b,c)(((a)+(b))%(c))
#define modmul(a,b,c)((int)(((ll)(a)*(b))%(c)))

#define P 1000000007


const int N=int(1e6)+ 9;

ll n,p;

ll f1(){
	ll l=1,r=1LL<<n;
	while(l<r){
		ll m=l+r+1>>1,res=0,b=m-1;
		for(ll j=1;j<=n;j++){
			if(b){
                res=res<<1^1;
                --b,b/=2;
			}else res<<=1;
		}
		if(res+1<=p)l=m;
		else r=m-1;
	}
	return l-1;
}
ll f2(){
	ll l=1,r=1LL<<n;
	while(l<r){
		ll m=(l+r+1)/2,res=0,b=(1LL<<n)-m;
		for(ll j=1;j<=n;j++){
			if(b){
                res*=2;
                b-=1,b/=2;
			}else res=res<<1^1;
		}
		if(res+1<=p)l=m;
		else r=m-1;
	}
	return l-1;
}

#define getint(x){\
	char __next__char__;\
	while(!isdigit(__next__char__=getchar()));x=__next__char__-48;\
	while(isdigit(__next__char__=getchar()))x=x*10+__next__char__-48;\
}
#define getint2(x1,x2){getint(x1);getint(x2);}
#define getint3(x1,x2,x3){getint(x1);getint(x2);getint(x3);}
#define getint4(x1,x2,x3,x4){getint(x1);getint(x2);getint(x3);getint(x4);}
#define getint5(x1,x2,x3,x4,x5){getint(x1);getint(x2);getint(x3);getint(x4);getint(x5);}
#define getint6(x1,x2,x3,x4,x5,x6){getint(x1);getint(x2);getint(x3);getint(x4);getint(x5);getint(x6);}


int main(){
	int t;
	getint(t);
    for(int _=1;_<=t;_++){
        getint2(n,p); 
		printf("Case #%d: ",_);
		printf("%lld %lld\n",f1(),f2());
    }
}

