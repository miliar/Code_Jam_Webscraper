#include <stdio.h>

using namespace std;

#define MAX_N 100000
int R, C, W;


int solve(){
    return ((W-1) + (C + W - 1) / W) * R;
}


int main()
{
    int T;
    freopen("input.txt", "r", stdin);
    freopen("answer.txt", "w", stdout);
    setbuf(stdout, NULL);
    scanf("%d", &T);
    for (int i = 1; i <= T; i++){
        scanf("%d %d %d", &R, &C, &W);
        printf("Case #%d: %d\n", i, solve());
    }
}
