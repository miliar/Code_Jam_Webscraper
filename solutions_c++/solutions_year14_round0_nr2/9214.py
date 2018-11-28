// Qualification Round
// Problem B Small

#include <stdio.h>
#include <vector>
using namespace std;

#define pb push_back

int main(){
	bool f;
	int T, ti;
	double C,F,X, t,n,p;
	FILE *fi = fopen("b_small.in","r"),
		*fo = fopen("b_small.out","w");
	fscanf(fi,"%d\n",&T);
	for(ti = 1; ti <= T; ti++){
		C = F = X = 0.0;
		fscanf(fi,"%lf %lf %lf",&C,&F,&X);
		if(C >= X){
			fprintf(fo,"Case #%d: %.8lf\n",ti,X/2.0);
			continue;
		}
		t = n = 0.0, p = 2.0;
		while(n < X){
			if(n >= C){
				if((X-(n-C))/(p+F) < (X-n)/p){
					n -= C, p += F;
				}else{
					t += (X-n)/p;
					break;
				}
			}else
				t += (C-n)/p, n = C;
		}
		fprintf(fo,"Case #%d: %.8lf\n",ti,t);
	}
	fclose(fi); fclose(fo);
	return 0;
}
