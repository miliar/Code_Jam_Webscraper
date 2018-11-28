#include <algorithm>
#include <cstdio>
using namespace std;

int T;
int N, M;
int a[105][105];
int maxr[105];
int maxs[105];
char res[][10]={"YES", "NO"};
int vysl;

int main()
{
	scanf("%d", &T);

	for(int q=1; q<=T; q++) {
		scanf("%d%d", &N, &M);
		for(int i=0; i<N; i++) for(int j=0; j<M; j++) scanf("%d", &a[i][j]);

		for(int i=0; i<N; i++) {
			maxr[i]=a[i][0];
			for(int j=1; j<M; j++) maxr[i]=max(maxr[i], a[i][j]);
		}

		for(int j=0; j<M; j++) {
			maxs[j]=a[0][j];
			for(int i=1; i<N; i++) maxs[j]=max(maxs[j], a[i][j]);
		}

		vysl=0;

		for(int i=0; i<N; i++) for(int j=0; j<M; j++) {
			if(a[i][j]<maxr[i] && a[i][j]<maxs[j]) vysl=1;
		}

		printf("Case #%d: %s\n", q, res[vysl]);
	}

	return 0;
}
