#include <stdio.h>
#include <set>
#include <string>
#include <vector>
#define MM 8
using namespace std;
int M, N, r, rc;
string d[MM];
char str[16];
int path[MM];
void back(int p)
{
	if (p < M) {
		for (path[p] = 0; path[p] < N; path[p]++)
			back(p+1);
	}
	else {
		int i, j, k, rr;
		
		rr = 0;
		for (i = 0; i < N; i++) {
			set<string> s; s.clear();
			for (j = 0; j < M; j++) {
				if (path[j] == i) {
					for (k = 0; k <= d[j].length(); k++)
						s.insert(d[j].substr(0,k));
				}
			}
			rr += s.size();
		}
		if (rr > r) {r = rr; rc = 1;}
		else if (rr == r) rc++;
	}
}
int main()
{
	freopen("input.txt","r",stdin);
	FILE *out=fopen("output.txt","w");
	int t, T, i, j, k;
	
	scanf("%d",&T);
	for (t = 1; t <= T; t++) {
		printf("%d\n",t);
		fprintf(out,"Case #%d: ",t);
		scanf("%d%d",&M,&N);
		for (i = 0; i < M; i++) {
			scanf("%s",str);
			d[i] = str;
		}
		r = 0; rc = 0;
		back(0);
		fprintf(out,"%d %d\n",r,rc);
	}
	fclose(out);
	return 0;
}