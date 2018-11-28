#include<stdio.h>

int main() {
	long long int tt, zz;
	FILE *in, *out;
	in = fopen("input.in", "r");
	out = fopen("output.txt", "w");
	fscanf(in, "%lld",&tt);
	for(zz=1;zz<=tt;zz++) {
		long long int n, t, z, i=1;
		fscanf(in, "%lld",&n);
		fprintf(out, "Case #%d: ", zz);
		int a[10] = {0};
		int rem = 10;
		if(n!=0) {
			while(rem>0) {
				t = i*n;
				z = t;
				while(t>0) {
					if(a[t%10]==0) {
						a[t%10] = 1;
						rem--;
					}
					t/=10;
				}
				i++;
			
			}
			fprintf(out, "%lld\n",z);
		}
		else {
			fprintf(out, "INSOMNIA\n");
		}
	}
}
