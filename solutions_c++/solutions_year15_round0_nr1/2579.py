#include <stdio.h>

using namespace std;

#define MAX_N 1000
int L;
char number[MAX_N+1];
int shy[MAX_N+1];

int solve(){
    int count = 0;
    int total = number[0] - '0';
    for (int i = 1; i <= L; i++){
        int need = (i - total) > 0 ? (i - total) : 0;
        count += need;
        total += number[i] - '0' + need;
    }
    return count;
}

int main()
{
    int T;
    freopen("input.txt", "r", stdin);
    freopen("answer.txt", "w", stdout);
    setbuf(stdout, NULL);
    scanf("%d", &T);
    for (int i = 1; i <= T; i++){
        scanf("%d", &L);
        scanf("%s", number);
        printf("Case #%d: %d\n", i, solve());
    }
}
