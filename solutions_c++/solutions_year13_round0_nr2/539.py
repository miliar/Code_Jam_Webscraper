#include<cstdio>
#include<algorithm>
using namespace std;

int T;
int N, M, A[100][100];
int B[100][100];

int main()
{
	scanf("%d", &T);
	for(int t=0;t++<T;){
		scanf("%d%d", &N, &M);
		for(int i=0;i<N;i++) for(int j=0;j<M;j++) B[i][j] = 100;

		for(int i=0;i<N;i++)
			for(int j=0;j<M;j++) scanf("%d", &(A[i][j]));

		for(int i=0;i<N;i++){
			int h = 0;
			for(int j=0;j<M;j++) h = max(h, A[i][j]);
			for(int j=0;j<M;j++) B[i][j] = min(B[i][j], h);
		}
		for(int i=0;i<M;i++){
			int h = 0;
			for(int j=0;j<N;j++) h = max(h, A[j][i]);
			for(int j=0;j<N;j++) B[j][i] = min(B[j][i], h);
		}

		bool ret = true;
		for(int i=0;i<N;i++)
			for(int j=0;j<M;j++) if(A[i][j] != B[i][j]) ret = false;

		printf("Case #%d: %s\n", t, ret ? "YES" : "NO");
	}

	return 0;
}
