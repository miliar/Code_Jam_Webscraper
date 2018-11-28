#include <bits/stdc++.h>
#define SZ(X) ((int)(X).size())
#define ALL(X) (X).begin(), (X).end()
#define REP(I, N) for (int I = 0; I < (N); ++I)
#define REPP(I, A, B) for (int I = (A); I < (B); ++I)
#define RI(X) scanf("%d", &(X))
#define RII(X, Y) scanf("%d%d", &(X), &(Y))
#define RIII(X, Y, Z) scanf("%d%d%d", &(X), &(Y), &(Z))
#define DRI(X) int (X); scanf("%d", &X)
#define DRII(X, Y) int X, Y; scanf("%d%d", &X, &Y)
#define DRIII(X, Y, Z) int X, Y, Z; scanf("%d%d%d", &X, &Y, &Z)
#define RS(X) scanf("%s", (X))
#define CASET int ___T, case_n = 1; scanf("%d ", &___T); while (___T-- > 0)
#define MP make_pair
#define PB push_back
#define MS0(X) memset((X), 0, sizeof((X)))
#define MS1(X) memset((X), -1, sizeof((X)))
#define LEN(X) strlen(X)
#define VPII vector<pair<int,int> >
#define F first
#define S second
#define RF(x) freopen(x,"r",stdin)
#define WF(x) freopen(x,"w",stdout)
typedef long long LL;
using namespace std;
typedef pair<LL,LL> PLL;
typedef pair<int,int> PII;
const LL MOD = 1e9+7;
const int SIZE = 1e6+5;
const LL INF = 1LL<<58;
const double eps = 1e-13;

string mm[14][3];

string dp(int x,int y){
	if(mm[x][y]!="x")return mm[x][y];
	if(x==0){
		if(y==0)return mm[x][y]="P";
		if(y==1)return mm[x][y]="R";
		if(y==2)return mm[x][y]="S";
	}
	if(y==0){
		string v1=dp(x-1,1),v2=dp(x-1,0);
		if(v1<v2)mm[x][y]=v1+v2;
		else mm[x][y]=v2+v1;
	}
	else if(y==1){
		string v1=dp(x-1,1),v2=dp(x-1,2);
		if(v1<v2)mm[x][y]=v1+v2;
		else mm[x][y]=v2+v1;
	}
	else if(y==2){
		string v1=dp(x-1,2),v2=dp(x-1,0);
		if(v1<v2)mm[x][y]=v1+v2;
		else mm[x][y]=v2+v1;
	}
	return mm[x][y];
}

int main(){
	RF("A-large.in");
	WF("out2.txt");
	REP(i,14){
		REP(j,3)mm[i][j]="x";
	}
	CASET{
		DRII(n,r);DRII(p,s);
		string cbest="x";
		REP(i,3){
			string cs=dp(n,i);
			//printf("%s ",cs.c_str());
			int v1=0,v2=0,v3=0;
			for(char c:cs){
				if(c=='P')v1++;
				else if(c=='R')v2++;
				else v3++;
			}
			if(p==v1&&r==v2&&s==v3){
				if(cbest=="x"||cs<cbest)cbest=cs;
			}
		}
		if(cbest=="x")printf("Case #%d: IMPOSSIBLE\n",case_n);
		else printf("Case #%d: %s\n",case_n,cbest.c_str());
		case_n++;
	}
}
