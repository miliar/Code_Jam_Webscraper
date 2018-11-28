#include <stdio.h>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>
#include <stack>
#include <map>
#include <set>
using namespace std;

int N,A[1010],S[1010][1010],R[1010],D[1010][1010];
pair<int, int> P[1010];

int sum(int a1, int a2, int b1, int b2){return S[a2][b2] - S[a1-1][b2] - S[a2][b1-1] + S[a1-1][b1-1];}

int main()
{
	freopen ("input.txt","r",stdin);
	freopen ("output.txt","w",stdout);

	int Test; scanf ("%d",&Test);
	for (int Case=1;Case<=Test;Case++){
		scanf ("%d",&N);
		for (int i=1;i<=N;i++) scanf ("%d",&A[i]), P[i] = make_pair(A[i],i);
		sort(P+1,P+1+N);
		for (int i=0;i<=N;i++) for (int j=0;j<=N;j++) S[i][j] = 0;
		for (int i=1;i<=N;i++) S[i][P[i].second] = 1, R[i] = P[i].second;
		for (int i=1;i<=N;i++) for (int j=1;j<=N;j++) S[i][j] += S[i-1][j] + S[i][j-1] - S[i-1][j-1];
		for (int l=1;l<=N;l++){
			for (int i=0,j=l;i<=l;i++,j--){
				D[i][j] = 0x7fffffff;
				if (i > 0) D[i][j] = min(D[i][j],D[i-1][j]+sum(l,N,1,R[l])-1);
				if (j > 0) D[i][j] = min(D[i][j],D[i][j-1]+sum(l,N,R[l],N)-1);
			}
		}
		
		int ans = 0x7fffffff;
		for (int i=0;i<N;i++) ans = min(ans,D[i][N-i]);

		printf ("Case #%d: %d\n",Case,ans);
	}

	return 0;
}