#include <bits/stdc++.h>
#define N 210
using namespace std;

bool yes[N][N];
double inp[N], inp2[N], dp[N][N];
int n, k;

double answer(int pos , int foo) {

    if(foo < 0) return 0;

    if(pos < 1) {
        if(foo) return 0;
        return 1;
    }

    if(yes[pos][foo]) return dp[pos][foo];

    yes[pos][foo] = 1;
    dp[pos][foo] = (answer(pos-1, foo) * (1 - inp2[pos]) + answer(pos-1, foo-1) * inp2[pos]);

    return dp[pos][foo];
}

main() {

    int t;
    cin>>t;
    for(int te=1 ; te<=t ; te++) {
        cin>>n>>k;
        for(int i=1; i<=n; i++) cin>>inp[i];
        sort(inp+1 , inp+n+1);
        double finalans = 0;

        for(int i=1; i<=n; i++) {
            int cnt = 1;
            for(int j=i; j<=n; j++) inp2[cnt++] = inp[j];
            for(int j=1; j<i; j++)  inp2[cnt++] = inp[j];

            for (int i2=0; i2<N; i2++) {
                for (int j=0; j<N; j++) yes[i2][j] = 0;
            }
            double tmp = answer(k, k/2);

            finalans = max(tmp, finalans);
        }

        cout<<"Case #"<<te<<": ";
        printf("%.9lf\n" , finalans);
    }
}
