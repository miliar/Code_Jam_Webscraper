#include<iostream>
#include<stdio.h>
#include<map>
#define fr(i,a,b) for(i=a;i<=b;i++)
typedef long long ll;
using namespace std;
const ll md=1000002013;
ll ti,ca,n,m,o,e,p,ans,mi;
map<ll,ll> in,out;
map<ll,ll>::iterator a,b;
int main(){
	freopen("a2.in","r",stdin);
	freopen("a2.out","w",stdout);
	cin>>ca;
	fr(ti,1,ca){
		cin>>n>>m;
		in.clear();
		out.clear();
		ans=0;
		while(m--){
			cin>>o>>e>>p;
			in[o]+=p;
			out[e]+=p;
			ans=(ans+(n+n+1-(e-o))*(e-o)/2%md*p)%md;
		}
		for(b=out.begin();b!=out.end();b++){
			for(a=in.begin();a!=in.end();a++)
				if(a->first>b->first)
					break;
			while(b->second>0){
				a--;
				mi=min(a->second,b->second);
				ans-=(n+n+1-(b->first-a->first))*(b->first-a->first)/2%md*mi;
				ans=(ans%md+md)%md;
				a->second-=mi;
				b->second-=mi;
			}
		}
		cout<<"Case #"<<ti<<": "<<ans<<endl;
	}
}