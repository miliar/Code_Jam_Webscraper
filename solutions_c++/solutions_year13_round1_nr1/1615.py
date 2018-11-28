#include <iostream>
#include <fstream>
#include <algorithm>
#include <string>
#include <cmath>
#include <sstream>

using namespace std;

int main(void){

	FILE *fin;
	fin = fopen("A-small-attempt0.in","r");

	FILE *fout;
	fout = fopen("output.txt","w");

	int T;

	fscanf(fin,"%d\n",&T);

	long long r, t;
	int tc;

	for(tc = 0; tc < T; tc++){

		fscanf(fin, "%llu %llu\n", &r, &t);
		long long area;
		area = (r+1)*(r+1) - r*r;
		long long total = 0;
		bool done = false;
		if(area <= t){
			total = 1;
			t -= area;
		}
		else done = true;

		while(!done){
			r+=2;
			area = (r+1)*(r+1) - r*r;
			if(area <= t){
				total++;
				t -= area;
			}
			else done = true;
		}

		fprintf(fout,"Case #%d: %llu\n",tc+1, total);

	}
	fclose(fin);
	fclose(fout);
	


}