///*
#include <stdio.h>
#include <vector>
#include <string>
#include <set>

using namespace std;

int N, M;
char D[10][100];
int check[100005];
set<string> Set[4];

int solve()
{
	for(int i = 1; i <= 100000; i++) check[i] = 0;
	int T[10]={0};
	while( T[M+1] == 0){
		int ans = 0;
		for(int i = 0; i < N; i++) Set[i].clear();
		for(int i = 1; i <= M; i++){
			string s;
			for(int j = 1; j <= strlen(D[i]+1); j++){
				s.push_back(D[i][j]);
				if(Set[T[i]].find(s) == Set[T[i]].end()){
					if(Set[T[i]].empty()) ans++;
					ans++;
					Set[T[i]].insert(s);
				}
			}
		}
		check[ans]++;

		if(N == 1)break;
		T[1]++;
		int ad = 1;
		while(T[ad] == N){
			T[ad] = 0; T[ad + 1]++;
			ad++;
		}
	}
	for(int i = 100000; i >= 0; i--){
		if(check[i] != 0){
			printf("%d %d\n", i, check[i]);
			return 0;
		}
	}
	printf("0 0\n");
}

int main()
{
	freopen("input.txt","r",stdin);
//	freopen("output.txt","w",stdout);

	int T;
	scanf("%d", &T);

	for(int t = 1; t <= T; t++){
		printf("Case #%d: ", t);
		scanf("%d%d", &M, &N);
		for(int i = 1; i <= M; i++){
			scanf("%s", D[i] + 1);
		}
		solve();
	}
	return 0;
}

//*/