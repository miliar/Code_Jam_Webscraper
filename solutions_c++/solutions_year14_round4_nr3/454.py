#include<iostream>
#include<algorithm>
#include<cstdio>
#include<string>
#include<cstring>
#include<vector>
#include<unistd.h>
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

int w,h,n;
pair<pi,pi> rect[1005];
int yzip[2005],ynn;

#define FIND(ar,len,key) lower_bound(ar,ar+len,key)-ar
bool ocu[2005][1005];

int dx[]={0,1,0,-1},dy[]={1,0,-1,0};

pi path[2005*1005];

inline bool able(pi& a,int d){
	int px=a.sc+dx[d],py=a.fr+dy[d];
	if(px<0 || py<0 || px>=w || py>=h || ocu[py][px]) return false;
	return true;
}

int flow(){
	int res=0;
	REP(i,w) if(!ocu[0][i]){
		pi pos=mp(0,i);
		int dir=0;
		int cnt=0;

		do{
			if(able(pos,dir)){
				path[cnt++]=pos;
				pos.fr+=dy[dir];
				pos.sc+=dx[dir];
				dir=(dir+3)%4;
			}else dir=(dir+1)%4;
		}while((!(pos==mp(0,i) && dir==0)) && pos.fr<h-1);
		path[cnt++]=pos;

		if(pos.fr==0){
			while(i<w && !ocu[0][i]) ++i;
		}else{
			REP(j,cnt) ocu[path[j].fr][path[j].sc]=1;
			++res;
		}
	}
	return res;
}

int main(){
	int t;
	cin>>t;
	REP(setn,t){
		printf("Case #%d: ",setn+1);
		cin>>w>>h>>n;
		
		ynn=0;
		CLR(ocu);
		REP(i,n){
			cin>>rect[i].fr.fr>>rect[i].fr.sc>>
				rect[i].sc.fr>>rect[i].sc.sc;
			++rect[i].sc.fr;++rect[i].sc.sc;
			yzip[ynn++]=rect[i].fr.sc;
			yzip[ynn++]=rect[i].sc.sc;
		}
		yzip[ynn++]=0;
		yzip[ynn++]=h;

		sort(yzip,yzip+ynn);
		ynn=unique(yzip,yzip+ynn)-yzip;

		REP(i,n){
		//	rect[i].fr.sc=FIND(yzip,ynn,rect[i].fr.sc);
		//	rect[i].sc.sc=FIND(yzip,ynn,rect[i].sc.sc);
			
			REPN(j,rect[i].sc.sc,rect[i].fr.sc) REPN(k,rect[i].sc.fr,rect[i].fr.fr){
				ocu[j][k]=1;
			}
		}
		//h=ynn-1;
		
		int res=flow();			
		cout<<res<<endl;
	}
	return 0;
}



