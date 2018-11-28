#include <cstdio>
#include <cstring>
#include <algorithm>

int P[41538];

char arr[16];
long long Val;

int prime() {
	bool flag;
	int count = 0;
	for (int i = 2; i <= 500000; i++) {
		flag = true;
		for (int j = 2; j < i; j++) {
			if (i%j == 0) {
				flag = false;
				break;
			}
		}
		if (flag) {
			P[count] = i;
//			printf("%d, ", i);
			count++;
//			if (count % 15 == 0) printf("\n");
		}
	}
//	printf("\n\n %d\n", count);
	return 0;
}

inline void make_arr(int order) {
	arr[0] = arr[15] = '1';
	for (int i = 14; i >= 1; i--) {
		arr[i] = (order % 2) + '0';
		order /= 2;
	}
}

inline long long getval(int base) {
	long long retval(0);
	for (int i = 0; i <= 15; i++) {
		retval *= base;
		retval += (arr[i] - '0');
	}
	return retval;
}

int main() {
	prime();
	//FILE *fi = fopen("sample.in", "r");
	//FILE *fi = fopen("C-large.in", "r");
	FILE *fi = fopen("C-small-attempt1.in", "r");
	FILE *fo = fopen("output.txt", "w");

	int T;
	int N, J;
	int count(0); // the number of answers
	int divider[11]; // use 2~10
	fscanf(fi, "%d", &T);
	for (int t = 1; t <= T; t++) {
		fscanf(fi, "%d %d", &N, &J);
		fprintf(fo, "Case #%d:\n", t);
		for (int i = 0; i <= 1024 * N - 1; i++) {
			bool flag(false);
			make_arr(i);
			for (int j = 2; j <= 10; j++) {
				Val = getval(j);
				flag = false;
				for (int p = 0; p < 41538; p++) {
					if (Val <= P[p]) break;
					if (Val % P[p] == 0) {
						flag = true;
						divider[j] = P[p];
						break;
					}
				}
				if (flag == false) break;
			}
			if (flag) {
				if (count < 50) {
					fprintf(fo, "%*.*s", N, N, arr);
					for (int j = 2; j <= 10; j++) {
						fprintf(fo, " %d", divider[j]);
					}
					fprintf(fo, "\n");
					count++;
				}
				else goto END;
			}
		}
		
	}
END:
	fclose(fi);
	fclose(fo);
	return 0;
}
