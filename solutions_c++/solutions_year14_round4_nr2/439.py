#include <stdio.h>
#include <memory.h>
#define MN 1000
using namespace std;
int N, r;
int d[MN];
bool ch[MN];
int main()
{
	freopen("input.txt","r",stdin);
	FILE *out=fopen("output.txt","w");
	int t, T, i, j, k;
	
	scanf("%d",&T);
	for (t = 1; t <= T; t++) {
		printf("%d\n",t);
		fprintf(out,"Case #%d: ",t);
		scanf("%d",&N);
		for (i = 0; i < N; i++)
			scanf("%d",&d[i]);
		memset(ch,0,sizeof(ch));
		r = 0;
		for (i = 0; i < N; i++) {
			k = -1;
			for (j = 0; j < N; j++) {
				if (!ch[j]) {
					if (k == -1 || d[j] < d[k])
						k = j;
				}
			}
			int left = 0, right = 0;
			for (j = k-1; j >= 0; j--) {
				if (!ch[j]) left++;
			}
			for (j = k+1; j < N; j++) {
				if (!ch[j]) right++;
			}
			if (left < right) r += left;
			else r += right;
			ch[k] = 1;
		}
		fprintf(out,"%d\n",r);
	}
	fclose(out);
	return 0;
}