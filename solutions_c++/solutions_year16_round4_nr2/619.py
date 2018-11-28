#include <iostream>
#include <vector>
#include <cstdio>
#include <algorithm>

using namespace std;

double prob(vector<double> P)
{
    int N = (int)P.size();
    vector<double> T(N+1);
    T[0] = 1.;

    for (int i=0; i<N; i++)
    {
        vector<double> S = T;
        T = vector<double>(N+1);

        for (int j=0; j<=i; j++)
            T[j+1] += S[j] * P[i],
            T[j] += S[j] * (1.-P[i]);
    }

    return T[N/2];
}

double solve()
{
    int N, K;
    cin>>N>>K;
    vector<double> P(N);
    for (double &p: P)
        cin>>p;
    sort(P.begin(), P.end());

    double ans = 0.;

    for (int i=0; i<=K; i++)
    {
        vector<double> tmp;

        for (int j=0; j<i; j++)
            tmp.push_back(P[j]);
        for (int j=i+N-K; j<N; j++)
            tmp.push_back(P[j]);

        //cout<<i<<" "<<prob(tmp)<<endl;
        ans = max(ans, prob(tmp));
    }

    return ans;
}

int main()
{
    int T;
    cin>>T;
    for (int t=1; t<=T; t++)
        printf("Case #%d: %.10f\n", t, solve());
}
