#include <stdio.h>
#include <cstring>
#include <vector>
#include <algorithm>

#define MAXSIZE 1001

using namespace std;
int main(){
	freopen("D-large.in", "r", stdin);
//	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T, N, res1, res2;
	
//	vector <int> a, b;
	double a[MAXSIZE], b[MAXSIZE];
	scanf("%d", &T);
	for(int test=1; test<=T; test++){
		res1 = 0;
		res2 = 0;
		scanf("%d", &N);
//		a.resize(N);
//		b.resize(N);
		for(int i=0; i<N; i++){
			scanf("%lf", &a[i]);
		}
		for(int i=0; i<N; i++){
			scanf("%lf", &b[i]);
		}
		sort(a, a+N);
		sort(b, b+N);
		int j = 0;
		for(int i=0; i<N; i++){
			if(a[i] > b[j]) {
				res1++;
				j++;
			}
		}
//		memset(c, 0, sizeof(c));
		j = 0;
		for(int i=0; i<N; i++){
			if(b[i] > a[j]){
				res2++;
				j++;
			}
		}
		res2 = N - res2;
		printf("Case #%d: %d %d\n", test, res1, res2);
	}
	return 0;
} 
