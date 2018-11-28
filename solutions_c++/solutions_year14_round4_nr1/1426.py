#include <cstdio>
#include <cstdlib>
#include <algorithm>
#define MAX 11234

using namespace std;

int main(){
	int T, N, X;
	int v[MAX];
	scanf("%d", &T);
	for(int t = 1; t <= T; t++){
		scanf("%d%d", &N, &X);
		for(int i = 0; i < N; i++)
			scanf("%d", &v[i]);
		sort(v, v+N);
		int cnt = 0;
		int p1 = 0, p2 = N-1;
		while(p1 <= p2){
			cnt++;
			if(v[p1] + v[p2] <= X){
				p1++;
				p2--;
			}
			else{
				p2--;
			}
		}
		printf("Case #%d: %d\n", t, cnt);
	}
	return 0;
}

