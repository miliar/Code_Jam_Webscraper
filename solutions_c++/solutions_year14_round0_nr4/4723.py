#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <queue>

#include <stdio.h>
#include <ctype.h>
#include <math.h>
#include <string.h>
#include <stdlib.h>
//#include <random>
#include <time.h>
//#include <float.h>

using namespace std;

int main() {
	int T, i, j, n, s1, s2, h;
	double x;

	int test = 0;

	scanf("%d", &T);

	for (i=0; i<T;i++) {
		scanf("%d", &n);
		printf("Case #%d: ",i+1);
		
		vector<double> Naomi, Naomi2;
		vector<double> Ken, Ken2;

		s1 = 0;
		s2 = 0;
		

		if (test==1) {printf("\n ");}
		for (j=0; j<n;j++) {
			scanf("%lf ", &x);
			Naomi.push_back(x);
			Naomi2.push_back(x);
			if(test==1){printf("%.5lf ", x);}
		}

		if(test==1){printf("\n ");}
		for (j=0; j<n;j++) {
			scanf("%lf ", &x);
			Ken.push_back(x);
			Ken2.push_back(x);
			if(test==1){printf("%.5lf ", x);}
		}
		if(test==1){printf("\n ");}

		
		if(test==2){
			sort(Naomi.begin(), Naomi.end());
			printf("\n");
			for (auto k=Naomi.begin(); k!=Naomi.end(); k++) {
				printf("%.5lf ",*k);
			}

			sort(Ken.begin(), Ken.end());
			printf("\n");
			for (auto k=Ken.begin(); k!=Ken.end(); k++) {
				printf("%.5lf ",*k);
			}
			printf("\n");
		}
		
		if(test==3){
			next_permutation(Naomi.begin(), Naomi.end());
			printf("\n");
			for (auto k=Naomi.begin(); k!=Naomi.end(); k++) {
				printf("%.5lf ",*k);
			}
			printf("\n");
		}

		h=1;
		for (j=0; j<n;j++) {
			
			
			auto m1 = max_element(Naomi.begin(), Naomi.end());
			auto m2 = Ken.begin();
			auto m3 = Ken.begin();

			for (auto k=Ken.begin(); k!=Ken.end(); k++) {
				if ((*k > *m2) & (*k > *m1)) { m2 = k; }
				if (*k < *m3) { m3 = k; }
			}

			//printf("\n");
			//printf("%.5lf ", *m1);
			//printf("%.5lf ", *m2);
			//printf("%.5lf ", *m3);

			if (*m2 > *m1) {
				Naomi.erase(m1);
				Ken.erase(m2);
				h=0;
			}
			else {
				s1++;
				Naomi.erase(m1);	
				Ken.erase(m3);
				h=1;
			}

			m1 = min_element(Naomi2.begin(), Naomi2.end());
			m2 = max_element(Ken2.begin(), Ken2.end());
			m3 = min_element(Ken2.begin(), Ken2.end());

			if (*m1 > *m3) {
				s2++;
				Naomi2.erase(m1);
				Ken2.erase(m3);
			}
			else {
				Naomi2.erase(m1);
				Ken2.erase(m2);	
			}

			
		}

		printf("%d %d", s2, s1);

		



		printf("\n");
	}

	return 0;
}