// Enjoy your stay.

#include <bits/stdc++.h>

#define EPS 1e-9
#define INF 1070000000LL
#define MOD 1000000007LL
#define fir first
#define foreach(it,X) for(auto it=(X).begin();it!=(X).end();it++)
#define ite iterator
#define mp make_pair
#define mt make_tuple
#define rep(i,n) rep2(i,0,n)
#define rep2(i,m,n) for(int i=m;i<(n);i++)
#define pb push_back
#define sec second
#define sz(x) ((int)(x).size())

using namespace std;

typedef istringstream iss;
typedef long long ll;
typedef pair<ll,ll> pi;
typedef stringstream sst;
typedef vector<ll> vi;

// from http://www.ioi-jp.org/camp/2014/2014-sp-tasks/2014-sp-d1-growing-sample.cpp

int N;
int segt[2250000];
void add(int id,int lf,int rg,int plc) {
	if(lf>plc||rg<plc) return;
	if(lf==rg&&lf==plc) {
		segt[id]=1;
		return;
	}
	int hf=(lf+rg)/2;
	add(id*2+1,lf,hf,plc);
	add(id*2+2,hf+1,rg,plc);
	segt[id]=segt[id*2+1]+segt[id*2+2];
}
int calc(int id,int lf,int rg,int callf,int calrg) {
	if(lf>calrg||rg<callf) return 0;
	if(callf<=lf&&calrg>=rg) return segt[id];
	int hf=(lf+rg)/2;
	return calc(id*2+1,lf,hf,callf,calrg)+calc(id*2+2,hf+1,rg,callf,calrg);
}
typedef struct {
	int vl;
	int plc;
}plts;
plts plt[300002];
int cmp(const void *ka,const void *kb) {
	plts *a=(plts *)ka;
	plts *b=(plts *)kb;
	if(a->vl!=b->vl) return b->vl-a->vl;
	return a->plc-b->plc;
}
int getmin(int a,int b) {
	if(a>b) return b;
	return a;
}
int main2() {
	scanf("%d",&N);
	for(int i=0;i<2250000;i++) segt[i]=0;
	for(int i=0;i<N;i++) {
		scanf("%d",&plt[i].vl);
		plt[i].plc=i+1;
	}
	qsort(plt,N,sizeof(plts),cmp);
	long long sol=0;
	int nw=0;
	while(nw<N) {
		int nvl=plt[nw].vl;
		int nwb=nw;
		while(nw<N) {
			if(plt[nw].vl!=nvl) break;
			sol+=getmin(calc(0,1,N,1,plt[nw].plc),calc(0,1,N,plt[nw].plc,N));
			nw++;
		}
		while(nwb<nw) {
			add(0,1,N,plt[nwb].plc);
			nwb++;
		}
	}
	printf("%lld\n",sol);
	return 0;
}
//

int main(){
	//cin.tie(0);
	//ios_base::sync_with_stdio(0);
	
	
	
	int T;
	cin>>T;
	time_t start=clock(),pre=start;
	rep(tc,T){
		cout<<"Case #"<<tc+1<<": ";
		main2();
		time_t now=clock();
		cerr<<tc+1<<"/"<<T<<": "<<(double)(now-pre)/CLOCKS_PER_SEC<<endl;
		if(tc==T-1){
			cerr<<"Total: "<<(double)(now-start)/CLOCKS_PER_SEC<<endl;
			cerr<<"  Ave: "<<(double)(now-start)/CLOCKS_PER_SEC/T<<endl;
		}
		pre=now;
	}
}
