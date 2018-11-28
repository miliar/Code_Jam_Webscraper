#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;

int solveWar(vector<double> & naomi, vector<double> & ken)
{
    sort (naomi.rbegin(), naomi.rend());
    int n = naomi.size() - 1;
    int res = 0;
    while (n >= 0)
    {
        if (naomi[n] > ken[n])
        {
            for (int i = 0; i < n; i++)
            {
                swap (ken[i], ken[i+1]);
            }
            res++;
        }
        else
        {
            vector<double>::iterator ind = lower_bound (ken.begin(), ken.begin() + n + 1, naomi[n]);
            int from = ind - ken.begin();
            for (int i = from; i < n; i++)
            {
                swap (ken[i], ken[i+1]);
            }
        }
        n--;
    }
    return res;
}
int main(void)
{
    int t;
    cin >> t;
    for (int k = 1; k <= t; k++)
    {
        int n, scoreD = 0, scoreW = 0;
        cin >> n;
        vector<double> ken(n), naomi(n);
        for (int i = 0; i < n; i++)
        {
            cin >> naomi[i];
        }
        sort (naomi.begin(), naomi.end());
        for (int i = 0; i < n; i++)
        {
            cin >> ken[i];
        }
        sort (ken.begin(), ken.end());
        //calcs
        int l = 0, j = n-1;
        for (int i = 0; i < n; ++ i)
        {
            if (naomi[i] > ken[l])
            {
                l++;
                scoreD++;
            }
            else
            {
                j--;
            }
        }
        scoreW = solveWar(naomi,ken);
        printf("Case #%i: %i %i\n", k, scoreD, scoreW);
    }
    return 0;
}
