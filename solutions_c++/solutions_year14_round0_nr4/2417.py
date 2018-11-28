#include <algorithm>
#include <cctype>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;

#define DEBUG(x) cout << ">>> " << #x << " : " << x << endl;
#define REP(i,a) for (int i = 0; i < (a); ++i)
#define FOR(i,a,b) for (int i = (a); i <= (b); ++i)
#define FORD(i,a,b) for (int i = (a); i >= (b); --i)
#define FOREACH(it, a) for (__typeof((a).begin()) it = (a).begin(); it != (a).end(); ++it)
#define  pb push_back
#define  pu push
#define SA(a,x) memset(a,x,sizeof(a))

inline bool EQ(double a, double b) { return fabs(a-b) < 1e-9; }

const int INF = 1<<29;
typedef long long ll;
typedef pair<int ,int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;
///////////////////////////////////////////////////////////////////////////
int T,N;
vector<double>  nao,ken;

int war(){
	int c = 0;
	int u_n[nao.size()],u_k[ken.size()];
	SA(u_n,0);
	SA(u_k,0);
	REP(i,nao.size()){
		bool nao_w = true;
		REP(j,ken.size()){
			if(u_k[j]) continue;
			if(nao[i]<ken[j]){
				u_k[j] = 1;				
				nao_w = false;
				break;
			}	
		}
		if(nao_w) c++;
	}
	return c;
}


int d_war(){
	int c = 0;
	int f = 0, l = ken.size()-1;
	REP(i,nao.size()){
		if(nao[i]>ken[f]) {
			c++;
			f++;
		} else {
			l--;
		}
	}
	return c;
}



int main()
{
int p = 1;
scanf("%d",&T);
while(T--){
	scanf("%d",&N);
	nao.clear();
	ken.clear();
	REP(i,N) {
		double b;
		scanf("%lf",&b);
		nao.pb(b);
	}
	REP(i,N) {
		double b;
		scanf("%lf",&b);
		ken.pb(b);
	}
	sort(nao.begin(),nao.end());
	sort(ken.begin(),ken.end());
	printf("Case #%d: %d %d\n",p++,d_war(),war());
}

return 0;
}
