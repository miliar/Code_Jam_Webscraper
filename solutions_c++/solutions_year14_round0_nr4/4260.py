#include <cstdio>
#include <algorithm>
using namespace std;

double ken[1001],ken2[1001],naomi[1001];

int scoreWar(int n){
	int i,score,chosen,nextFirst = 0;
	for(i=0; i<n; i++){ ken2[i] = ken[i]; }
	for(i=0; i<n; i++){
		chosen = nextFirst;
		while(ken[chosen] < naomi[i]) { chosen++; }
		if (chosen < n){ ken[chosen] = -1; }
		else{ ken[nextFirst] = -1; score++; }
	}
	return score;
}

int scoreDWar(int n){
	int i,j,score = 0,next = 0;
	double nao;
	for(i=0,j=0; i<n; i++){
		for(j=next; j<n; j++){
			if (ken2[j] != -1 && naomi[i] > ken2[j]){ score++; ken2[j] = -1; break; }
		}
	}
	return score;
}

int main(){
	freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

	int t,n,i,c,sw,sdw;
	scanf("%d", &t);
	c = t;
	while(t--){
		scanf("%d",&n);
		for(i=0; i<1000; i++){ naomi[i] = ken[i] = ken2[i] = 0; }
		for(i=0; i<n; i++){ scanf("%lf", &naomi[i]); }
		for(i=0; i<n; i++){ scanf("%lf", &ken[i]); }
		sort(ken,ken+n);
		sort(naomi,naomi+n);
		sw = scoreWar(n);
		sdw = scoreDWar(n);
		printf("Case #%d: %d %d\n", c-t, sdw, sw);
	}
}