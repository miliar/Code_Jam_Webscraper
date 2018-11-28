#include <stdio.h>
#include <algorithm>

using namespace std;

int N,V, S[10005];

int main() {
	int T,Cas=0;
	scanf("%d",&T);
	while (T--) {
		scanf("%d%d",&N,&V);
		for (int i=0;i<N;i++)
			scanf("%d",S+i);
		sort(S,S+N);
		int tot=0, b=0;
		for (int i=N-1;i>=b;i--) {
			if (i>b)
				if (S[i]+S[b]<=V)
					b++;
			tot++;
		}
		printf("Case #%d: %d\n",++Cas,tot);
	}
}
