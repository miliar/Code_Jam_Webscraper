#include <stdio.h>
#include <algorithm>
using namespace std;

int N,D;
long long S[1000001],M[1000001];
int C[2000002],L[1000001],R[1000001];

int main()
{
	freopen ("input.txt","r",stdin);
	freopen ("output.txt","w",stdout);

	int Test; scanf ("%d",&Test); for (int Case=1;Case<=Test;Case++){
		printf ("Case #%d: ",Case);

		scanf ("%d %d",&N,&D);
		long long a,c,r;
		scanf ("%d %lld %lld %lld",&S[0],&a,&c,&r);
		L[0] = R[0] = S[0];
		for (int i=1;i<N;i++){
			S[i] = (S[i-1] * a + c) % r;
			L[i] = R[i] = S[i];
		}
		scanf ("%d %lld %lld %lld",&M[0],&a,&c,&r);
		for (int i=1;i<N;i++){
			M[i] = (M[i-1] * a + c) % r;
		}

		for (int i=0;i<=2000001;i++) C[i] = 0;
		for (int i=0;i<N;i++){
			if (i){
				M[i] %= i;
				L[i] = min(L[M[i]],L[i]);
				R[i] = max(R[M[i]],R[i]);
			}
			if (R[i] - L[i] <= D){
				int l = R[i] - D;
				if (l < 1) l = 0;
				C[l]++;
				int r = L[i] + 1;
				C[r]--;
			}
		}

		int ans = 0;
		for (int i=0;i<=2000001;i++){
			if (i) C[i] += C[i-1];
			ans = max(ans,C[i]);
		}
		printf ("%d\n",ans);
	}

	return 0;
}