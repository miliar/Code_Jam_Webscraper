#include <iostream>
#include <cstdio>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
#include <vector>
#include <cmath>
#include <cstdlib>
#include <complex>

using namespace std;

#define rep(a,b,c) for(int a=b;a<=c;a++)
#define per(a,b,c) for(int a=b;a>=c;a--)
#define max(a,b) ((a>b)?(a):(b))
#define min(a,b) ((a<b)?(a):(b))
#define pb push_back
#define mp make_pair
#define PII pair<int,int>
#define X first
#define Y second

typedef long long ll;

ll n,m,T,ori,cur;
vector<pair<ll,ll> > thi;
struct H{
	ll o,e,p;
}h[100010];

struct Card{
	ll s,mu;
}te;

bool operator >(Card a,Card b){return	a.s>b.s;}
bool operator <(Card a,Card b){return	a.s<b.s;}
inline ll calc(ll s,ll t,ll p){
	return	p*(n+n-(t-s)+1)*(t-s)/2;
}

priority_queue<Card> Q;

int main(){
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	cin >>T;
	rep(vv,1,T){
		cin >>n >>m;
		ori=0;cur=0;thi.clear();
		rep(i,1,m){
			scanf("%I64d%I64d%I64d",&h[i].o,&h[i].e,&h[i].p);
			ori+=h[i].p*(n+n-(h[i].e-h[i].o)+1)*(h[i].e-h[i].o)/2;
			thi.pb(mp(h[i].o,-h[i].p));
			thi.pb(mp(h[i].e,h[i].p));
		}
		sort(thi.begin(),thi.end());
		rep(i,0,thi.size()-1){
			if	(thi[i].Y<0){
				te.s=thi[i].X;te.mu=-thi[i].Y;
				Q.push(te);
			}
			else{
				te=Q.top();Q.pop();
				while	(te.mu<thi[i].Y){
					thi[i].Y-=te.mu;
					cur+=calc(te.s,thi[i].X,te.mu);
					te=Q.top();Q.pop();
				}
				cur+=calc(te.s,thi[i].X,thi[i].Y);
				te.mu-=thi[i].Y;
				Q.push(te);
			}
		}
		cout <<"Case #" <<vv <<": " <<ori-cur <<endl;	
	}
}

