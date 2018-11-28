#include <iostream>
#include <vector>
#include <map>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <stack>

using namespace std ;

#define forsn(i, s, n) for (int i = s ; i < n ; i++)
#define forn(i, n) forsn(i, 0, n)
#define fore(i, n) forn(i, n.size())
#define fori(i, n) for (typeof (n.begin()) i = n.begin() ; i != n.end() ; i++)
#define all(n) n.begin(), n.end()

#define pb push_back
#define mp make_pair
#define x first
#define y second

#define dbg(x) //cout<<#x<<' '<<x<<endl;
#define RAYA //cout<<"--------------"<<endl;

#define eps 0.0001
#define INF 1000000
#define MOD 1000002013

typedef long long int  tint;

typedef pair<tint,tint> pii;

tint n;

tint f(tint dist){
	return (n*(n+1)/2 - (n-dist)*(n-dist+1)/2)%MOD;	
}


int main()
{
	freopen ("gcjA.out","w",stdout);
	int t;
	cin>>t;
	forn(caso,t){
		RAYA;
		map <tint,tint> v;
		 cin>>n;
		tint m; cin>>m;
		tint resp=0;	
		forn(i,m){
			tint o,e,p;
			cin>>o>>e>>p;
			resp+=(p*(( n*(n+1)/2-(n-e+o)*(n-e+o+1)/2)%MOD))%MOD;
			resp%=MOD;
			v[o]+=p;
			v[e]-=p;
		}
		dbg(resp)
		stack <pii> q;
		tint res=0;	
		fori(i,v){
			dbg(i->x)
			dbg(i->y)
			
			if(i->y >0){				
				q.push(mp(i->x,i->y));
			}else{
				tint bajan=-i->y;
				dbg(res)
				while(bajan>0){
					pii ahora= q.top();
					q.pop();
					tint dist= i->x - ahora.x;
					dbg(ahora.y)
					dbg(bajan)
					tint gente;
					if(bajan<ahora.y){
						gente=bajan;
						q.push(mp(ahora.x,ahora.y-bajan));
					}else{
						gente=ahora.y;
					}					
					bajan -=gente;
					dbg(dist)
					dbg(gente)
					res+=(f(dist)*gente)%MOD;
					res%=MOD;
				}				
				dbg(res)
			}
		}
		cout<<"Case #"<<caso+1<<": "<<(resp-res+MOD+MOD)%MOD<<endl;	
		
		
	}
}



