#include <cstdio>
#include <vector>

FILE * in = fopen("in.txt", "r");
FILE * out = fopen("out.txt", "w");

using namespace std;

int main(){
	int t; fscanf(in, "%d", &t);
	for (int i = 1; i <= t; i++){
		long long n; fscanf(in, "%lld", &n);
		int chk[10] = { 0 }; 

		fprintf(out, "Case #%d: ", i);
		if (n == 0) fprintf(out, "INSOMNIA\n");
		else {
			for (long long j = 1; ; j++) {
				long long m = n * j, c = 0;

				for (long long k = 1; m / k > 0; k *= 10)
					chk[(m / k) % 10] = 1;

				for (int i = 0; i < 10; i++) c += chk[i];

				if (c == 10) {
					fprintf(out, "%lld\n", m);
					break;
				}
			}
		}
	}
}