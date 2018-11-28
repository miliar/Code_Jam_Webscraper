#include <vector>
#include <algorithm>
#include <stdio.h>
#include <string>
#include <math.h>

#ifndef min
#define min(A,B) B < A ? B : A
#endif
#ifndef s
#define s(...) fscanf(in, __VA_ARGS__)
#endif
#ifndef p
#define p(...) fprintf(out, __VA_ARGS__)
#endif

using namespace std;

FILE *in, *out;
long long r, t, res;
double aux;

int counter = 0;
void make() {
    p("Case #%d: ", ++counter);
    s("%lld %lld", &r, &t);
	aux = (double)(2*r-1);
	res = floor((sqrt(aux*aux+8*t)-aux)/4);
	p("%lld\n", res);
}

int main() {
	in = fopen("A-small-attempt0.in", "r");
	out = fopen("A.out", "w");
    int t; s("%d", &t);
    while(t--) {
        make();
    }
    return 0;
}
