#include<stdio.h>
#include<vector>
#include<string.h>
#include<math.h>
#define MAX 100
#define BASE 10


using namespace std;

int radixsort(int a[], int n)
{
	int i, b[MAX], m = a[0], exp = 1;
	//Get the greatest value in the array a and assign it to m
	for (i = 1; i < n; i++)
	{
		if (a[i] > m)
			m = a[i];
	}

	//Loop until exp is bigger than the largest number
	while (m / exp > 0)
	{
		int bucket[BASE] = { 0 };

		//Count the number of keys that will go into each bucket
		for (i = 0; i < n; i++)
			bucket[(a[i] / exp) % BASE]++;

		//Add the count of the previous buckets to acquire the indexes after the end of each bucket location in the array
		for (i = 1; i < BASE; i++)
			bucket[i] += bucket[i - 1];

		//Starting at the end of the list, get the index corresponding to the a[i]'s key, decrement it, and use it to place a[i] into array b.
		for (i = n - 1; i >= 0; i--)
			b[--bucket[(a[i] / exp) % BASE]] = a[i];

		//Copy array b to array a
		for (i = 0; i < n; i++)
			a[i] = b[i];

		//Multiply exp by the BASE to get the next group of keys
		exp *= BASE;
	}
	return a[n / 2];
}


int main() {
	char str[100][100];
	int count[100][100];
	double sum[100];
	char checker[100];
	char buf[100];
	int w[100];

	int T, i, j, k,N,c, a;
	bool b;
	int move;

	FILE* f1= fopen("A-small-attempt1.in", "r+");
	FILE* f2 = fopen("A-small-attempt1.out", "w+");
	fscanf(f1, "%d", &T);
	for (j = 0; j < T; j++) {
		b = true;
		fscanf(f1,"%d" ,&N);
		for (i = 0; i < 100; i++) {
			sum[i] = 0;
			checker[i] = 0; 
			buf[i] = 0;
			for (k = 0; k < N; k++) str[k][i] = 0;
		}
		move = 0;

		for (i = 0; i < N; i++) {
			fscanf(f1, "%s", &str[i]);

			for (k = 0; k < 100; k++) {
				count[i][k] = 0;
				buf[k] = 0;
			}

			if (i ==0 )  checker[0] = str[i][0];
			buf[0] = str[i][0];
			count[i][0] ++;
			sum[0]++;
			c = 0;
			for (k = 1; k < strlen(str[i]); k++) {

				if (str[i][k] == str[i][k - 1]) {
					count[i][c]++;
					sum[c] ++;
				}

				else {
					count[i][++c]++;
					sum[c]++;
					if (i == 0) checker[c] = str[i][k];
					buf[c] = str[i][k];
				}

			}
			if (strcmp(buf, checker) != 0) {
				fprintf(f2, "Case #%d: Fegla Won\n", j + 1);
				b = false;
				break;
			}
		}
		int temp;

		if (b) {
			/*

			for (i = 0;; i++) {
				if (checker[i] == 0) break;
				for (k = 0; k < N; k++) w[k] = count[k][i];
				temp = radixsort(w, N);
				for (k = 0; k < N; k++) {
					move += abs(count[k][i] -temp);
				}

			}*/

			/*
			for (i = 0; i < 100; i++) {
				if (checker[i] == 0) break;

				sum[i] = floor(sum[i] / N);
				for (k = 0; k < N; k++) {
					move += abs(count[k][i] - sum[i]);
				}
			}*/
			for (i = 0;; i++) {
				if (checker[i] == 0) break;
				move += abs(count[1][i] - count[0][i]);
			}
			fprintf(f2, "Case #%d: %d\n", j + 1, move);
		}
	}

	fclose(f1);
	fclose(f2);

}