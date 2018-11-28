#include<stdio.h>
#include<iostream>
#include<vector>
#include<cmath>
#include<algorithm>
#include<memory.h>
#include<map>
#include<set>
#include<queue>
#include<list>
#include<sstream>
#define mp make_pair
#define pb push_back
#define F first
#define S second
#define SS stringstream
#define sqr(x) ((x)*(x))
#define m0(x) memset(x,0,sizeof(x))
#define m1(x) memset(x,63,sizeof(x))
#define CC(x) cout << (x) << endl
#define AL(x) x.begin(),x.end()
#define pw(x) (1ull<<(x))
#define M 1000002013
using namespace std;
typedef pair<int,int> pt;
typedef vector<int> vt;

map<int,vector<int> >e,d;
set<int>s;
set<int>::iterator it;
int n,m,x,y,p,k;
pair<int,int>g[1000111];

int main(){
	freopen("1.in","r",stdin);	
	freopen("1.out","w",stdout);	
	int T=0;
	cin >> T;
	for (int E=1;E<=T;E++){
		cin >> n >> m;
		e.clear();
		d.clear();
		s.clear();
		long long ans=0,ga=0;
		for (int i=0;i<m;i++){
			cin >> x >> y >> p;
			long long w=y-x;         	
			ga=(ga+w*(w-1)/2%M*p)%M;
			e[x].pb(p);
			d[y].pb(p);
			s.insert(x);
			s.insert(y);
		}
		int pr=-1;
		k=0;
		for (it = s.begin(); it!=s.end(); it++){
			if (pr!=-1){
				long long t=(*it)-pr;
				for (int i=0;i<k;i++) {
					ans=(ans+t*(t-1)/2%M*g[i].S)%M;
					ans=(ans+g[i].F*t%M*g[i].S)%M;
					g[i].F+=t;
				}
			}			
			pr=*it;
			vector<int>x=e[*it];
			for (int i=0; i<x.size(); i++) g[k++]=mp(0,x[i]);
			x=d[*it];
			for (int i=0;i<x.size();i++){
				int dd=x[i];
				for (int i=k-1;i>=0;i--){
					if (g[i].S>dd){
						g[i].S-=dd;
						break;
					}else{
						dd-=g[i].S;
						k--;
					}
				}
			}
		}
		ans=(ans-ga+M)%M;
		cout << "Case #" << E << ": " << ans << endl;
	}
	return 0;
}


