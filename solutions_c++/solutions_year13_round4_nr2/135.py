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
#define vs vector<string>
#define vpi vector<pi>
#define vpll vector<pll>
#define ALL(x) (x).begin(),(x).end()
#define Max (1<<30)
#define LLMax (1ll<<60)
template<class T>string ToString(T t){stringstream s;s<<t;return s.str();}
template<class T>void ToOther(T&t,string a){stringstream s(a);s>>t;}


#define vll vector<ll>
#define mod 1000002013
#define MAXN 200



int main(){
	freopen("input.txt","r",stdin);freopen("output.txt","w",stdout);
	int T;
	cin>>T;

	for(int test=1;test<=T;test++){

		ll n,p;
		cin>>n>>p;

		ll last=(1ll<<n);
		last-=p;

		ll cnt=0;
		for(int i=n-1;i>=0;i--)if(last>>i&1)break;
		else cnt++;
	
		ll s=0,e=(1ll<<n)-1;
		if(cnt){s=(1ll<<cnt)-1 + (1ll<<cnt)-1;}
		if(cnt==n)s=(1ll<<n)-1;

		cnt=0;
		ll now=0;
		for(int i=n-1;i>=0;i--){
			if(now>=last)break;
			now |= (1ll<<i);
			cnt++;
		}
		e-=( (1ll<<cnt) -1 );
		cout<<"Case #"<<test<<": "<<s<<" "<<e<<endl;
	}

}


