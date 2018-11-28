
#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;
typedef long long i8;

int ntc$, cas$;

int K,L,S;
char alf[105], wrd[105];
int buk[256], adv[105][256];
double dp[105][105][105];
vector< pair<char,int> > bve;

double solve() {
	scanf("%d%d%d",&K,&L,&S);
	scanf("%s",alf);
	scanf("%s",wrd);
	
	for (int i=0; i<L; i++) {
		bool fi=false;
		for (int j=0; j<K; j++)
			if (alf[j]==wrd[i]) fi=true;
		if (!fi) return 0.0;
	}
	
	for (char i='A'; i<='Z'; i++) {
		buk[i]=0;
	}
	for (int i=0; i<K; i++) {
		buk[alf[i]]++;
	}
	
	bve.clear();
	for (char i='A'; i<='Z'; i++) if (buk[i]>0) {
		bve.push_back(make_pair(i,buk[i]));
	}
	
	for (int m=0; m<L; m++) {
		for (int b=0; b<bve.size(); b++) {
			char c=bve[b].first;
			adv[m][c]=0;
			if (wrd[m]==c) {
				adv[m][c]=m+1;
			} else {
				for (int n=m-1; n>=0; n--) {
					int o=m-n;
					bool ok=(wrd[n]==c);
					for (int i=0; i<n; i++) 
						if (wrd[i]!=wrd[o+i]) ok=false;
					if (ok) {
						adv[m][c]=n+1;
						break;
					}
				}
			}
			//printf("   adv %d %c = %d\n", m, c, adv[m][c]);
		}
	}
	
	int pe=L;
	for (int i=1; i<L; i++) {
		bool ok=true;
		for (int j=0; j+i<L; j++)
			if (wrd[j]!=wrd[j+i]) ok=false;
		if (ok) {
			pe=i;
			break;
		}
	}
	
	int mx=(S-L+pe)/pe;
	//printf("   wrd=%s pe=%d mx=%d\n", wrd, pe, mx);
	
	double xx;
	dp[0][0][0]=1.0; // pos, match, already
	for (int t=1; t<=S; t++) {
		for (int m=0; m<=L; m++)
			for (int a=0; a<=mx; a++)
				dp[t][m][a]=0.0;
		for (int a=0; a<=min(mx,t); a++) {
			for (int m=0; m<=min(t,L); m++) if ((xx=dp[t-1][m][a])>0) {
				for (int i=0; i<bve.size(); i++) {
					char c=bve[i].first;
					if (adv[m][c]==L) {
						dp[t][L-pe][a+1] += xx*bve[i].second / K;
					} else {
						dp[t][adv[m][c]][a] += xx*bve[i].second / K;
					}
				}
			}
		}
	}
	
	double exp=0.0;
	for (int m=0; m<L; m++)
		for (int a=1; a<=mx; a++)
			exp += a*dp[S][m][a];
	
	return mx-exp;
}

main() {
	scanf("%d", &ntc$);
	for (int cas$=1; cas$<=ntc$; cas$++) {
		printf("Case #%d: %.8lf\n", cas$, solve());
	}
}
