// I'm too sleepy... Let's try a greedy solution

#include <stdio.h>

#define MAX 1000

long m[MAX];
long n[MAX];

void quicksort(long x[MAX], int first, int last){
 int pivot, j, temp, i;
 if (first < last){
  pivot = first;
  i = first;
  j = last;
  while (i < j){
   while (x[i] <= x[pivot] && i<last)
    i++;
   while (x[j]>x[pivot])
    j--;
   if (i < j){
    temp = x[i];
    x[i] = x[j];
    x[j] = temp;
   }
  }
 
  temp = x[pivot];
  x[pivot] = x[j];
  x[j] = temp;
  quicksort(x, first, j - 1);
  quicksort(x, j + 1, last);
 }
}
 

int main() {
  FILE *rf = fopen("A-big-practice.in", "r");
  FILE *wf = fopen("A-big-practice.out", "w");
  int t, c, i, j, cols;
  int dw,w;

  fscanf(rf, "%d", &t);
  double ss, temp;
  for (c=1; c<=t; c++) {

    fscanf(rf, "%d", &cols);
    for (i=0; i<cols; i++) {
		fscanf(rf, "%lf", &ss);
		m[i] = ss*100000;
	}
	quicksort(m, 0, cols - 1);
    for (i=0; i<cols; i++) {
		fscanf(rf, "%lf", &ss);
		n[i] = ss*100000;
	}
	quicksort(n, 0, cols - 1);

	// count dw
	j = 0; dw = 0; i =0;
	while (i < cols && j < cols)
	{
		if (m[i] > n[j]) {
			dw++;
			i++;
			j++;
		} else {
			i++;
		}
	}

	// count w
	j = 0; w = 0; i =0;
	while (i < cols && j < cols)
	{
		if (m[i] < n[j]) {
			i++;
			j++;
		} else {
			while (n[j] < m[i] && j < cols) {
				w++;
				j++;
			}
		}
	}

    fprintf(wf, "Case #%d: %d %d\n", c, dw, w);
  }
  fclose(rf);
  fclose(wf);

  return 0;
}
