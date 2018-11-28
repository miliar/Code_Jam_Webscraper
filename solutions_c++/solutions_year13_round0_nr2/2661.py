#include <cstdio>
#include <algorithm>
using namespace std;

int N, M;
int a[100][100];
bool u[100][100];
int main(){
	int T;
	scanf("%d", &T);
	for(int c = 1; c <= T; c++){
	scanf("%d %d", &N, &M);
	for(int i = 0; i < N; i++) for(int j = 0; j < M; j++) u[i][j] = false;
	for(int i = 0; i < N; i++)
		for(int j = 0; j < M; j++)
			scanf("%d", &a[i][j]);
	bool OK = true;
	for(int i = 0; i < N; i++){
		if(a[i][0] == 1){
			bool f = true;
			for(int j = 0; j < M; j++){
				if(a[i][j] > 1){
					f = false;
					break;
				}
			}
			if(f) for(int j = 0; j < M; j++) u[i][j] = true;
		}
	}
	for(int j = 0; j < M; j++){
		if(a[0][j] == 1){
			bool f = true;
			for(int i = 0; i < N; i++){
				if(a[i][j] > 1){
					f = false;
					break;
				}
			}
			if(f) for(int i = 0; i < N; i++) u[i][j] = true;
		}
	}

	bool f = true;
	for(int i = 0; i < N; i++)
		for(int j = 0; j < M; j++)
			if(a[i][j] == 1 && !u[i][j]){
				f = false;
				break;
			}
	printf("Case #%d: %s\n", c, (f)?"YES":"NO");
	}
	return 0;
}

