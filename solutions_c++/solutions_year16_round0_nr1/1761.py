#include <conio.h>
#include <vector>
#include <math.h>

void main () {
	int T, n;

	FILE *f_in, *f_out;
	f_in = fopen("data.txt","r");	
	f_out = fopen("output.txt","w");	
	fscanf(f_in,"%d",&T);

	for (int t = 0; t < T; ++t) {
		fscanf(f_in, "%d", &n);

		if (n == 0) {
			fprintf(f_out, "Case #%d: INSOMNIA\n", t+1);
			continue;
		}

		int bitmask = 0;
		for (int loop = 1;  ; loop++)
		{
			long long j = (long long)loop * n;
			while (j) {
				int k = j % 10;
				bitmask |= 1 << k;
				j /= 10;
			}

			if (bitmask == (1 << 10) - 1) {
				fprintf(f_out, "Case #%d: %lld\n", t+1, (long long)loop * n);
				break;
			}
		}
	}
	 

}