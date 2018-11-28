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

int r[4][4];
int d[4][4];//ith worker can control jth machine
int o[4];
char tp[4];
bool taken[4];
int n;

bool recurse(int x){
	if(x==n)return 1;
	int haspath=0;
	REP(i,n){
		if(d[o[x]][i]){
			if(!taken[i]){
				taken[i]=1;
				int nv=recurse(x+1);
				taken[i]=0;
				if(nv==0)return 0;
				else haspath=1;
			}
		}
	}
	return haspath;
}

int main(){
	RF("D-small-attempt0.in");
	WF("out.txt");
	CASET{
		RI(n);
		REP(i,n){RS(tp);
			REP(j,n)r[i][j]=tp[j]-'0';
		}
		int bmax=1<<(n*n);
		int cmin=1<<30;
		REP(bm,bmax){
			bool legit=1;
			int cc=0;
			REP(i,n){
				REP(j,n){
					int cbit=bm&(1<<(i*n+j));
					d[i][j]=cbit;
					if(cbit==0&&r[i][j]){legit=0;break;}
					cc+=(cbit>0)^r[i][j];
				}
				if(!legit)break;
			}
			if(!legit)continue;
			//printf("BM:%d",bm);
			REP(i,n)o[i]=i;
			legit=1;
			do{
				MS0(taken);
				legit&=recurse(0);
			}while(next_permutation(o,o+n));
			if(legit)cmin=min(cmin,cc);
		}
		printf("Case #%d: %d\n",case_n,cmin);
		case_n++;
	}
}
