//Written by technolt~h
 
#pragma comment(linker, "/STACK:16777216")
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <string>
#include <memory.h>
#include <sstream>
#include <complex>
 
#define REP(i,n) for(int i = 0, _n = (n); i < _n; i++)
#define REPD(i,n) for(int i = (n) - 1; i >= 0; i--)
#define FOR(i,a,b) for (int i = (a), _b = (b); i <= _b; i++)
#define FORD(i,a,b) for (int i = (a), _b = (b); i >= _b; i--)
#define FORN(i,a,b) for(int i=a;i<b;i++)
#define FOREACH(it,c) for (__typeof((c).begin()) it=(c).begin();it!=(c).end();it++)
#define RESET(c,x) memset (c, x, sizeof (c))
 
#define sqr(x) ((x) * (x))
#define PB push_back
#define MP make_pair
#define F first
#define S second
#define ALL(c) (c).begin(), (c).end()
#define SIZE(c) (c).size()
 
#define DEBUG(x) { cerr << #x << " = " << x << endl; }
#define PR(a,n) {cerr<<#a<<" = "; FOR(_,1,n) cerr << a[_] << ' '; cerr <<endl;}
#define PR0(a,n) {cerr<<#a<<" = ";REP(_,n) cerr << a[_] << ' '; cerr << endl;}
#define ll long long
using namespace std;
 
const double PI = 2.0 * acos (0.0);
 
typedef long long LL;
typedef pair <ll, ll> PII;
 
template <class T> inline T MAX (T a, T b) { if (a > b) return a; return b; }
template <class T> inline T MIN (T a, T b) { if (a < b) return a; return b; }

#define maxn 1111

#define base 1000002013LL

struct seg {
	ll start,finish,num;
} a[maxn];

struct point {
	ll pos,gender,num;
};

bool cmp(point a,point b) {
	if(a.pos!=b.pos) return a.pos<b.pos;
	return a.gender>b.gender;
}

ll n,m;

ll getCost(ll len) {
	return ((n+n-len)*(n-(n-len)+1)/2)%base;
}

int main() {
	freopen("a.inp","r",stdin);
	freopen("a.out","w",stdout);
	ll ntest;cin >> ntest;
	FOR(test,1,ntest) {
		cin >> n >> m;
		vector<point> list;
		
		ll res=0;
		FOR(i,1,m) {
			cin >> a[i].start >> a[i].finish >> a[i].num;
			
			point p;
			p.pos=a[i].start;
			p.gender=1;
			p.num=a[i].num;
			
			list.PB(p);
			
			p.pos=a[i].finish;
			p.gender=-1;
			p.num=a[i].num;
			
			list.PB(p);
			
			res=(res+a[i].num*getCost(a[i].finish-a[i].start))%base;
		}
		
		sort(list.begin(),list.end(),cmp);
		ll i=0;
		priority_queue<PII> heap;
		while(i<list.size()) {
			ll j=i;
			while(j<list.size() && list[i].pos==list[j].pos) {
				point p=list[j];
				if(p.gender==1) {
					heap.push(MP(p.pos,p.num));
				} else {
					ll need=p.num;
					while(need>0) {
						PII tmp=heap.top();
						heap.pop();
						
						ll used=0;
						if(tmp.S>need) {
							heap.push(MP(tmp.F,tmp.S-need));
							used=need;
							need=0;
						} else {
							need-=tmp.S;
							used=tmp.S;
						}
						
						ll len=p.pos-tmp.F;
						res=(res-used*getCost(len)%base+base)%base;
					}
				}
				j++;
			}			
			i=j;
		}
		cout << "Case #" << test << ": " << res << endl;
	}
}

