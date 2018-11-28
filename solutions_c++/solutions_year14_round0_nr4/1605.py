#include<cstdio>
#include<iostream>
#include<algorithm>

using namespace std;
double A[1005];
double B[1005];
int main(){
//	freopen("d.in", "r", stdin);
//	freopen("d.out", "w", stdout);
	int T;
	scanf("%d", &T);
	int N;
	for(int i = 1; i <= T;i++){
		scanf("%d", &N);
		for(int j = 0; j < N;j++){
			scanf("%lf", &A[j]);
		}
		for(int j = 0; j < N;j++){
			scanf("%lf", &B[j]);
		}
		sort(A, A+N);
		sort(B, B+N);
		int cnt2 = 0;
		int idx = 0;
		for(int j = 0; j < N; j++){
			for(int k = idx; k < N; k++){
				if(B[k] > A[j]){
					cnt2++;
					idx = k+1;
					break;
				}
			}
		}
		int cnt1 = 0;
		idx = 0;
		for(int j = 0; j < N; j++){
			for(int k = idx; k < N; k++){
				if(A[k] > B[j]){
					cnt1++;
					idx = k+1;
					break;
				}
			}
		}
		printf("Case #%d: %d %d\n", i, cnt1, N-cnt2);
	}
	return 0;
}
