#include <cstdio>
#include <algorithm>

#define MAXN 105
#define forn(i,n) for(int i = 0; i < n; i++)
#define forn2(i,j,n) for(int i = j; i <= n; i++)

using namespace std;

double naomi[1005], ken[1005];
int N;

int war(){
	int n = 0, k = 0;
	while(k != N){
		if(ken[k] > naomi[n]){
			n++;
		}
		k++;
	}
	return N-n;
}

int deceitfulWar(){
	int n = 0, res = 0, k = 0;
	while(n != N){
		if(naomi[n] > ken[k]){
			res++;
			k++;
		}
		n++;
	}
	return res;
}

int main(){
	int T,t;
	scanf("%d",&T);
	forn2(t,1,T){
		int i;
		scanf("%d",&N);
		forn(i,N) scanf("%lf",&naomi[i]);
		forn(i,N) scanf("%lf",&ken[i]);

		sort(naomi,naomi+N);
		sort(ken,ken+N);

		printf("Case #%d: %d %d\n",t, deceitfulWar(), war());
	}
}