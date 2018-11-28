#pragma warning(disable:4996)
#include <iostream>
#include <fstream>
#include <cstdio>
using namespace std;
const double eps = 1e-7;

int main(){
	//ifstream in("B-small-attempt0.in");
	//ofstream out("B-small-practice.txt");

	FILE *in = fopen("B-large.in", "r");
	FILE *out = fopen("B-large.txt", "w");

	int cases;
	fscanf(in, "%d", &cases);
	for (int i = 1; i <= cases; i++){
		double C, F, X;
		fscanf(in, "%lf %lf %lf", &C, &F, &X);
		double cur_speed = 2;
		double result = 0;
		for (int i = 0;; i++){
			double time1 = X / cur_speed;
			double time2 = C / cur_speed + X / (cur_speed + F);
			if (time1 < time2){
				result += time1;
				break;
			}
			else{
				result += C / cur_speed;
				cur_speed += F;
			}
		}
		fprintf(out, "Case #%d: %.7f\n", i, result);
	}

	return 0;
}