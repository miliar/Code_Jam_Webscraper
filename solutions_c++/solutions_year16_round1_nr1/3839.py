#include <stdio.h>
#include <vector>
#include <queue>
#include <string>
#include <string.h>
#include <time.h>
#include <algorithm>
using namespace std;

int T;
char S[1002];
int len;
int arr[1002];
char A[2010];

void solve(int t)
{
    int idx = 0;
    for (char  s = 'A'; s <= 'Z'; ++s)
        for (int i = 0; i < len; ++i)
            if (S[i] == s)
                arr[i] = idx++;
    idx = 1000;
    int front = idx, rear = idx;
    A[idx] = S[0];
    int maxValue = arr[0];
    for (int i = 1; i < len; ++i)
    {
        if (maxValue > arr[i]) // 뒤에다가 추가
            A[++rear] = S[i];
        else // 앞에다가 추가
        {
            A[--front] = S[i];
            maxValue = arr[i];
        }
    }
    printf("Case #%d: ", t);
    for (int i = front; i <= rear; ++i) printf("%c", A[i]);
    printf("\n");
}

int main()
{
    setbuf(stdout, NULL);
    //freopen("A-small-attempt0.in", "rt", stdin);
    scanf("%d", &T);
    for (int t = 1; t <= T; ++t)
    {
        scanf("%s", &S[0]);
        len = strlen(S);
        solve(t);
    }
    return 0;
}