#include <iostream>
#include <utility> 
#include <vector>
#include <stdio.h>
#include <algorithm> 
#include <string.h>
#include <set>
#include <iomanip>

using namespace std;

#define MAX 20

int main(){

	double c, f, x, b, total;
	int t;
	
	scanf("%d", &t);
	
	for (int i = 0; i < t; i++){
		scanf("%lf %lf %lf", &c, &f, &x);
		
		total = 0.0;
		b = 2.0;
		while ((x/b) >= ((c/b) + (x/(b+f)))){
			total += (c/b);
			b+= f;
		}
		total += (x/(b));

		printf("Case #%d: %.7lf\n", i+1, total);
	}
	return 0;
}