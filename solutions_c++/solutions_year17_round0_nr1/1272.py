#include<stdio.h>
#include<string.h>
#include <algorithm>
#include<queue>
#include<string>
#include<math.h>
#include<vector>
#include <map>
#include <stack>
#include<set>

using namespace std;

char a[1111];
int b[1111];
int main() {
	int tc, t, i, j;
	FILE *fp1,*fp2;
	fp1= fopen("1.in", "r");
	fp2 = fopen("2.out","w");
	fscanf(fp1, "%d", &tc);
	for (t = 1; t <= tc; t++) {
		int k,dap=0;
		memset(b, 0, sizeof(b));
		fscanf(fp1,"%s %d",a,&k );
		fprintf(fp2, "Case #%d: ", t);
		int l = strlen(a);
		for (i = 0; i < l; i++) {
			if (a[i] == '+')b[i] = 1;
			else b[i] = 0;
		}
		for (i = 0; i < l-k+1; i++) {
			if (b[i])continue;
			dap++;
			for (j = i; j < i + k; j++) {
				b[j] = (b[j] + 1) % 2;
			}
		}
		for (i = 0; i < l; i++) {
			if (!b[i]) {
				fprintf(fp2, "IMPOSSIBLE\n");
				break;
			}
		}
		if(i==l)
			fprintf(fp2, "%d\n",dap);
	}
	fclose(fp1);
	fclose(fp2);
}


