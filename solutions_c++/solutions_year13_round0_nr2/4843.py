#include<stdio.h>
#include<stdlib.h>
#include<math.h>

char a[110][110];
int n,m;

bool checkcross(int i, int j, char num) {
	bool deny1 = false, deny2 = false;
	int k;
	for (k=0;k<n;k++) {
		if (a[k][j] > num) {
			deny1 = true;
			break;
		}
	}
	for (k=0;k<m;k++) {
		if (a[i][k] > num) {
			deny2 = true;
			break;
		}
	}
	return ( !(deny2 && deny1) );

}

int main() {
	FILE *f;
	FILE *g;
	int i,j,testnum,testi;
	bool possible;
	fopen_s(&f,"B-large.in","r");
	fopen_s(&g,"output.txt","w");
	fscanf_s(f, "%d\n", &testnum);
	for (testi = 0; testi<testnum; testi++) {
		possible = true;
		fscanf_s(f, "%d %d\n", &n, &m);
		for (i=0;i<n;i++) {
			for (j=0;j<m;j++) {
				fscanf_s(f, "%d\n", &a[i][j]);
			}
		}
		for (i=0;i<n;i++) {
			for (j=0;j<m;j++) {
				if ( !checkcross(i,j,a[i][j]) ) {
					possible = false;
					break;
				}
			}
			if (!possible) {
				break;
			}
		}
		if (possible) {
			fprintf_s(g, "Case #%d: YES\n", testi+1);
		}
		else {
			fprintf_s(g, "Case #%d: NO\n", testi+1);
		}
	}
	fclose(f);
	fclose(g);
	return 0;
}