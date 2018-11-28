#include <stdint.h>
#include <stdio.h>
#include <string>
#include <math.h>

typedef unsigned long long llu;

using namespace std;

FILE *in, *out;

int T, t;
llu A, B, res;

bool eh_palim(llu x) {
	llu pd, ud, aux;
	int N = (int)log10(x)+1;
	int it = 0, N1;
	while (N > 0) {
		ud = x % 10;
		aux = (llu)pow(10, N-1);
		N1 = (int)log10(x)+1;
		if (N == N1)
			pd = x / aux;
		else
			pd = 0;
		if (pd != ud)
			return false;
		if (N == N1)
			x -= pd*aux;
		x /= 10;
		N -= 2;
		it++;
	}
	return true;
}

llu transforma_palim(llu x) {
	while (!eh_palim(x))
		x++;
	return x;
}

llu prox_palim(llu p) {
	int N = (int)log10(p)+1;
	llu fh = p / (llu)pow(10, N/2);
	fh++;
	if (fh == (llu)pow(10, (N+1)/2)) {
		N++;
		if (N % 2 == 0)
			fh /= 10;
	}
	llu aux = fh;
	if (N % 2 == 1)
		aux /= 10;
	while (aux > 0) {
		fh = 10*fh + aux%10;
		aux /= 10;
	}
	return fh;
}

llu sum_palim() {
	llu p = transforma_palim(ceil(sqrt(A)));
	llu max = floor(sqrt(B));
	llu sum = 0;
	while (p <= max) {
		if (eh_palim(p*p)) {
			sum++;
		}
		p = prox_palim(p);
	}
	return sum;
}

int main() {
	in = fopen("C-large-1.in", "r");
	out = fopen("C.out", "w");
	fscanf(in, "%d ", &T);
	
	for(int t = 1; t <= T; ++t)
	{
		fscanf(in, "%llu %llu ", &A, &B);
		res = sum_palim();
		fprintf(out, "Case #%d: %llu\n", t, res);
	}
	
	return 0;
}
