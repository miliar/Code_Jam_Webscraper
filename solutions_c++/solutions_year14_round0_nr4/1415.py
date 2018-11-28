#include <cstdio>
#include <algorithm>
#include <cstring>

using namespace std;

int N;
double naomi[10000];
double ken[10000];
int used[10000];
int y, z;

bool compare(double a, double b){
	return b<a;
}

int deceitfulWar(){
	sort(naomi, naomi+N);
	sort(ken, ken+N);
	int iNaomi=N-1;
	int iKen=N-1;
	int nPoints=0;
	while(iKen>=0){
		for(;iKen && ken[iKen]>naomi[iNaomi]; iKen--);
		nPoints+=naomi[iNaomi]>ken[iKen];
		//printf("K[%d] = %lf\t", iKen, ken[iKen]);
		//printf("N[%d] = %lf %d\n", iNaomi, naomi[iNaomi], ken[iKen]>naomi[iNaomi]);
		iNaomi--;
		iKen--;
	}
	return nPoints;
}

int war(){
	sort(naomi, naomi+N);
	sort(ken, ken+N);
	int iNaomi=N-1;
	int iKen=N-1;
	int kPoints=0;
	while(iNaomi>=0){
		for(;iNaomi && naomi[iNaomi]>ken[iKen]; iNaomi--);
		kPoints+=ken[iKen]>naomi[iNaomi];
		//printf("K[%d] = %lf\t", iKen, ken[iKen]);
		//printf("N[%d] = %lf %d\n", iNaomi, naomi[iNaomi], ken[iKen]>naomi[iNaomi]);
		iNaomi--;
		iKen--;
	}
	return N-kPoints;
}

int main(){
	int T, cases=1;
	scanf("%d\n",&T);
	
	
	while(T--){
		scanf("%d\n",&N);
		for(int i=0; i<N; i++){
			scanf("%lf\n", &naomi[i]);
		}
		for(int i=0; i<N; i++){
			scanf("%lf\n", &ken[i]);
		}
		//sort(naomi, naomi+N);
		//sort(ken, ken+N, compare);
		//
		//for(int i=0; i<N; i++){
		//	printf("%lf\t", naomi[i]);
		//}
		//printf("\n");
		//
		//for(int i=0; i<N; i++){
		//	printf("%lf\t", ken[i]);
		//}
		//printf("\n");
		//
		//printf("*******************\n");
		//sort(naomi, naomi+N);
		//sort(ken, ken+N);
		//
		//for(int i=0; i<N; i++){
		//	printf("%lf\t", naomi[i]);
		//}
		//printf("\n");
		//
		//for(int i=0; i<N; i++){
		//	printf("%lf\t", ken[i]);
		//}
		//printf("\n");
		
		y=deceitfulWar();
		z=war();
		
		printf("Case #%d: %d %d\n", cases++, y, z);
	}
	return 0;
}

