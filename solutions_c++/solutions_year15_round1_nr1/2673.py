#include <iostream>
#include <stdio.h>
#include <stdlib.h>

void solveA(int N, int *m)
{
    int last=m[0];
    long int sum=0;
    for(int i=1;i<N;i++){
        if(m[i]<last)
            sum+=(last-m[i]);
        last=m[i];
    }
    printf("%d ", sum);
}

int findMaxDiff(int N, int *m){
    int maxdiff=0;
    for(int i=1;i<N;i++){
        int diff=m[i-1]-m[i];
        if(diff>0&&maxdiff<diff)
            maxdiff=diff;
    }
    return maxdiff;
}

void solveB(int N, int *m)
{
    int maxdiff=findMaxDiff(N,m);
    long int eat=0;
    for(int i=0;i<N-1;i++){
        eat+=(m[i]<maxdiff?m[i]:maxdiff);
    }
    printf("%ld\n", eat);
}

void solve(int N, int *m)
{
    solveA(N, m);
    solveB(N, m);
}

int main(int argc, const char * argv[]) {
    int T;
    scanf("%d", &T);
    for(int i=0;i<T;i++){
        int N, m[10001];
        scanf("%d", &N);
        for(int j=0;j<N;j++){
            scanf("%d", &m[j]);
        }
        printf("Case #%d: ", i+1);
        solve(N, m);
    }
    return 0;
}
