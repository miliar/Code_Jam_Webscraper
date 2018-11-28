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
const int Max = 10000;
int minp[Max + 1];
template <class T>
T minf(T a,T b){
	if(a<b)return a;
	else b;
}

main(){
	ll T;
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	cin>>T;
	ll C=1;
		while(T--){
			double taf,tc,c,f,x,t,tb,cc,res,res2;
			t=0;tb=0;
			cin>>c>>f>>x;
			res=10000.0;
			ll loop=50000;
			cc=2;
			while(loop--){
				tc=x/cc;
				tc=tc+tb;
				tb+=(c/cc);
				cc=cc+f;
				taf=tb+x/cc;
				if(taf<tc){
					res2=taf;
				}
				else res2=tc;
				if(res>res2)res=res2;
				//cout<<"taf"<<taf<<" tc"<<tc<<" res"<<res<<endl;
			}
			printf("Case #%d: %.7f\n",C,res);
			C++;	
		}
	}
