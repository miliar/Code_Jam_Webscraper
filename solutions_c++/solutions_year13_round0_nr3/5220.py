#include <vector>
#include <algorithm>
#include <sstream>
#include <deque>
#include <string.h>
#include <stdio.h>
#include <iostream>
#include <map>
#include <set>
#include <math.h>

using namespace std;

int check(char *p){

	int tam = strlen(p);
	
	for (int i = 0; i < tam; i++){
		if (p[i] != p[tam-i-1])
			return 0;
	}
	return 1;
}

int main(){

	char fair[43];
	char square[43];
	int t;
	long a, b, cont, n_;
	double n;
	
	scanf("%d", &t);
	
	for (int i = 0; i < t; i++){
		scanf("%ld %ld", &a, &b);
		cont = 0;
		for (long j = a; j <= b; j++){
		
			n = sqrt(j);
			n_ = (long)n;
			
			if ((n_*n_) == j){
				sprintf (fair, "%ld", j);
				sprintf (square, "%ld", n_);
				if (check(fair) and check(square)){
					cont++;
				}
			}
		}
		cout << "Case #" << i+1 << ":" << " " << cont << endl;
	}
	

	return 0;
}