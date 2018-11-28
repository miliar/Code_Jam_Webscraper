#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

const int MAXN = 10005;

int N, X, cases;
int A[MAXN];

int main(){
	scanf("%d", &cases);
	for(int xx = 1; xx <= cases; ++xx){
		scanf("%d%d", &N, &X);
		for(int i = 0; i < N; ++i)
			scanf("%d", &A[i]);
		sort(A, A + N);
		int l = 0, r = N - 1;
		int ans = 0;
		while(l <= r){
			while((l != r) && (A[l] + A[r] > X)){
				++ans;
				--r;
			}
			if(l == r){
				++ans;
				break;
			}
			++ans;
			++l; --r;
		}
		printf("Case #%d: %d\n", xx, ans);
	}
}
