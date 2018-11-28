#include <cstdio>
#include <algorithm>
using namespace std;

int T;
int N;
double A[1050], B[1050];

int playDeceitful()
{
	for(int i=0;i<N;i++){
		for(int j=0;j<N-i;j++){
			if(A[i+j] < B[j]) goto nex;
		}
		return N-i;
nex:
		continue;
	}
	return 0;
}

int playNormal()
{
	int lp = 0;
	for(int i=0;i<N;i++){
		while(lp < N && A[i] > B[lp]) ++lp;

		if(lp == N) return N - i;

		++lp;
	}

	return 0;
}

int main()
{
	scanf("%d", &T);
	for(int t=0;t++<T;){
		scanf("%d", &N);
		for(int i=0;i<N;i++) scanf("%lf", A + i);
		for(int i=0;i<N;i++) scanf("%lf", B + i);

		sort(A, A+N);
		sort(B, B+N);

		//for(int i=0;i<N;i++) printf("%f %f\n", A[i], B[i]);

		printf("Case #%d: %d %d\n", t, playDeceitful(), playNormal());
	}
	return 0;
}
