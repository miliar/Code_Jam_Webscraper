#include<iostream>
#include<algorithm>
#include<cstdio>
#include<string>
#include<cstring>
#include<vector>
#define REP(i,m) for(int i=0;i<(m);++i)
#define REPN(i,m,in) for(int i=(in);i<(m);++i)
#define ALL(t) (t).begin(),(t).end()
#define CLR(a) memset((a),0,sizeof(a))
#define pb push_back
#define mp make_pair
#define fr first
#define sc second
#define dump(x)  cerr << #x << " = " << (x) << endl
#define prl cerr<<"called:"<< __LINE__<<endl
using namespace std;
static const int INF =500000000; 
template<class T> void debug(T a,T b){ for(;a!=b;++a) cerr<<*a<<' ';cerr<<endl;}
template<class T> void chmin(T& a,const T& b) { if(a>b) a=b; }
template<class T> void chmax(T& a,const T& b) { if(a<b) a=b; }
typedef long long int lint;
typedef pair<int,int> pi;


int ok[30];

void doit(){
	int r;cin>>r;--r;
	REP(i,4) REP(j,4){
		int tmp;cin>>tmp;
		if(i!=r) ok[tmp]=0;
	}
}

int main(){
	int t;cin>>t;
	REPN(setn,t+1,1){
		REP(i,30) ok[i]=1;
		
		doit();
		doit();
		
		int cnt;
		printf("Case #%d: ",setn);
		if((cnt=count(ok+1,ok+17,1))==1){
			int res;
			REPN(i,17,1) if(ok[i]) res=i;
			cout<<res<<endl;
		}else if(cnt>1) puts("Bad magician!");
		else puts("Volunteer cheated!");
	}
	return 0;
}



