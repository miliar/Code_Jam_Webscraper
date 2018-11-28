#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <vector>
#define MAX 1010

using namespace std;

int main(){
	int T, t;
	scanf("%d", &T);
	for(t = 1; t <= T; t++){
		int N;
		scanf("%d", &N);
		double v1[MAX], v2[MAX];
		for(int i = 0; i < N; i++)
			scanf("%lf", &v1[i]);
		for(int i = 0; i < N; i++)
			scanf("%lf", &v2[i]);

		sort(v1, v1+N);
		sort(v2, v2+N);

		int i1 = 0, i2 = N-1;
		int sc1 = 0;
		int sc2 = 0;
		for(int i = 0; i < N; i++){
			if(v1[i] > v2[i1]){
				sc1++;
				i1++;
			}
			else{
				i2--;
			}
		}
		int m[MAX];
		for(int i = 0; i < N; i++)
			m[i] = 1;
		for(int i = 0; i < N; i++){
			int k = 0;
			for(int j = 0; j < N; j++){
				if(m[k] == 0 && m[j] != 0)
					k = j;
				if(m[j] != 0 && v2[k] < v1[i] && v2[j] > v1[i])
					k = j;
			}
			if(v2[k] < v1[i])
				sc2++;
			m[k] = 0;
		}

		printf("Case #%d: %d %d\n", t, sc1, sc2);
	}
	return 0;
}
