#include<iostream>
#include<vector>
#include<map>
#include<set>
#include<algorithm>
#include<cstdio>
#include<functional>
#include<cstdlib>
#include<ctime>
#include<cassert>
#include<iomanip>
#include<string>
#include<cstring>
#include<cctype>
#include<cmath>
 #include<iterator>
using namespace std;
typedef long long ll;
#define FRN(i,a,b) for(ll i=a;i<(ll)b;i++)
#define pb push_back
#define mp make_pair 
typedef  vector<ll> vi;
typedef  vector<vector<ll> > vvi;
typedef  vector<string> vs;
typedef  vector<double> vd;
typedef  pair<ll,ll> pi;
typedef  map<ll,ll> mii;
typedef  map<string,ll> msi;
typedef  map<ll,string> mis;
typedef  vector<pair<int,int> > vp;
typedef  set<ll> si;
typedef  set<string> ss;
typedef long long ll;

int main(){
	int T;
	freopen("B.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	cin>>T;
	ll C=1;
	while(T--){
		ll a,b,k;
		cin>>a>>b>>k;
		ll ans=0;
		for(int i=0;i<a;i++){
			for(int j=0;j<b;j++){
				if((i&j)<k)ans++;
			}
		}
			cout<<"Case #"<<C<<": "<<ans<<endl;
	C++;
	}
}

