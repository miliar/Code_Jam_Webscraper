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

int n;
vector<int> ar;

pi hei[1005];
int main(){
	int t;
	cin>>t;
	REP(setn,t){
		printf("Case #%d: ",setn+1);

		cin>>n;
		ar.resize(n);
		REP(i,n){
			cin>>ar[i];
			hei[i]=mp(ar[i],i);
		}
		sort(hei,hei+n);
			
		lint res=0;
		REP(i,n){
			int val=hei[i].fr;
			int pos=find(ALL(ar),val)-ar.begin();
			res+=min(pos,(int)(ar.size()-1-pos));
			ar.erase(ar.begin()+pos);
		}
		cout<<res<<endl;
	}

	return 0;
}



