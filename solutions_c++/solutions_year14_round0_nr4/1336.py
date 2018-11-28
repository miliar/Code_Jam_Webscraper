#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <cmath>
#include <climits>
#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <utility>
#include <algorithm>

#define MAX 1010

#define PB push_back

#define PP pair<int, int>
#define MP make_pair
#define F first
#define S second

using namespace std;

typedef long long ll;

int main(){
	int T;
	scanf("%d", &T);
	for(int i = 1; i <= T; i++){
		printf("Case #%d: ", i);	
		
		int N;
		scanf("%d", &N);
		double A[MAX], B[MAX];
		for (int i = 0; i < N; i++) scanf("%lf", &A[i]);
		for (int i = 0; i < N; i++) scanf("%lf", &B[i]);
		sort(A, A+N);
		sort(B, B+N);

		int i, j;
		for (i = j = 0; i < N; i++, j++){
			while(j < N && A[i] >= B[j]) j++;
			if (j == N) break;
		}
		int w = N-i;
		
		for (i = j = 0; i < N; i++, j++){
			while(j < N && B[i] >= A[j]) j++;
			if (j == N) break;
		}
		int dw = i;

		printf("%d %d\n", dw, w);
	}
	return 0;
}
