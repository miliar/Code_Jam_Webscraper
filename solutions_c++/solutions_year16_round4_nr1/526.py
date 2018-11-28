#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define pii pair<int,int>
#define pll pair<ll,ll>
#define pdd pair<double,double>
#define X first
#define Y second
#define REP(i,a) for(int i=0;i<a;++i)
#define REPP(i,a,b) for(int i=a;i<b;++i)
#define FILL(a,x) memset(a,x,sizeof(a))
#define	foreach( gg,itit )	for( typeof(gg.begin()) itit=gg.begin();itit!=gg.end();itit++ )
#define	mp make_pair
#define	pb push_back
#define all(s) s.begin(),s.end()
#define present(c,x) ((c).find(x) != (c).end())
const double EPS = 1e-8;
const int mod = 1e9+7;
const int N = 1e6+10;
const ll INF = 1e18;

//#define DEBUG
ll power(ll x,ll y){
  ll t=1;
  while(y>0){
    if(y%2) y-=1,t=t*x%mod;
    else y/=2,x=x*x%mod;
  }
  return t;
}
#ifdef DEBUG
#define dprintf(fmt,...) fprintf(stderr,fmt,__VA_ARGS__)
#else
#define dprintf(fmt,...)
#endif

int check(int n,int a,int b,int c){
	if(n==0){
		return a+b+c==1;
	}
	int x=(a+b+c)/2; 
	if(a>x||b>x||c>x) return 0;
	return check(n-1,x-b,x-c,x-a);
}
string find(int n,int a,int b,int c){
	if(n==0) {
		if(a==1) return "R"; else if(b==1) return "P"; return "S";
	}
	int x=(a+b+c)/2;
	string l=find(n-1,x-b,x-c,x-a);
	string ze="";
	REP(i,l.size()) if(l[i]=='P') ze.pb('P'),ze.pb('R'); else if(l[i]=='R') ze.pb('R'),ze.pb('S'); else ze.pb('P'),ze.pb('S');
	return ze;
}
bool comp(string &a,int l1,int l2,int r){
	REP(i,r)if(a[l1+i]!=a[l2+i]){
		return a[l1+i]<a[l2+i];
	}
	return 1;
}
void doit(string &a,int l,int r){
	if(r==1) return;
	doit(a,l,r/2); doit(a,l+r/2,r/2);
	if(!comp(a,l,l+r/2,r/2)) {
		REP(i,r/2) swap(a[l+i],a[l+r/2+i]);
	}
}
string calc(int n,int a,int b,int c){
	string z=find(n,a,b,c);
	doit(z,0,z.size());
	return z;
}
int main(){
	int aa=0;
	scanf("%d",&aa);
	REP(t,aa){
		int n,a,b,c; scanf("%d%d%d%d",&n,&a,&b,&c);
		if(check(n,a,b,c)){
			printf("Case #%d: ",t+1);
			cout<<calc(n,a,b,c)<<endl;
		}else{
			printf("Case #%d: IMPOSSIBLE\n",t+1);
		}
	}
  return 0;
}
