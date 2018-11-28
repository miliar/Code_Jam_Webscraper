#include <cstdio>
#include <algorithm>

using namespace std;

int main(){
    int T;
    scanf("%d",&T);
    for(int c = 1 ; c <= T ; c++){
        int N, mx = 0;
        int A[1010];
        scanf("%d",&N);
        for(int d = 0 ; d < N ; d++){
            scanf("%d",&A[d]);
            mx = max(A[d],mx);
        }
        int sol = -1u/2;
        for(int d = 1 ; d <= mx ; d++){
            int sum = d;
            for(int e = 0 ; e < N ; e++)
                if(A[e] > d)
                    sum += (A[e]-d)/d+(((A[e]-d)%d)>0);
            sol = min(sum,sol);
            // printf("%d-- %d\n",d,sum);
        }
        printf("Case #%d: %d\n",c,sol);
    }
}
