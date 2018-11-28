#include <iostream>
#include "math.h"

using namespace std;
int t,a,b;

bool ifpol(int x){
	if(x < 10)
		return true;
	if(x < 100){
		if(!(x % 11)){
			return true;
		}
		else return false;
	}
	if(x == 1000){
		return false;
	}
	if((x / 100) == x % 10)
		return true;
	return false;
}

int main(){
	FILE * inp;
	FILE * outp;
	inp = fopen("input.in", "r");
	outp = fopen("output.txt", "w");

	fscanf(inp,"%d\n",&t);
	for(int i = 0; i < t; i++){
		int count = 0;
		fscanf(inp,"%d %d\n",&a, &b);
		int s,f;
		if((int)sqrt(a)*(int)sqrt(a) == a)
			s = (int)sqrt(a);
		else s = (int)sqrt(a)+1;
		f = (int)sqrt(b);
		for(int j = s; j <= f; j++){
			if((ifpol(j))&&(ifpol(j*j))){
				count++;
			}
		}
		fprintf(outp, "Case #%d: %d\n", i+1, count);
	}

	fclose(inp);
	fclose(outp);
	return 0;
}