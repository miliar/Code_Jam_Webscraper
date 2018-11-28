#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

using namespace std;

void solve(int R, int C, int W)
{
    int count=R*C/W;
    if(C%W==0||W==1)
        count+=(W-1);
    else
        count+=W;
    printf("%d\n", count);
}

int main(int argc, const char * argv[]) {
    int T;
    scanf("%d", &T);
    for(int i=0;i<T;i++){
        int R, C, W;
        scanf("%d %d %d", &R, &C, &W);
        printf("Case #%d: ", i+1);
        solve(R, C, W);
    }
    return 0;
}