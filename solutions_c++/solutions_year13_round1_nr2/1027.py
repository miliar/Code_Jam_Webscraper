#include<cstdio>
#include<cstdlib>
#include<vector>
#include<map>
#include<set>
#include<cstring>
#include<algorithm>
using namespace std;
#define pb(X) push_back(X)
#define mp(X,Y) make_pair(X,Y)
#define sz(X) (int)X.size()

int PD[10][20], v[20];
int E, R, n;

int solve(int e, int p){
	if(p==n)
		return 0;
	if(PD[e][p]!=-1)
		return PD[e][p];
	PD[e][p]=0;
	for(int i=0;i<=e;i++)
		PD[e][p] = max(PD[e][p], i*v[p] + solve(min(E,e-i+R),p+1));
	return PD[e][p];
}


int main(){
	int T;
	scanf("%d", &T);
	for(int caso=1;caso<=T;caso++) {
		scanf("%d %d %d",&E,&R,&n);
		for(int i=0;i<n;i++)
				scanf("%d",&v[i]);
		memset(PD,-1,sizeof(PD));
		printf("Case #%d: %d\n",caso,solve(E,0));
	}
	return 0;
}
