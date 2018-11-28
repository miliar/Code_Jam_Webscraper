#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int T, N;

double naomi[1001];
double ken[1001];

int main(){

	scanf("%d ", &T);

	for(int cas = 1; cas <= T; cas++){
		scanf("%d ", &N);

		
		for(int i=0;i<N;i++) scanf("%lf ", &naomi[i]);
		for(int i=0;i<N;i++) scanf("%lf ", &ken[i]);
		
		sort(naomi, naomi + N);
		sort(ken, ken + N); 

		//for(int i=0;i<N;i++) printf("%lf ", naomi[i]);
		//printf("\n");

		int p1 = 0, p2 = 0;

		//Normal strategy
		int n = 0, k = 0;
		while(n < N && k < N){
			if(naomi[n] < ken[k]){
				n++;
				k++;
			}else{
				k++;
			}
		}

		p1 = N - n;

		//Deceit strategy
		n = 0, k = 0;
		while(n < N && k < N){
			if(naomi[n] > ken[k]){
				n++;
				k++;
			}else{
				n++;
			}
		} 
		p2 = k; 	

		printf("Case #%d: %d %d\n", cas, p2, p1);
	}

	return 0;
}
