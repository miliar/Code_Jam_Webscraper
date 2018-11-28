#include <cstdio>
#include <algorithm>

int T, N, cnt;
bool chk[10];

int main(){
	FILE *fin = fopen("A-large.in", "r");
	FILE *fout = fopen("A-large.out", "w");
	long long tmp, tmp2, c;

	fscanf(fin, "%d", &T);
	
	for (int i = 1; i <= T; ++i){
		fscanf(fin, "%d", &N);

		memset(chk, false, 10);

		cnt = 0, tmp = N;
		while (tmp>0){
			if (chk[tmp % 10] == false){
				chk[tmp % 10] = true;
				cnt++;
			}
			tmp /= 10;
		}

		tmp = N;
		c = 0;
		while (cnt != 10 && c<100000){
			tmp += N;
			tmp2 = tmp;
			while (tmp2>0){
				if (chk[tmp2 % 10] == false){
					chk[tmp2 % 10] = true;
					cnt++;
				}
				tmp2 /= 10;
			}
			c++;
		}

		fprintf(fout, "Case #%d: ",i);
		if (cnt == 10)	fprintf(fout, "%lld\n", tmp);
		else	fprintf(fout, "INSOMNIA\n");
	}

	fclose(fin);
	fclose(fout);

	return 0;
}