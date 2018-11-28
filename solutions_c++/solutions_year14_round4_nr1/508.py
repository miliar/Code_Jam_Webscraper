#include<cstdio>
#include<iostream>
#include<vector>
#include<algorithm>
#include<string>
#include<cstring>
using namespace std;

typedef long long LL;

int N, X, S[10011];

int main() {
    int T;
    scanf("%d", &T);

    for (int tc=1; tc<=T; tc++) {
	scanf("%d%d", &N, &X);
	for (int i=0; i<N; i++) scanf("%d", S+i);
	sort(S, S+N);

	int cnt = 0;
	int l=0, r=N-1;
	for (; l<=r; ) {
	    if (l==r) {
		cnt++;
		break;
	    } else if (S[l]+S[r] <= X) {
		l++; r--; cnt++;
	    } else {
		r--; cnt++;
	    }
	}
	printf("Case #%d: %d\n", tc, cnt);
	
    }
    return 0;
}
