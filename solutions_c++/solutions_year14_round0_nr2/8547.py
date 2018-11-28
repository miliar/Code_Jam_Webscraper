#include <iostream>
#include <fstream>
#include <stdio.h>

using namespace std;

int main(){
	int t, test = 1;
	ifstream in;
	FILE *out = fopen("outBlarge.out","w");
	in.open("B-large.in");
	double f,c,x,best,tmp;
	double farms;
	in>>t;
	while ( test <= t){
		in>>c>>f>>x;
		best = x/2;
		tmp = c/2;
		farms = 1;
		while (1){
			if ( tmp + x/(2+f*farms) > best)
				break;
			best = tmp + x/(2+f*farms);
			tmp+=(c/(2+f*farms));
			farms++;
		}
		fprintf(out,"Case #%d: %.7f\n",test,best);
		test++;
	}
	in.close();
	fclose(out);
}