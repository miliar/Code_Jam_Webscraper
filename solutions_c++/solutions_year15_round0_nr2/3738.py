#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <queue>

using namespace std;

#define MAXN 1009
int D,A[MAXN];

void Read() {
    scanf("%d",&D);

    for (int i=1;i<=D;i++) {
        scanf("%d",&A[i]);
    }
}

int stepsToK(int N,int K) {
    if ( N % K == 0 ) {
        return N / K -1;
    }
    else {
        return N / K;
    }
}

void Solve(int testcase) {
    int ans = 100000009;
    int maxP = -1;

    for (int i=1;i<=D;i++) {
        maxP = max(maxP,A[i]);
    }

    for (int i=1;i<=maxP;i++) {
        int stepsNeeded = 0;
        for (int j=1;j<=D;j++) {
            if (i < A[j]) {
                stepsNeeded += stepsToK(A[j],i);
            }
        }
        ans = min (ans,stepsNeeded+i);
    }

    printf("Case #%d: %d\n",testcase,ans);
}

int main () {
    freopen("in.in","r",stdin);
    freopen("out.out","w",stdout);

    int t;
    scanf("%d",&t);

    for (int i=1;i<=t;i++) {
        Read();
        Solve(i);
    }

    return 0;
}
