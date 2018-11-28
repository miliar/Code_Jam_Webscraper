/*
@author: Ankit Srivastava
*/

#include<bits/stdc++.h>
using namespace std;
#define MOD 					1000000007
#define pb(x) 					push_back(x)
#define mp(x,y)                 make_pair(x,y)
#define FF 						first
#define SS 						second
#define s(n) 					scanf("%d",&n)
#define sl(n) 					scanf("%lld",&n)
#define sf(n) 					scanf("%lf",&n)
#define ss(n) 					scanf("%s",n)
#define sc(n)                   {char temp[4]; ss(temp); n=temp[0];}
#define INF						(int)1e9
#define LINF					(long long)1e18
#define EPS						1e-9
#define maX(a,b)				((a)>(b)?(a):(b))
#define miN(a,b)				((a)<(b)?(a):(b))
#define abS(x)					((x)<0?-(x):(x))
typedef long long ll;
typedef unsigned long long LL;
typedef pair<int,int> PII;
typedef pair<LL,LL> PLL;
typedef pair<int,PII> TRI;
typedef vector<int> VI;
typedef vector<LL> VL;
typedef vector<ll> vl;
typedef vector<PII> VII;
typedef vector<TRI> VT;

/*Main code begins now*/
int n;
int a[10004];
void precompute(){

}
void read(){
     int n,x;
     scanf("%d%d",&n,&x);
     for(int i=0;i<n;i++) scanf("%d",&a[i]);
     sort(a,a+n);
     reverse(a,a+n);
     vector<pair<int,int> > v;
     for(int b=0;b<n;b++){
         int dn=0;
         for(int i=0;i<v.size();i++){
             pair<int,int> px=v[i];
             if(px.first<2 && px.second+a[b]<=x){
                 v[i].first++;
                 v[i].second+=a[b];
                 dn=1;
                 break;
             }
         }
         pair<int,int> p=mp(1,a[b]);
         if(dn==0) v.pb(p);
         
     }
     /*for(int i=0;i<v.size();i++){
             fprintf(stderr,"%d %d %d\n",i,v[i].first,v[i].second);
         }*/
     int ans=v.size();
     int k=1;
     for(vector<pair<int,int> >::iterator it=v.begin();it!=v.end();it++){
         pair<int,int> px=*it;
         if(px.second>x){
             k=0;
         }
     }
     if(k)printf("%d\n",ans);
     assert(k);
}
void solve(){

}
int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	precompute();
	int t;
	s(t);
	for(int I=1;I<=t;I++){
	    printf("Case #%d: ",I);
	    read();
        solve();
  	}
	return 0;
}




