#include <stdio.h>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>
#include <stack>
#include <map>
#include <set>
using namespace std;

int N,M,A[10010];

int main()
{
	freopen ("input.txt","r",stdin);
	freopen ("output.txt","w",stdout);

	int Test; scanf ("%d",&Test);
	for (int Case=1;Case<=Test;Case++){
		scanf ("%d %d",&N,&M);
		for (int i=0;i<N;i++) scanf ("%d",&A[i]);
		sort(A,A+N);

		int ans = 0;
		for (int i=N-1;i>=0;i--) if (A[i] != -1){
			int ind = -1;
			for (int j=i-1;j>=0;j--) if (A[j] != -1 && A[i] + A[j] <= M){
				ind = j; break;
			}
			A[i] = -1;
			if (ind != -1){
				A[ind] = -1;
			}
			ans++;
		}

		printf ("Case #%d: %d\n",Case,ans);
	}

	return 0;
}