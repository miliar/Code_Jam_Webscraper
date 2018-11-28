#include<iostream>
#include<vector>
#include<sstream>
#include<set>
#include<map>
#include<algorithm>

using namespace std;

long double prob(vector<long double> & P)
{
    int k = P.size();
    vector <long double> prob(k + 1, 0);
    prob[0] = 1;
    for (int i = 0; i < k; ++i)
    {
        vector <long double> prob_new(k + 1);
        for (int j = 0; j < prob.size(); ++j)
        {
            prob_new[j] = 0;
            if (j - 1 >= 0) prob_new[j] += prob[j - 1] * P[i];
            if (j < prob.size()) prob_new[j] += prob[j] * (1 - P[i]);
        }
        prob = prob_new;
    }
    return prob[k / 2];
}

long double check(vector<long double> & p, vector<int> & subset)
{
    vector <long double> new_p;
    for (int i = 0; i < p.size(); ++i)
        if (subset[i])
            new_p.push_back(p[i]);
    return prob(new_p);
}

long double  solve()
{
    long double ans = 0;
    int n, k;
    cin >> n >> k;
    vector <long double> p(n);
    for (int i = 0; i < n; ++i)
        cin >> p[i];
    vector <int> subset;
    subset.resize(n - k, 0);
    subset.resize(n, 1);
    ans = check(p, subset);
    while (next_permutation(subset.begin(), subset.end()))
        ans = max(ans, check(p, subset));
    return ans;
}

int main()
{
    int T, t;
    cin >> T;
    cout.precision(20);
    for (t = 1; t <= T; ++t)
    {
        cout << "Case #" << t << ": " << solve() << endl;
    }
    return 0;
}

