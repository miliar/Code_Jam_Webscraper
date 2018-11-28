#include<iostream>
#include<algorithm>
#include<cstdio>
#include<cstring>
#include<vector>
#define REP(i,m) for(int i=0;i<m;++i)
#define REPN(i,m,in) for(int i=in;i<m;++i)
#define ALL(t) (t).begin(),(t).end()
#define pb push_back
#define mp make_pair
#define fr first
#define sc second
#define dump(x)  cerr << #x << " = " << (x) << endl
#define prl cerr<<"called:"<< __LINE__<<endl
using namespace std;
static const int INF =500000000; 
template<class T> void debug(T a,T b){ for(;a!=b;++a) cerr<<*a<<' ';cerr<<endl;}
typedef long long int lint;
typedef pair<int,int> pi;
int buf[105][105],rcan[105],ccan[105];

int h,w;
int main(){
	int t;scanf("%d",&t);
	for(int setn=1;setn<=t;++setn){
		scanf("%d%d",&h,&w);
		
		REP(i,h) REP(j,w) scanf("%d",&buf[i][j]);
		REP(i,h) rcan[i]=1;
		REP(i,w) ccan[i]=1;
		int fail=0;
		for(int i=2;i>=1;--i){
			REP(j,h) REP(k,w) if(buf[j][k]==i && !rcan[j] && !ccan[k]) fail=1;
			REP(j,h) REP(k,w) if(buf[j][k]==i){
				rcan[j]=0,ccan[k]=0;
			}
		}

		if(!fail) printf("Case #%d: YES\n",setn);
		else printf("Case #%d: NO\n",setn);
	}

	return 0;
}



