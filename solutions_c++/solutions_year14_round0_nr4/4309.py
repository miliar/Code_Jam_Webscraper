#include <stdio.h>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>

using namespace std;
int solve(vector <double> a, vector <double> b){
	int cont = 0;
	int n = a.size();
	for (int i = 0; i < n ; i++ ){	
		for ( int j=0; j<n ; j++ ){
			if(b[j] > a[i]){
				//printf("%lf %lf\n", b[j], a[i]);
				b[j]=-1.0;
				a[i]=0.0;
				cont++;
				break;
			}
		}
	}
	return cont;
}
main(){
	
	int ncases;
	int n;
	scanf("%d", &ncases);
	double naomi, ken;
	vector <double> vec1, vec2;
	for ( int i=1; i <= ncases; i++ ){

		scanf("%d", &n);
		vec1.clear(); vec2.clear();
		for (int j=0; j < n; j++){
			scanf("%lf", &naomi );
			vec1.push_back(naomi);
		}
		for (int j=0; j < n; j++){
			scanf("%lf", &ken );
			vec2.push_back( ken );
		}
		sort(vec1.begin(), vec1.end() );


		sort(vec2.begin(), vec2.end() );
		/*	for(int j=0; j < n; j++){
			printf("%lf %lf\n", vec1[j], vec2[j]);
		}
		puts("");
	
		*/
//puts("1");
		int ans1 = solve(vec2, vec1);
		//puts("2");
		int ans2 = n-solve(vec1, vec2);

		printf("Case #%d: %d %d\n", i, ans1, ans2);

	}
}