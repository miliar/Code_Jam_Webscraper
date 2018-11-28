#include <cstdio>
#include <algorithm>
using namespace std;
int a[105], b[105], c[105][105];
int i, j;

int main(){
    //freopen ("input.txt", "r", stdin);
    //freopen ("output.txt", "w", stdout);
    int t, T;
    scanf ("%d", &T);
    for (t=1; t<=T; t++){
        memset (a, 0, sizeof(a));
        memset (b, 0, sizeof(b));
        bool flag = false;
        int N, M;
        scanf ("%d%d", &N, &M);
        for (i=0; i<N; i++)
        for (j=0; j<M; j++){
            scanf ("%d", &c[i][j]);
            a[i] = max(a[i], c[i][j]);
            b[j] = max(b[j], c[i][j]);
        }
        for (i=0; i<N; i++)
        for (j=0; j<M; j++)
            if (c[i][j] < a[i] && c[i][j] < b[j])
                flag = true;
        if(flag == true)
            printf ("Case #%d: NO\n", t);
        else
            printf ("Case #%d: YES\n", t);
    }
    return 0;
}
