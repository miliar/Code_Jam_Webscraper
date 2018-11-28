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

int r,c,m;
int grid[10][10];
int buf[10][10];
int dx[]={0,1,0,-1,1,1,-1,-1},dy[]={1,0,-1,0,1,-1,1,-1};
void rec(int y,int x){
	buf[y][x]=2;
	int around=0;
	REP(d,8){
		int py=y+dy[d],px=x+dx[d];
		if(py<0 || px<0 || px>=c || py>=r) continue;
		if(buf[py][px]==1) ++around;
	}
	if(around==0) REP(d,8){
		int py=y+dy[d],px=x+dx[d];
		if(py<0 || px<0 || px>=c || py>=r || buf[py][px]!=0) continue;
		rec(py,px);
	}
}

bool check(){
	REP(i,r) REP(j,c) if(grid[i][j]==0){
		REP(i2,r) REP(j2,c) buf[i2][j2]=grid[i2][j2];

		rec(i,j);
		int fail=0;
		REP(i2,r) REP(j2,c) if(buf[i2][j2]==0) fail=1;
		if(!fail){
			grid[i][j]=2;
			return true;
		}
	}
	return false;
}

bool dfs(int y,int x,int sum){
	if(x==c){
		++y;
		x=0;
	}
	if(y==r){
		if(sum!=m) return false;
		return check();
	}

	grid[y][x]=1;
	if(dfs(y,x+1,sum+1)) return true;
	grid[y][x]=0;

	if(dfs(y,x+1,sum)) return true;
	return false;
}

char code[]={'.','*','c'};
int main(){
	int t;cin>>t;
	REPN(setn,t+1,1){
		printf("Case #%d:\n",setn);
		cin>>r>>c>>m;

		if(dfs(0,0,0)==false) puts("Impossible");
		else{
			REP(i,r){
				REP(j,c) putchar(code[grid[i][j]]);
				putchar('\n');
			}
		}
	}

	return 0;
}



