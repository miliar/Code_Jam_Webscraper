# include <cstdio>
# include <iostream>
# include <cmath>
# include <cstring>
using namespace std;

int main(){
    //freopen ("A-large.in", "r", stdin);
    //freopen ("Alout.txt", "w", stdout);
    int cases, caseno=0, n, m, A[1005], i, j, mxdif, s1, s2;
    scanf ("%d", &cases);
    while (cases--){
        mxdif = s1 = s2 = 0;
        scanf ("%d", &n);
        scanf ("%d", &A[0]);
        for (i=1; i<n; i++){
            scanf ("%d", &A[i]);
            mxdif = max(mxdif, (A[i-1]-A[i]));
        }
        for (i=0; i<n-1; i++){
            s1+=(A[i]>A[i+1]) ? (A[i]-A[i+1]) : 0;
            s2+=(A[i]>mxdif) ? mxdif : A[i];
        }
        printf ("Case #%d: %d %d\n", ++caseno, s1, s2);
    }
    return 0;
}
