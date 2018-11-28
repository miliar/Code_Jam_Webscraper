#include <iostream>
#include <iomanip>
#include <fstream>
#include <algorithm>
#include <vector>
#include <string>
#include <cmath>

using namespace std;
typedef long long ll;
const int MAXN = 210;

ifstream fin ("B.in");
ofstream fout ("B.out");

int N, K;
double prob[MAXN];
double cool[MAXN];

double dp[MAXN];

double solve()
{
    for (int i = 0; i < MAXN; i++)
        dp[i] = 0;
    dp[0] = 1;
    
    for (int i = 0; i < K; i++)
        for (int j = i; j >= 0; j--)
        {
            double p = dp[j] * cool[i];
            dp[j+1] += p;
            dp[j] -= p;
        }
    return dp[K/2];
}

int main()
{
    fout << fixed << setprecision (7);
    int ntest = 0; fin >> ntest;
    for (int test = 1; test <= ntest; test++)
    {
    fin >> N >> K;
    for (int i = 0; i < N; i++)
        fin >> prob[i];
    sort (prob, prob + N);
    
    for (int i = 0; i < K; i++)
        cool[i] = prob[i];
    
    double ans = solve();
    for (int i = 0; i < K; i++)
    {
        cool[K-1-i] = prob[N-1-i];
        ans = max (ans, solve());
    }
    
    fout << "Case #" << test << ": ";
    fout << ans << "\n";
    }
    return 0;
}

