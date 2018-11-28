#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<math.h>
#include<algorithm>
#include<set>
#include<map>
#include<utility>
#include<vector>
#include<string>
#include<stack>
#include<queue>
using namespace std;
#define MAXN 10006
int array[MAXN];
int main()
{
    //freopen("data.txt", "r", stdin);
    freopen("Ain2.txt", "r", stdin);
    freopen("Aout.txt", "w", stdout);
    int t,T;
    int N,X,i,ans,j;
    scanf("%d", &T);
    for (t=1; t<=T; ++t)
    {
        scanf("%d %d", &N, &X);
        for (i=1; i<=N; ++i) scanf("%d", &array[i]);
        sort (array+1, array+1+N);
        reverse (array+1, array+1+N);
        ans = 0;
        for (i=1; i<=N; ++i)
        {
            if (array[i] == -1) continue;
            ++ans;
            for (j=i+1; j<=N; ++j)
            {
                if (array[j] == -1) continue;
                if (array[i] + array[j] <= X)
                {
                    array[j] = -1;
                    break;
                }
            }
        }
        printf("Case #%d: %d\n", t, ans);
    }
    return 0;
}
