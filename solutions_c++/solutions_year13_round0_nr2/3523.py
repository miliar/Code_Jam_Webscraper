#include <cstdio>

using namespace std;

int N, M;
int B[128][128];

int main()
{
	int T;
	
	scanf("%d", &T);
	
	for (int testnum = 1; testnum <= T; testnum++){
		scanf("%d %d", &N, &M);
		
		for (int i = 0; i < N; i++)
			for (int j = 0; j < M; j++)
				scanf("%d", &B[i][j]);
		
		bool ok = true;
		for (int i = 0; i < N; i++){
			for (int j = 0; j < M; j++){
				bool ng1 = false, ng2 = false;
				for (int x = 0; x < N; x++)
					if (B[x][j] > B[i][j]) ng1 = true;
				for (int x = 0; x < M; x++)
					if (B[i][x] > B[i][j]) ng2 = true;
				if (ng1 && ng2) ok = false;
			}
		}
		
		printf("Case #%d: %s\n", testnum, ok ? "YES" : "NO");
	}
	
	return (0);
}
