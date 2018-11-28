#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <cmath>
#include <map>
#include <vector>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <functional>
#include <algorithm>
#include <utility>
#include <ctime>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;

#define mp make_pair
#define pb push_back
#define pii pair<int,int>
#define pll pair<ll,ll>
#define pdd pair<double,double>
#define vi vector<int>
#define rep(i,n) for( int i = 0; i < (n); i++ )
#define forn(i,a,b) for( int i = (a); i < (b); i++ )
#define fi first
#define se second

const int MXN = 1010;
const ll modulo = 1000002013;

struct rot{
	int a,b,p;
};

struct even{
	int tp, tm, n;
	even( int tp = 0, int tm = 0, int n = 0 ):tp(tp), tm(tm), n(n){}
};

even evs [3*MXN];

bool cmp ( even a, even b ){
	if( a.tm != b.tm )
		return a.tm < b.tm;
	else return a.tp < b.tp;
}
int n;

ll cst( ll a, ll b ){

	return ((n+n-(b-a-1))*(b-a)/2) % modulo;
}

ll solve(){

	int m;
	scanf("%d%d", &n, &m);

	int a,b,p;

	int q = 0;
	ll res1 = 0;
	ll h1 = 0,h2 = 0, h11 = 0;
	rep(i,m){
		scanf("%d%d%d", &a, &b, &p);
		res1 = (res1 + p*cst(a,b) ) % modulo;

		h2+=p;
		evs[q++] = even(0,a,p);
		evs[q++] = even(1,b,p);
	}

	sort( evs, evs + q, cmp );

	multiset<pii, greater<pii> > ev;


	ll res = 0;

	rep(i,q){
		if( evs[i].tp ){
			h2 -= evs[i].n;
			for(;;){
				pii qr = *ev.begin();
				ev.erase( ev.begin() );
				h11 -= qr.second;

				if( qr.second <= evs[i].n ){
					evs[i].n -= qr.second;
					res = ( res + qr.second * cst(qr.first, evs[i].tm) ) %modulo;
					h1 -= qr.second;
				}
				else{
					qr.second -= evs[i].n;
					h1-=evs[i].n;
					res = (res + evs[i].n *  cst(qr.first, evs[i].tm) ) % modulo;
					evs[i].n = 0;
					ev.insert(qr);
					h11+=qr.second;

				}
				if( evs[i].n==0 ) break;
			}
		}
		else{
			h1+=evs[i].n;
			ev.insert( mp( evs[i].tm, evs[i].n) );
			h11 += evs[i].n;
		}
	}

	return (res1 - res + modulo) % modulo;
}

int main(){
	freopen("A.in", "r", stdin);	freopen("A.out", "w", stdout);

	int T;

	scanf("%d", &T);

	rep(i,T){
		cout<<"Case #"<<i+1<<": "<<solve()<<endl;
	}
}