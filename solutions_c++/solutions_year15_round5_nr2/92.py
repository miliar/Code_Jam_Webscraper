#include <stdio.h>
#include <algorithm>
using namespace std;

int N,K,sum[1010];
long long low[1010],upp[1010],now[1010];

int main()
{
	freopen ("input.txt","r",stdin);
	freopen ("output.txt","w",stdout);

	int Test; scanf ("%d",&Test); for (int Case=1;Case<=Test;Case++){
		printf ("Case #%d: ",Case);

		scanf ("%d %d",&N,&K);
		for (int i=0;i<N-K+1;i++) scanf ("%d",&sum[i]);
		for (int i=0;i<K;i++) low[i] = now[i] = upp[i] = 0;
		for (int i=1;i<N-K+1;i++){
			int v = (i-1) % K;
			now[v] += sum[i] - sum[i-1];
			low[v] = min(low[v],now[v]);
			upp[v] = max(upp[v],now[v]);
		}
		long long s = sum[0], mx = 0, c = 0;
		for (int i=0;i<K;i++){
			s += low[i];
			mx = max(mx,upp[i] - low[i]);
		}
		s = (s % K + K) % K;
		for (int i=0;i<K;i++) c += mx - (upp[i] - low[i]);
		if (s > c) mx++;
		printf ("%lld\n",mx);
	}

	return 0;
}