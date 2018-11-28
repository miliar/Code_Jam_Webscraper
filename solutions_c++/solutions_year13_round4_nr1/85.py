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
#define LLD "%lld"
#else
#define LLD "%I64d"
#endif
#define pii pair<int,int>
#define pip pair<int,pii>
#define vi vector<int>
#define vpi vector<pii>
#define pq priority_queue
#define P 1000002013

template<typename T>inline bool chkmin(T&a,T&b){return a>b?a=b,1:0;}
template<typename T>inline bool chkmax(T&a,T&b){return a<b?a=b,1:0;}
#define modadd(a,b,c)(((a)+(b))%(c))
#define modmul(a,b,c)((int)(((ll)(a)*(b))%(c)))


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


int n,m;
ll calc(int a,int b){
	return ((ll)(b-a)*n+(ll)(b-a-1)*(b-a)/2)%P;
}
ll run(){
vector<pip>a;
	getint2(n,m);
	ll ans=0;
	for(int i=-1;++i!=m;){
		int x,y,z;
		getint3(x,y,z);
		a.pb(mp(x,mp(0,z)));
		a.pb(mp(y,mp(1,z)));
		ans=((ans-calc(x,y)*z)%P+P)%P;
	}sort(a.begin(),a.end());
	vector<pii>Q;
	for(int i=-1;++i!=a.size();){
		pip A=a[i];
		if(!A.c1.c0)Q.pb(mp(A.c0,A.c1.c1));
		else{
			while(A.c1.c1){
				if(Q.back().c1<=A.c1.c1){
					ans=(ans+calc(Q.back().c0,A.c0)*Q.back().c1)%P;
					A.c1.c1-=Q.back().c1;
					Q.pop_back();
				}else{
					ans=(ans+calc(Q.back().c0,A.c0)*A.c1.c1)%P;
					Q.back().c1-=A.c1.c1;
					A.c1.c1=0;
				}
			}
		}
	}return ans;
}
int main(){
	int t;
	getint(t);
	for(int _=1;_<=t;_++){
		printf("Case #%d: %lld\n",_,run());
	}
	return 0;
}
