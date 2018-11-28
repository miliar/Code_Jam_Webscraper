#include <stdio.h>
#include <limits.h>
#include <algorithm>

#define MAX INT_MAX / 1000

using namespace std;
int t;
double c, f, x;


double Recurse(int farms){
	//printf("x / c = %f, farms = %d\n", x/c, farms);
	if(farms >= x){return MAX;}
	//printf("x / (f * farms + 2) = %f\nc / (f * farms + 2) = %f\n",x / (f * farms + 2),  c / (f * farms + 2));
	return min(x / (f * farms + 2), c / (f * farms + 2) + Recurse(farms + 1));
};

int main(){
	FILE *in, *out;
	in = fopen("cookie.in.txt", "r");
	out = fopen("cookie.out.txt", "w");
	fscanf(in, "%d", &t);
	for (int i = 0; i < t; i++){
		fscanf(in, "%lf %lf %lf", &c, &f, &x);
		fprintf(out, "Case #%d: %.7f\n", i+1, Recurse(0));
	}
	
	fclose(in);
	fclose(out);
	
	return 0;
}
