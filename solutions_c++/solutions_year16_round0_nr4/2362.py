#include <bits/stdc++.h>
#ifdef DEBUG
#define D(x...) fprintf(stderr,x) 
#else
#define D(x...)
#endif
using namespace std;
int T, K, C, S;
int main ()
{
	freopen("infile.txt", "r", stdin);
	freopen("outfile.txt", "w", stdout);
	scanf("%d", &T);
	for(int t=1; t<=T; t++)
	{
		scanf("%d %d %d ", &K, &C, &S);
		printf("Case #%d:",t);
		for(int s=1; s<=S; s++)
		{
			printf(" %d", s);
		}
		printf("\n");
		D("solved %d\n", t);
	}
}