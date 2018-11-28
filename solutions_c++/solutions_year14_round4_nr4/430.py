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


int m,n;
char strs[10][15];
int lens[10];

int assign[10];
int maxi=-1,cnt;


struct node{
	node* nxt[30];
};
node pool[10*15];
int pcnt;
node* root[5];

int exi[5];
void solve(){
	memset(pool,0,sizeof(pool));
	REP(i,n) root[i]=&pool[i];
	memset(exi,0,sizeof(exi));
	REP(i,m) exi[assign[i]]++;
	REP(i,n) if(exi[i]==0) return;
	pcnt=n;
	

	REP(i,m){
		node* cur=&pool[assign[i]];
		REP(j,lens[i]){
			if(cur->nxt[strs[i][j]-'A']==NULL){
				cur->nxt[strs[i][j]-'A']=&pool[pcnt++];
			}
			cur=cur->nxt[strs[i][j]-'A'];
		}
	}

	if(maxi<pcnt){
		maxi=pcnt;
		cnt=1;
	}else if(maxi==pcnt) ++cnt;
}

void dfs(int ind){
	if(ind==m) {
		solve();
		return;
	}
	REP(i,n){
		assign[ind]=i;
		dfs(ind+1);
	}
}
int main(){
	int t;
	cin>>t;
	REP(setn,t){
		printf("Case #%d: ",setn+1);
		maxi=-1;
		cin>>m>>n;
		CLR(strs);
		REP(i,m) scanf("%s",strs[i]),lens[i]=strlen(strs[i]);
		
		dfs(0);

		cout<<maxi<<' '<<cnt<<endl;
	}



	return 0;
}



