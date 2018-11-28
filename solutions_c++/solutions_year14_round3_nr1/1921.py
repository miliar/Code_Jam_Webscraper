#include <iostream>
#include <queue>
#include <stack>
#include <vector>
#include <stdio.h>
#include <algorithm>
#include <string>
#include <cstring>
#include <cmath>
#include <complex>
#include <map>
#include <climits>
using namespace std;

#define reep(i,a,b) for(int i=(a);i<(b);++i)
#define rep(i,n) reep((i),0,(n))
#define ALL(v) (v).begin(),(v).end()
#define PB push_back
#define EPS 1e-8
#define F first
#define S second
#define mkp make_pair

static const double PI=6*asin(0.5);
typedef long long ll;
typedef complex<double> CP;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef vector<int> vint;
static const int INF=1<<24;

ll gcd( ll m, ll n )
{
	if ( ( 0 == m ) || ( 0 == n ) )
		return 0;
	
	while( m != n )
	{
		if ( m > n ) m = m - n;
		else         n = n - m;
	}
	return m;
}



int main(){
	int T;
	cin>>T;
	rep(o,T){
		printf("Case #%d: ",o+1);
		ll p,q;
		char cht;
		cin>>p>>cht>>q;
		if(p==1&&q==1){
			cout<<1<<endl;
			continue;
		}
		ll gg=gcd(p,q);
		p/=gg;
		q/=gg;
		ll t=q;
		bool f=false;
		int c=0;
		while(t){
			//cout<<t<<endl;
			c++;
			if(t==2){
				f=true;
				break;
			}
			if(t%2==1) break;
			t/=2;
		}
		//cout<<c<<endl;
		//cout<<p<<" "<<q<<endl;
		if(!f){
			cout<<"impossible\n";
			continue;
		}
		rep(i,c+1){
			//cout<<p<<" "<<q<<endl;
			if(p>=q){
				cout<<i<<endl;
				break;
			}
			else{
				q/=2;
			}
		}
		
	}
	return 0;
}
			