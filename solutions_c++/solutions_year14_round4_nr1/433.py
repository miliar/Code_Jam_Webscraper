#include <stdio.h>
#include <memory.h>
#include <algorithm>
#define MN 10000
using namespace std;
int N, X, r;
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
		scanf("%d%d",&N,&X);
		for (i = 0; i < N; i++)
			scanf("%d",&d[i]);
		sort(d,d+N);
		r = 0;
		memset(ch,0,sizeof(ch));
		for (i = 0; i < N; i++) {
			if (ch[i]) continue;
			ch[i] = true;
			for (j = N-1; j >= i+1; j--) {
				if (!ch[j] && d[i]+d[j] <= X) {
					ch[j] = 1;
					break;
				}
			}
			r++;
		}
		fprintf(out,"%d\n",r);
	}
	fclose(out);
	return 0;
}