/*
 * =====================================================================================
 *
 *       Filename:  Cs.cpp
 *
 *    Description:  
 *
 *        Version:  1.0
 *        Created:  2013年04月13日 10时00分48秒
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  Wang Shengyu (nbuacm09), 
 *        Company:  
 *
 * =====================================================================================
 */
#include <set>
#include <map>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <cctype>
#include <cstdio>
#include <string>
#include <vector>
#include <cassert>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
#define ll long long
using namespace std;
template<class T> T gcd(T x,T y){while(T t=x%y)x=y,y=t;return y;}
const double eps = 1e-10;
const double PI = acos(-1.);
const int INF = 1000000000;
const int MOD = 1000000007;
const double E = 2.7182818284590452353602874713527;

#define pmul(x1,y1,x2,y2) ((x1)*(x2)+(y1)*(y2))
#define xmul(x1,y1,x2,y2) ((x1)*(y2)-(x2)*(y1))
#define sqr(x) ((x)*(x))

#define FR(i,N) for(int i=0;i<N;i++)
#define _FR(i,N) for(i=0;i<N;i++)
#define FRS(i,S,E) for(int i=S;i<=E;i++)
#define _FRS(i,S,E) for(i=S;i<=E;i++)
#define FRD(i,S,E) for(int i=S;i>=E;i--)
#define _FRD(i,S,E) for(i=S;i>=E;i--)
#define SZ(x) ((int)(x).size())
#define fill(a,b) memset(a,b,sizeof(a));
#define MP(a,b) make_pair(a,b)
#define PII pair<int,int>
#define PLL pair<ll,ll>
#define fi first
#define se second
#define all(x) (x).begin(),(x).end()
#define PB push_back
#define lowbit(x) ((x)&(-(x)))

bool isdig(char x){return x>='0'&&x<='9';}
bool isup(char x){return x>='A'&&x<='Z';}
bool islow(char x){return x>='a'&&x<='z';}
bool islet(char x){return isup(x)||islow(x);}

//--------CODE----------
vector<int>od, ev;
ll get_odv(ll x){
	ll tx = x, r = 0;
	x/=10;
	while(tx){
		r = r*10+tx%10;
		tx/=10;
		x*=10;
	}
	return r + x;
}

ll get_evv(ll x){
	ll tx = x, r = 0;
	while(tx){
		r = r*10+tx%10;
		tx/=10;
		x*=10;
	}
	return r + x;
}
bool pal(int x){
	int r = 0, tx = x;
	while(x){
		r=r*10+x%10;
		x/=10;
	}
	return r == tx;
}
bool issqr(ll x){
	ll t = sqrt(x*1.);
	while((t+1)*(t+1) <= x)t++;
	return t*t == x && pal(t);
}
void pre(){
	od.clear();
	ev.clear();
	FRS(i,1,10000005){
		ll odv, evv;
		odv = get_odv(i);
		evv = get_evv(i);
		if(issqr(odv))od.PB(odv);
		if(issqr(evv))ev.PB(evv);
	}
}
ll s,e;
void get_data(){
	cin>>s>>e;
	
}
void run(){
	int r = 0;
	r += upper_bound(all(od),e) - lower_bound(all(od),s);
	r += upper_bound(all(ev),e) - lower_bound(all(ev),s);
	cout<<r<<endl;
}

int main ( int argc, char *argv[] ){
	//	get_prime();
		freopen("c1.in","r",stdin);
		freopen("output.txt","w",stdout);
	pre();
	int t,i=0;
	cin>>t;
	while(t--)
	{
		get_data();
		printf("Case #%d: ",++i);
		run();
		
	}
	return EXIT_SUCCESS;
}

