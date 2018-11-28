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

char buf[5][5];
int X,O,T;
void doit(char a){
	if(a=='X') ++X;
	else if(a=='O') ++O;
	else ++T;
}

int judge(char a,char b,char c,char d){
	X=0,O=0,T=0;
	doit(a);doit(b);doit(c);doit(d);

	if(X>=3 && X+T==4) return 1;
	if(O>=3 && O+T==4) return 2;
	return 0;
}

int solve(){
	REP(i,4){
		int r=judge(buf[i][0],buf[i][1],buf[i][2],buf[i][3]);
		if(r!=0) return r;
		r=judge(buf[0][i],buf[1][i],buf[2][i],buf[3][i]);
		if(r!=0) return r;
	}
	int r;
	if((r=judge(buf[0][0],buf[1][1],buf[2][2],buf[3][3]))!=0) return r;
	if((r=judge(buf[3][0],buf[2][1],buf[1][2],buf[0][3]))!=0) return r;
	return 0;
}

char code[][30]={
	"Draw",
	"X won",
	"O won",
	"Game has not completed"
};

int main(){
	int t;scanf("%d",&t);
	for(int setn=1;setn<=t;++setn){
		REP(i,4) scanf("%s",buf[i]);

		int r=solve();
		printf("Case #%d: ",setn);
		if(r) printf("%s\n",code[r]);
		else{
			int emp=0;
			REP(i,4) REP(j,4) if(buf[i][j]=='.') ++emp;
			if(emp) r=3;
			else r=0;
			printf("%s\n",code[r]);
		}
	}


	return 0;
}



