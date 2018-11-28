#include<stdio.h>
int main(){
	
	int t;
	FILE *in, *out;

	in = fopen("B-small-attempt0.in", "r");
	out = fopen("output.txt", "w");

	fscanf(in, "%d", &t);
	for (int z = 0; z < t; z++){
		int k, l, s, p = 0, m=-1, c[26] = { 0, };
		double ans = 1.;
		char a[101], b[101];
		fscanf(in, "%d %d %d", &k, &l, &s);
		fscanf(in, "%s", a);
		fscanf(in, "%s", b);

		for (int i = 0; i < k; i++){
			c[a[i] - 65]++;
		}//checking string

		for (int i = 0; i < l; i++){
			if (c[b[i] - 65] == 0){
				m = 0;
				break;
			}
		}
		if (m != 0){
			for (int i = 1; i < l; i++){
				if (b[i] == b[0]){
					for (int j = 1; j < l - i; j++){
						if (b[j] != b[i + j]){
							p = -1;
							break;
						}
					}
					if (p != -1) p = l - i;
				}
				if (p > 0) break;
			}
			if (p == -1 || p == 0) m = s / l;
			else{
				m = (s - p) / (l - p);
			}
		}//finding max
		
		for (int i = 0; i < l; i++){
			ans *= ((double)c[b[i] - 65] / (double)k);
		}
		ans *= (s - l + 1);
		fprintf(out, "Case #%d: %lf\n", z + 1, (double)m-ans);
	}

	fclose(in);
	fclose(out);

	return 0;
}