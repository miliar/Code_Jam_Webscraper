#include <stdio.h>
#include <stdlib.h>
int compare(const void *data1, const void *data2){
	double *p1 = (double *) data1;
	double *p2 = (double *) data2;
	if (*p1 > *p2)
		return 1;
	if (*p1 < *p2)
		return -1;
	return 0;
}
int find_min(double num, double* b, int n){
	for (int i = 0; i < n; i++){
		if (num < b[i])
			return i;
	}
	return -1;
}
void setMin(double* b){
	int i;
	for (i = 0; b[i] == -1; i++);
	b[i] = -1;
	return;
}
int play_war(double* a, double* b, int n){
	int score = 0;
	int index;
	for (int i = 0; i < n; i++){
		index = find_min(a[i], b, n);
		if (index == -1){
			setMin(b);
			score++;
		}
		else
			b[index] = -1;			
	}
	return score;
}
int play_dwar(double* a, double* b, int n){
	int score = 0;
	int i, j = 0;
	for (i = 0; i < n; i++)
		if (a[i] > b[j]){
			score++;
			j++;
		}
	return score;
}
int main(void){
	int n, t;
	double a[1010], b[1010], a1[1010], b1[1010];
	scanf("%d", &t);
	for (int k = 0; k < t; k++){
		scanf("%d", &n);
		for (int i = 0; i < n; i++)
			scanf("%lf", &a[i]);
		for (int i = 0; i < n; i++)
			scanf("%lf", &b[i]);
		qsort(a, n, sizeof(double), compare);	
		qsort(b, n, sizeof(double), compare);	
		for (int i = 0; i < n; i++)
			a1[i] = a[i];
		for (int i = 0; i < n; i++)
			b1[i] = b[i];
/*		for (int j = 0; j < n; j++)
			printf("%.3f ", a[j]);
		printf("\n");
		for (int j = 0; j < n; j++)
			printf("%.3f ", b[j]);
		printf("\n");
*/		printf("Case #%d: %d %d\n", k + 1, play_dwar(a, b, n), play_war(a1, b1, n));
	}
	return 0;
}
