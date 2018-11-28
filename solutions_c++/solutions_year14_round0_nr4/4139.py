#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <queue>
#include <vector>
#include <map>
#include <set>
#include <stack>
#include <list>
#include <algorithm>
#include <iostream>
#include <assert.h>

using namespace std;

#define SET(v,i) memset(v,i,sizeof(v));
#define FOR(i,n,k) for(int i=n;i<k;++i)
#define WHILE(i,n) while(i<n)
#define RI(i) scanf("%d",&i);
#define RS(i) scanf("%s",i);
#define RF(i) scanf("%lf",&i);
#define RL(i) scanf("%lld",&i);
#define OPEN(s) freopen(s,"r",stdin);
#define CLOSE(s) freopen(s,"w",stdout);

const int INF=0x3F3F3F3F;
const int MAXN=100001;
typedef long long int i64;
typedef pair<int,int> pii;
typedef pair<string,int> psi;

double naomi[MAXN],ken[MAXN];
bool used[MAXN];

int main(){
	#ifdef DM1_MACHINE
		OPEN("D.in");
		CLOSE("FILED.out");
	#endif
	int t; RI(t);
	FOR(ic,1,t+1){
		SET(used,false);
		int n; RI(n);
		FOR(i,0,n) RF(naomi[i]);
		FOR(i,0,n) RF(ken[i]);
		sort(naomi,naomi+n);
		sort(ken,ken+n);
		int naomi_war=0,naomi_dwar=0;
		for(int i=n-1,j=n-1;i>=0;--i){
			double ncard = naomi[i];
			double kcard = ken[j];
			if(ncard > kcard) naomi_war++;
			else j--;
			
		}
		int lidx=0;
		for(int i=0;i<n;++i){
			if(naomi[i] < ken[lidx]){
				continue;
			}
			else{
				lidx++;
				naomi_dwar++;
			}
		}
		printf("Case #%d: %d %d\n",ic,naomi_dwar,naomi_war);
	}
	return 0;
}


////////////////////////////////////////////
/////////////Code by David Moran////////////
/////////////////////////////P=NP///////////
