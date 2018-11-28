#include <stdio.h>
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <sstream>
#include <set>
#include <map>
#include <stack>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <string>

using namespace std;

#define ll long long
#define pi pair<int,int>
#define pll pair<ll,ll>
#define pii pair<int,pi>
#define X first
#define Y second
#define pb push_back
#define ab(x) ((x)<0?(-(x)):(x))
#define xx(x) ((x)*(x))
#define mp make_pair
#define vi vector<int>
#define vll vector<ll>
#define vs vector<string>
#define vpi vector<pi>
#define vpll vector<pll>
#define ALL(x) (x).begin(),(x).end()
#define Max (1<<30)
#define LLMax (1ll<<60)
template<class T>string ToString(T t){stringstream s;s<<t;return s.str();}
template<class T>void ToOther(T&t,string a){stringstream s(a);s>>t;}



#define mod 1000000007
#define mod2 (1ll<<55)

// cout<<"Case #"<<test<<": "<<;

ll a[50];
ll tot;
int n;

double go(int s,ll k){
	if(a[s]>k)return 0.0;
	if(s==3){
		s=s;
	}
	ll use=0;
	double cnt=37.0-(double)s;
	double r=0.0;

	for(int i=0;i<s;i++)if(a[i]<k+1)use+=(k+1-a[i]);
	for(int i=s;i<=36;i++){
		ll t=(k-a[i]);
		use+=t;
		r+=double( t*36ll )/cnt;
	}
	if(use>tot)return 0.0;
	return r-use;
}
double calc(ll k){
	
	double r=0.0;
	for(int s=0;s<=36;s++){
		r=max(r,go(s,k));
	}
	return r;
}
int main(){
	freopen("output.txt","w",stdout);freopen("input.txt","r",stdin);
	int TT;
	cin>>TT;
	for(int test=1;test<=TT;test++){

		//////////////////////////////////////////////


		cin>>tot>>n;
		memset(a,0,sizeof(a));
		for(int i=0;i<n;i++)cin>>a[i];
		sort(a,a+37,greater<ll>());

		ll s=1;
		ll e=LLMax;
		ll r=0;
		while(s<=e){
			ll m=(s+e)/2;
			ll t=tot;
			for(int i=0;i<=36;i++)if(a[i]<m){
				t-=(m-a[i]);
				if(t<0)break;
			}
			if(t>=0)r=m,s=m+1;
			else e=m-1;
		}


		double rst=0.0;

		for(ll i=max(1ll,r-10000ll);i<=r;i++){
			rst=max(rst,calc(i));
		}

		cout<<"Case #"<<test<<": ";
		printf("%.9lf\n",rst);
		//////////////////////////////////////////////
	}
}

