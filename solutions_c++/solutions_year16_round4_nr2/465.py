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

double v[300];//probability of getting 
double p[300];
double t[300];

int main(){
	RF("B-large.in");
	WF("out4.txt");
	CASET{
		DRII(n,k);
		REP(i,n)scanf("%lf",&p[i]);
		sort(p,p+n);
		double cmax=0;
		REP(s,k+1){//number of things in first section
			REP(i,n+1)v[i]=0;
			v[0]=1;
			REP(i,s){
				t[0]=v[0]*((double)1-p[i]);
				REPP(j,1,n){
					t[j]=v[j]*((double)1-p[i])+v[j-1]*p[i];
				}
				swap(v,t);
			}
			REPP(i,n-(k-s),n){
				t[0]=v[0]*((double)1-p[i]);
				REPP(j,1,n){
					t[j]=v[j]*((double)1-p[i])+v[j-1]*p[i];
				}
				swap(v,t);
			}
			if(v[k/2]>cmax){
				cmax=v[k/2];
			}
		}
		printf("Case #%d: %.9lf\n",case_n,cmax);
		case_n++;
	}
}
