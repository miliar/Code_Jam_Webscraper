#include <iostream>
#include <vector>
#include <stdio.h>
#include <iomanip>
using namespace std;

int T;
double C, F, X;

double Calc() {
	double tempo = X / 2, nuovo=0, prod=2, fact=0;
	do {
	  fact += C/prod;
	  nuovo = fact + (X / (prod+F) );
	  if(nuovo < tempo) {
		  tempo=nuovo;
		  prod += F;
	  }
	  else break;
    } while(true);
	return tempo;
}
int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin >> T;
	for(int i=0; i< T; i++) {
		cin >> C >> F >> X;
		double x = Calc();
		printf("Case #%d: %.7f\n", i+1, x);
	}
	
}
