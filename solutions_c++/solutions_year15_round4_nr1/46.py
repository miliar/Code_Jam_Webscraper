#include<stdio.h>
#include<algorithm>
#include<string>
#include<vector>
#include<queue>
#include<functional>

using namespace std;

typedef long long ll;
typedef pair<int,int> pii;

const int MX = 105;
char D[105][105];


int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	scanf("%d", &T);
	for(int t = 1; t <= T; t++){
		printf("Case #%d: ", t);
		int N, M, ans = 0;
		scanf("%d%d", &N, &M);
		for(int i = 1; i <= N; i++) scanf("%s", D[i] + 1);

		bool pos = true;
		for(int i = 1; i <= N; i++){
			for(int j = 1; j <= M; j++){
				if( D[i][j] != '.' ){
					int cnt = 0;
					for(int k = 1; k <= M; k++) cnt += D[i][k] != '.';
					for(int k = 1; k <= N; k++) cnt += D[k][j] != '.';
					if(cnt == 2) pos = false;
				}
			}
		}
		if( !pos ){
			printf("IMPOSSIBLE\n");
			continue;
		}

		for(int i = 1; i <= N; i++){
			int j;
			for(j = 1; j <= M; j++){
				if( D[i][j] != '.' ) break;
			}
			if( j == M+1 ) continue;
			if( D[i][j] == '<' ) ans++;
		}
		
		for(int i = 1; i <= N; i++){
			int j;
			for(j = M; j >= 1; j--){
				if( D[i][j] != '.' ) break;
			}
			if( j == 0 ) continue;
			if( D[i][j] == '>' ) ans++;
		}
		
		for(int j = 1; j <= M; j++){
			int i;
			for(i = 1; i <= N; i++){
				if( D[i][j] != '.' ) break;
			}
			if( i == N+1 ) continue;
			if( D[i][j] == '^' ) ans++;
		}

		for(int j = 1; j <= M; j++){
			int i;
			for(i = N; i >= 1; i--){
				if( D[i][j] != '.' ) break;
			}
			if( i == 0 ) continue;
			if( D[i][j] == 'v' ) ans++;
		}
		printf("%d\n", ans);
	}
	return 0;
}