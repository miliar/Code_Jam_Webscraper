#include <bits/stdc++.h>

using namespace std;

double tieProb(const vector<double>& p)
{
    int n = p.size();
    
    double pVote[n + 1][n + 1];
    memset(pVote, 0, sizeof(pVote));
    
    pVote[0][0] = 1;
    
    for (int voted = 0; voted < n; voted++)
        for (int agree = 0; agree < n; agree++)
        {
            pVote[voted + 1][agree + 1] += pVote[voted][agree] * p[voted];
            pVote[voted + 1][agree] += pVote[voted][agree] * (1 - p[voted]);
        }
        
    return pVote[n][n / 2];
}

void solve(int caseN)
{
    int n, k;
    cin >> n >> k;
    
    vector<double> p(n);
    for (int i = 0; i < n; i++)
        cin >> p[i];
    
    double ans = 0;
    for (int mask = 0; mask < (1 << n); mask++)
    {
        if (__builtin_popcount(mask) != k) continue;
        
        vector<double> choose;
        for (int i = 0; i < n; i++)
            if (mask & (1 << i))
                choose.push_back(p[i]);
            
        double can = tieProb(choose);
        ans = max(can, ans);
    }
    
    printf("Case #%d: %.12f\n", caseN, ans);
}

int main()
{
    int nt;
    scanf("%d", &nt);
    
    for (int i = 0; i < nt; i++)
        solve(i + 1);
    
    return 0;
}
