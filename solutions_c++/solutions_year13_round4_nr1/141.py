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


struct data{
	int s,e,n;
	data(int a,int b,int c){
		s=a;
		e=b;
		n=c;
	}
	data(){}
};
int N,n;
vector<data> v;
vi x;

bool sf(data a,data b){
	return a.s<b.s;
}
bool sf2(data a,data b){
	return a.e<b.e;
}
ll cnt[2005];
ll out[2005];

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	cin>>T;

	for(int test=1;test<=T;test++){

		cin>>N>>n;
		v.clear();
		x.clear();
		memset(cnt,0,sizeof(cnt));

		ll tot=0;
		for(int i=0;i<n;i++){
			int s,e,p;
			cin>>s>>e>>p;
			v.pb(data(s,e,p));

			ll d=e-s;
			ll S=N-d+1;

			tot+= ((ll)p*( ((S+(ll)N)*d/2)%mod))%mod;
			tot%=mod;
			x.pb(s);
			x.pb(e);
		}


		sort(ALL(x));
		x.erase(unique(ALL(x)),x.end());

		int p=0;
		sort(ALL(v),sf2);
		for(int i=0;i<x.size();i++){
			int now=x[i];
			while(p<v.size() && v[p].e==now){
				out[i]+=(ll)v[p].n;
				p++;
			}
		}
		sort(ALL(v),sf);
		p=0;
		ll r=0;
		for(int i=0;i<x.size();i++){

			int now=x[i];
			while(p<v.size() && v[p].s==now){
				cnt[i]+=(ll)v[p].n;
				p++;
			}

			if(out[i]){
				for(int k=i;k>=0;k--){

					ll t=min(out[i],cnt[k]);

					ll d=x[i]-x[k];
					ll S=N-d+1;

					r+= ((ll)t%mod*( ((S+(ll)N)*d/2)%mod))%mod;
					r%=mod;


					out[i]-=t;
					cnt[k]-=t;
					if(out[i]==0)break;
				}
			}
		}
		tot=(tot-r+mod)%mod;
		cout<<"Case #"<<test<<": "<<tot<<endl;
	}

}


