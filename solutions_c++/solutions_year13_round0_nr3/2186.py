#include "stdio.h"
#include <math.h>
#define ll long long
bool isP(ll num) {
	bool re=true;
	ll tmp=num;
	int size=0;
	int n[11];
	while(tmp!=0) {
		n[size]=tmp%10;
		tmp/=10;
		++size;
	}
	for(int i=0; i<size/2; ++i)
		if(n[i]!=n[size-i-1]) {
			re=false; 
			break;
		}
	return re;
}
int main() {
	ll num, i,j,k;
	ll ans;
	ll A, B;
	FILE *fp, *fp2;
	
	fp = fopen("C-small-attempt0.in", "r");
	fp2 = fopen("C-small-attempt0-sol.in", "w");
	fscanf(fp, "%lld", &num);

	for(i=0; i<num; ++i) {
		ans=0;
		fprintf(fp2,"Case #%d: ",i+1);
		fscanf(fp,"%lld %lld", &A, &B);
		for(j=ceil(sqrt((long double)(A))); j<=floor(sqrt((long double)(B))); ++j) {
			if(isP(j*j) && isP(j)) 
				++ans;
		}
		fprintf(fp2, "%lld\n", ans);
	}

	fclose(fp);
	fclose(fp2);
	return 0;
}
