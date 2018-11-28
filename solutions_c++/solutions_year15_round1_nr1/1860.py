#include <stdio.h>

int main(){
    int t, ans1, ans2, rate;
    int n, m[50000];
    scanf ("%d", &t);

    for (int k=1; k<=t; k++){
        scanf ("%d", &n);

        for (int i=1; i<=n; i++)
            scanf ("%d", &m[i]);

        ans1 = 0;
        for (int i=2; i<=n; i++){
            if (m[i] < m[i-1])
                ans1 += m[i-1]-m[i];
        }

        rate = 0;
        for (int i=2; i<=n; i++){
            if (m[i-1]-m[i] > rate)
                rate = m[i-1]-m[i];
        }

        ans2 = 0;
        for (int i=2; i<=n; i++){
            if (m[i-1] < rate)
                ans2 += m[i-1];
            else ans2 += rate;
        }

        printf ("CASE #%d: %d %d\n", k, ans1, ans2);
    }

    return 0;
}
