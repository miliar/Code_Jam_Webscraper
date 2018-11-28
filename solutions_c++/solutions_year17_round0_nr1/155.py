#include <stdio.h>
#include <map>
using namespace std;


int main()
{
	freopen ("input.txt","r",stdin);
	freopen ("output.txt","w",stdout);

	int Test; scanf ("%d",&Test); for (int Case=1;Case<=Test;Case++){
		printf ("Case #%d: ",Case);

		char S[1010];
		int N,K,P[1010] = {0,};
		scanf ("%s %d",S,&K);
		N = 0;
		while (S[N]) N++;

		int c = 0, p = 0;
		for (int i=0;i<N-K+1;i++){
			int x = (S[i] == '-');
			if ((x + p) % 2){
				P[i]++; P[i+K-1]--;
				c++;
			}
			p += P[i];
		}
		for (int i=N-K+1;i<N;i++){
			int x = (S[i] == '-');
			if ((x + p) % 2){
				puts("IMPOSSIBLE");
				c = -10000;
				break;
			}
			p += P[i];
		}
		if (c >= 0) printf ("%d\n",c);
	}

	return 0;
}