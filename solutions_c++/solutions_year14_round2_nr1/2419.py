#include <stdio.h>
#include <string.h>
#include <algorithm>

using namespace std;

int main()
{
	//freopen("input.txt","r",stdin);
	freopen(".\\DATA\\codejam_round1B\\A-small-attempt1.in","r",stdin);
	freopen("output.txt","w",stdout);

	int t;
	scanf("%d",&t);
	for (int z=1; z<=t; z++) {
		int n,L=0;
		char M[110][110]={0};
		int A[110][110]={0};
		scanf("%d",&n);
		for (int i=1; i<=n; i++) {
			scanf("%s",M[i]+1);
			int idx=1;
			for (int j=1; M[i][j]; j++) {
				A[i][idx]++;
				if (M[i][j] != M[i][j+1]) { idx++; }
			}
			if (i==1) { L = idx; }
			else if (L!=idx) {
				L = -1;
				break;
			}
		}
		
		bool flag=(L<0);


		int Idx[110]={0};
		for (int i=1; i<=L; i++) {
			for (int j=2; j<=n; j++) {
				if (M[j-1][Idx[j-1]+1] != M[j][Idx[j]+1]) {
					flag = true;
					break;
				}
			}
			for (int j=1; j<=n; j++) {
				Idx[j] += A[j][i];
			}
			if (flag) { break; }
		}
		
		printf("Case #%d: ",z);
		if (flag) { printf("Fegla Won\n"); }
		else {
			int ret=0;
			for (int i=1; i<=L; i++) {
				double sum=0;
				for (int j=1; j<=n; j++) { sum += A[j][i]; }
				sum = (int)((sum/n)+0.5);
				for (int j=1; j<=n; j++) { ret += abs(sum-A[j][i]); }
			}
			printf("%d\n",ret);
		}

	}
}

