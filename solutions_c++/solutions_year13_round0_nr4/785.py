#include <iostream>
#include <algorithm>
#include <string>
#include <map>
#include <math.h>
#include <fstream>
using namespace std;
#define fon(i,n) for(i=0;i<n;++i)
#define re return
#define ll long long
const double EPS = 1E-9;const int INF = 1000000000;const ll INF64 = (ll)1E18;const double PI = 3.1415926535897932384626433832795;

const int MAXN = 20,MAXK=41;

typedef struct{int keys[MAXK],t;}tpo;
tpo all[200];ll n;

typedef struct {//unsigned int h[(MAXN>>5)+1];
unsigned int h[1];}cont;
typedef struct {int h[MAXK];}tk;
bool is_set(cont& c,int x){
	return c.h[x>>5]&(1<<(x&31));
}void set(cont& c,int x){
	c.h[x>>5]|=1<<(x&31);
}void unset(cont& c,int x){
	c.h[x>>5]^=1<<(x&31);
}
map <int,int>my;
int resP[MAXN],iresP;

bool dfs(cont cur,tk keys,int v){
	int i,j;
	for(i=0;i<MAXK;++i)keys.h[i]+=all[v].keys[i];
	int jk=0;for(i=0;i<n;++i)if(!is_set(cur,i))jk++;
	for(i=0;i<n;++i)if(keys.h[all[i].t]>0&&!is_set(cur,i)){
		set(cur,i);
		keys.h[all[i].t]-=1;
		if(my.find(cur.h[0])==my.end()){
			if(dfs(cur,keys,i)){
				resP[iresP++]=v+1;re true;
			}
		}
		keys.h[all[i].t]+=1;
		unset(cur,i);
	}
	if(jk==0){resP[iresP++]=v+1;re true;}
	my.insert(make_pair(cur.h[0],1));
	re false;
}

int main()
{
	#ifndef ONLINE_JUDGE
	ifstream cin("input.txt");
	ofstream cout("output.txt");
	#endif

	ll i,j,m,T,t,k;
	ll a,b;
	cin>>T;
	
	for(t=0;t<T;++t){
		cin>>k>>n;
		
		tk keys;memset(&keys,0,sizeof(tk));
		cont cur;memset(&cur,0,sizeof(cont));
		memset(&all,0,MAXN*sizeof(tpo));
		for(i=0;i<k;++i){cin>>a;keys.h[a]+=1;}
		for(i=0;i<n;++i){
			cin>>all[i].t>>a;
			for(j=0;j<a;++j){cin>>b;all[i].keys[b]+=1;}
		}bool res=false;
		iresP=0;for(i=0;i<n&&!res;++i)if(keys.h[all[i].t]>0){
			set(cur,i);
			keys.h[all[i].t]-=1;
			res=dfs(cur,keys,i);
			keys.h[all[i].t]+=1;
			unset(cur,i);
		}my.clear();
		cout<<"Case #"<<t+1<<":";
		if(!res)cout<<" IMPOSSIBLE"<<endl;
		else{
			for(;iresP>0;iresP--)cout<<" "<<resP[iresP-1];
			cout<<endl;
		}
	}
	re 0;
}