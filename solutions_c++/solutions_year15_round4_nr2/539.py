#include <bits/stdc++.h>

using namespace std;

const double EPS=1e-9;
int N;
double V, X;
double C[100];
double R[100];
double A[100];

void _main()
{
    scanf("%d%lf%lf", &N, &V, &X);
    for(int i=0; i<N; i++)
        scanf("%lf%lf", R+i, C+i), C[i]-=X;
    double ans=1e300;
    double rt=0.0;
    for(int i=0; i<N; i++)
        if(fabs(C[i])<=EPS)
            rt+=R[i];
    if(fabs(rt)>EPS)
        ans=min(ans, V/rt);
    if(N>1)
    {
        double t0 = -(V * C[1]) / (R[0] * C[0] - R[0] * C[1]);
        double t1 = V / R[1] - t0 * R[0] / R[1];
        if(t0>-EPS && t1>-EPS)
            ans=min(ans, max(t0, t1));
    }
    if(ans>1e200)
        printf("IMPOSSIBLE\n");
    else
    {
        printf("%.9f\n", ans);
    }
}

int main()
{
    //freopen("in.txt", "r", stdin);
    freopen("B-small-attempt1.in", "r", stdin);
    freopen("B-small-attempt1.out", "w", stdout);
    int TEST;
    scanf("%d", &TEST);
    for(int i=1; i<=TEST; i++)
    {
        printf("Case #%d: ", i);
        _main();
    }
    return 0;
}
