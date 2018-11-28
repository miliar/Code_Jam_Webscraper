#include <cstdio>
int t;
int **a, **b;
void write(int n, int m){
	int j, k;
	for (j = 0; j<=m; j++){
			for (k=0; k<=n; k++)
				printf("%d ",a[j][k]);
			printf ("\n");
		}
	printf ("\n");
	for (j = 0; j<=m; j++){
		for (k=0; k<=n; k++)
			printf("%d ",b[j][k]);
		printf ("\n");
	}
	printf ("\n");
}

void cut_h(int n, int m){
	int j, k;
	for (j = 0; j<m; j++)
		for (k = 0; k<n; k++)
			b[j][k] = a[j][n];
}
void cut_v(int n, int m){
	int j, k;
	for (j = 0; j<n; j++)
		for (k = 0; k<m; k++)
			if (b[k][j] > a[m][j])
				b[k][j] = a[m][j];
}
bool compare(int **x, int **y, int m, int n){
	int j, k;
	for (j = 0; j<m; j++)
		for (k = 0; k<n; k++)
			if (x[j][k] != y[j][k]) return false;
	return true;
}
void find_max(int ** c, int n, int m){
	int max, j, k;
	for (j = 0; j<m; j++){
		max = -1;
		for (k = 0; k<n; k++)
			if (c[j][k]>max) max = c[j][k];
		c[j][k] = max;
	}
	for (j = 0; j<n; j++){
		max = -1;
		for (k = 0; k<m; k++)
			if (c[k][j]>max) max = c[k][j];
		c[k][j] = max;
	}
}

void read(){
	int n, m, i, j, k;
	FILE *f = fopen ("B-large.in", "r");
	FILE *g = fopen ("B-large.out", "w");
	fscanf (f, "%d", &t);
	for (i = 1; i<=t; i++){
		fscanf (f, "%d%d", &m,&n);
		a = new int*[m+1];
		b = new int*[m+1];
		for (j = 0; j<m; j++){
			a[j] = new int[n+1];
			b[j] = new int[n+1];
			for (k = 0; k<n; k++){
				fscanf (f, "%d", &a[j][k]);
				b[j][k] = 100;
			}
		}
		a[j] = new int[n+1];
		b[j] = new int[n+1];
		find_max (a,n,m);
		cut_h(n,m);
		cut_v(n,m);
		fprintf (g, "Case #%d: ",i);
		if (compare(a,b,m,n)) fprintf (g,"YES\n");
		else fprintf (g,"NO\n");
		delete[] a;
		delete[] b;
	}
	fclose (f);
	fclose (g);
}

int main(){
	read();
	return 0;
}