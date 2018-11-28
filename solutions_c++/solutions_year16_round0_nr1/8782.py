#include <bits/stdc++.h>

using namespace std;

int dig[11];

bool totalcount(long long int x) {
	while(x) {
		dig[x%10]++;
		x /= 10;
	}
	for(int i = 0; i < 10; ++i)
		if(dig[i] == 0)	return false;
	return true;
}

int main(void) {

	FILE *fpi, *fpo;
	fpi = fopen("A-large.in", "r");
	fpo = fopen("output.out", "w+");

	int t;
	fscanf(fpi, "%d", &t);

	for(int tt = 1; tt <= t; ++tt) {
		memset(dig, 0, sizeof(dig));
		long long int n;
		fscanf(fpi, "%lld", &n);
		if(n == 0) {
			//cout<<"Test Case "<<tt<<": "<<"INSOMNIA\n";
			fprintf(fpo, "Case #%d: INSOMNIA\n", tt);
		}
		else {
			long long int i = 2;
			long long int nn = n;
			while(true) {
				if(totalcount(nn)) {
					//cout<<"Test Case "<<tt<<": for "<<n<<" "<<nn<<"\n";
					fprintf(fpo, "Case #%d: %lld\n", tt, nn);
					break;
				}
				else {
					nn = i*n;
					++i;
				}
			}
		}
	}
	fclose(fpi);
	fclose(fpo);

	return 0;

}