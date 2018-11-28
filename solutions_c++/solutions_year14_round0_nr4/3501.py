#include <stdio.h>

double* sort(double *str, int len) {
	for (int i = 0; i < len; i++) {
		for (int j = 0; j < len - 1; j++) {
			if (str[j] > str[j+1]) {
				double temp = str[j];
				str[j] = str[j+1];
				str[j+1] = temp;
			}
		}
	}
	return str;
}

int ken(double num, double *str2, int n) {
	int result = -1;
	for (int i = 0; i < n - 1; i++) {
		if (num < str2[0]) {
			result = 0;
			break;
		} else if (str2[i] <= num && str2[i + 1] >= num) {
			result = i + 1;
			break;
		}
	}
	return result;	
}

int War(int num, double *str1, double *str2) {
	double *arr2 = new double[num];
	for (int i = 0; i < num; i++) {
		arr2[i] = str2[i];
	}
	int count = 0;
	if (num == 1) {
		if (str1[0] > arr2[0]) {
			count++;
		}
	} else {
		for (int i = 0; i < num; i++) {
			int result = ken(str1[i], arr2, num);
			if (result != -1) {
				arr2[result] = 0;
			} else {
				count++;
				for (int j = 0; j < num; j++) {
					if (arr2[j] != 0) {
						arr2[j] = 0;
						break;
					}
				}
			}
		}
	}
	return count;
}

int DeceitfulWar(int num, double *str1, double *str2) {
	int count = 0;
	double *arr1 = new double[num];
	double *arr2 = new double[num];
	for (int j = 0; j < num; j++) {
		arr1[j] = str1[j];
		arr2[j] = str2[j];
	}
	for (int i = num - 1; i >= 0; i--) {
		if (arr1[i] > arr2[i]) {
			count++;
			continue;
		} else {
			double *arr3 = new double[i];
			double *arr4 = new double[i];
			for (int j = 1; j <= i; j++) {
				arr3[j - 1] = arr1[j];
				arr4[j - 1] = arr2[j - 1];
			}
			count += DeceitfulWar(i, arr3, arr4);
			break;
		}
	}
	return count;
}


int main() {
	freopen ("D-large.in","r",stdin);
	freopen ("D-large.out", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int i = 0; i < t; i++) {
		int N;
		scanf("%d", &N);
		double *str1 = new double[N];
		double *str2 = new double[N];
		for (int j = 0; j < N; j++) {
			scanf("%lf", &str1[j]);
		}
		for (int j = 0; j < N; j++) {
			scanf("%lf", &str2[j]);
		}
		double *arr1 = new double[N];
		double *arr2 = new double[N];
		arr1 = sort(str1, N);
		arr2 = sort(str2, N);

		printf("Case #%d: %d %d\n",i + 1, DeceitfulWar(N, arr1, arr2), War(N, arr1, arr2));

	}

	fclose(stdout);
	return 0;
}