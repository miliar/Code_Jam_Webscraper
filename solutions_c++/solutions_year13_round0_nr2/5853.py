#include <cstdio>
using namespace std;

int lawn[100][100];

int maxR[100];
int maxC[100];

int main()
{
	int T, N,M, a, count=1;
	scanf("%d", &T);
	while(T--) {
		scanf("%d %d",&N,&M);
		for(int i=0;i<N;i++) maxR[i] = 0;
		for(int i=0;i<M;i++) maxC[i] = 0;
		for(int i=0;i<N;i++) {
			for(int j=0;j<M;j++) {
				scanf("%d", &a);
				lawn[i][j] = a;
				maxR[i] = (maxR[i] < a)? a:maxR[i];
				maxC[j] = (maxC[j] < a)? a:maxC[j];
				}
			}
		bool valid = true;
		for(int i=0;i<N;i++) {
			for(int j=0;j<M;j++) {
				if ((lawn[i][j] <maxR[i]) && (lawn[i][j] <maxC[j])) {
					valid = false;
					break;
				}
			}
			if (!valid) break;
		}
		printf("Case #%d: %s\n", count++, (valid?"YES":"NO"));
	}
	return 0;
}