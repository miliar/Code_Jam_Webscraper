#include <cstdio>
#include <cstdlib>

long long unsigned gcd(long long unsigned p, long long unsigned q) {
	long long unsigned t = 0;
	if(q == p) return q;
	if(p < q)
		t = gcd(p, q - p);
	else
		t = gcd(p - q, q);
	return t;
}

int main() {
    int T, iter;
    FILE *in = fopen("input", "r"), *out = fopen("output", "w");
    long long unsigned p, q, t;
    double r;
    fscanf(in, "%d", &T);
    for(iter = 0; iter < T; iter++) {
    	fscanf(in, "%llu/%llu\n", &p, &q);
    	printf("%llu %llu\n", p, q);
    	t = gcd(p, q);
    	p = p / t;
    	q = q / t;
    	t = 0;
    	r = p * 1.0 / q;
    	int s = 0;
    	printf("%d\n",s);
    	while(r < 1) {
    		r *= 2;
    		s++;
    	}
    	/*while(q) {
    		q = q / 2;
    		t++;
    	}
    	printf("%llu\n",t);*/
    	while(q) {
    		if(q != 1 && q % 2) {
    			s = 0;
    		}
    		q /= 2;
    	}
    	if(s) {
    		fprintf(out, "Case #%d: %d\n", iter + 1, s);
    	}
    	else {
    		fprintf(out, "Case #%d: impossible\n", iter + 1);
    	}
    }
    fclose(in);
    fclose(out);
    return 0;
}