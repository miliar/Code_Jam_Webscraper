#include<cstdio>
#include<iostream>
#include<vector>
#include<algorithm>
#include<string>
#include<cstring>
using namespace std;

typedef long long LL;

int N, A[1011];

int main() {
    int T;
    scanf("%d", &T);

    for (int tc=1; tc<=T; tc++) {
	scanf("%d", &N);
	for (int i=0; i<N; i++) scanf("%d", A+i);
	
	int cnt = 0;
	int l=0, r=N;
	for (int k=0; k<N; k++) {
	    int p=l;
	    for (int i=l; i<r; i++) if (A[p] > A[i]) p = i;
	    if (p-l < r-p-1) {
		cnt += p-l;
		for (int i=p-1; i>=l; i--) swap(A[i], A[i+1]);
		l++;
	    } else {
		cnt += r-p-1;
		for (int i=p; i<r-1; i++) swap(A[i], A[i+1]);
		r--;
	    }
	}
	printf("Case #%d: %d\n", tc, cnt);
	
    }
    return 0;
}
