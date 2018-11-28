# include <cstdio>
# include <cstring>
using namespace std;

int main(){
    //freopen("A-large.in", "r", stdin);
    //freopen ("Alout.txt", "w", stdout);
    int cases, caseno=0, A[1005], i, total, n, len;
    char st[1005];
    scanf ("%d", &cases);
    while (cases--){
        total = 0;
        scanf ("%d %s", &n, st);
        len = strlen(st);
        for (i=0; i<len; i++) A[i] = st[i]-'0';
        for (i=1; i<len; i++){
            if (A[i-1]<i){
                total += (i-A[i-1]);
                A[i-1] = i;
            }
            A[i] += A[i-1];
        }
        printf ("Case #%d: %d\n", ++caseno, total);
    }
    return 0;
}
