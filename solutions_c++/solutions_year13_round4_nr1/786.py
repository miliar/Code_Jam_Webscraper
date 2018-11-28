#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <queue>
#include <set>
#include <map>
using namespace std;



#define fr(i,a,b) for(int i=a;i<b;++i)
typedef long long ll;
typedef pair<int,int> pii;
#define mp make_pair
#define F first
#define S second
const ll mod = 1000002013;

int in[10010], sai[10010];
ll qtd[10010];

bool rem[10010];
struct E{
	int q,t;
	ll qg;
	bool e;
	E(){}
	E(int Q, int T, ll QG, bool En){q = Q, t = T, qg = QG, e = En; }
	bool operator <(const struct E &lhs) const{
		if(t == lhs.t){
			if(e != lhs.e) return e;
			if(in[q] == in[lhs.q]) return sai[q] < sai[lhs.q];
			return in[q] < in[lhs.q];
		}
		return t < lhs.t;
	}
}ev[1010*1010*2];
int nev;
set<E> s;



ll f(int a, int b, ll c){
	ll x = b-a;
	return (c * (((x*(x-1))/2LL)%mod))%mod;
}

int t,n,m;



int main(){
	scanf("%d",&t);
	fr(cas,1,t+1){
		nev = 0;
		s.clear();
		memset(rem, false, sizeof rem);
		scanf("%d %d",&n,&m);
		fr(i,0,m){
			int a,b;
			ll c;
			scanf("%d %d %lld",&in[i],&sai[i],&qtd[i]);
		}
		fr(i,0,m){
			fr(j,i+1,m){
				if(rem[i] || rem[j]) continue;
				if(in[i] == in[j] && sai[i] == sai[j]){
					rem[j] = true;
					qtd[i] += qtd[j];
				}
			}
		}
		int pnt = 0;
		fr(i,0,m){
			if(!rem[i]){
				in[pnt] = in[i], sai[pnt] = sai[i], qtd[pnt] = qtd[i];
				pnt++;
				
			}
		}
		m = pnt;
		fr(i,0,m){
			ev[nev++] = E(i, in[i], qtd[i], true);
			ev[nev++] = E(i, sai[i], qtd[i], false);
		}
		ll resp = 0LL;
		ll auxi = 0LL;
		fr(i,0,m){
			resp += f(in[i], sai[i], qtd[i]);
			resp %= mod;
		}
		sort(ev, ev+nev);
		fr(i,0,nev){
			if(ev[i].e){
				s.insert(ev[i]);
			}
			else{
				while(ev[i].qg){
					E aux = *(s.rbegin());
					s.erase(aux);
					ll add;
					if(aux.qg > ev[i].qg){
						aux.qg -= ev[i].qg;
						add = ev[i].qg;
						ev[i].qg = 0;
						s.insert(aux);
					}
					else if(aux.qg == ev[i].qg){
						add = ev[i].qg;
						ev[i].qg = 0;
					}
					else{
						ev[i].qg -= aux.qg;
						add = aux.qg;
					}
					auxi += f(aux.t,ev[i].t,add);
					auxi %= mod;
				}
			}
		}
		resp = (auxi - resp + mod)%mod;
		printf("Case #%d: %lld\n",cas,resp);
	}
	return 0;
}











































