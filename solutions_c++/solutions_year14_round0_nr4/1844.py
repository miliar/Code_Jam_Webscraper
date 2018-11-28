#include <iostream>
#include <fstream>
#include <map>
#include <vector>
#include <set>
#include <string>
#include <algorithm>
#include <math.h>
#include <stdlib.h>
#include <stdio.h>

using namespace std;

int solve1(vector<double> &na, vector<double> &ke)
{
    int k0 = 0;
    int score = 0;
    for (int i = 0; i < na.size(); i++)
    {
        if (na[i] > ke[k0])
        {
            score++;
            k0++;
        }
    }
    return score;
}

int solve2(vector<double> &na, vector<double> &ke)
{
    int k0 = 0;
    int score = 0;
    for (int i = 0; i < na.size(); i++)
    {
        while (k0 != ke.size() && ke[k0] < na[i])
            k0++;
        if (k0 == ke.size())
            score++;
        else
            k0++;
    }
    return score;
}

void solve(int t)
{
    int n;
    double w;
    cin >> n;
    vector<double> na,ke;

    for (int i = 0; i< n; i++)
    {
        cin >> w;
        na.push_back(w);
    }
    sort(na.begin(), na.end());

    for (int i = 0; i< n; i++)
    {
        cin >> w;
        ke.push_back(w);
    }
    sort(ke.begin(), ke.end());

    cout.precision(10);
    cout << fixed;
    cout << "Case #" << t+1 << ": " << solve1(na, ke) << ' ' << solve2(na, ke) << endl;
    cerr << "case " << t+1 << endl;
}

int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

    int T;
    cin >> T;

    for (int i = 0; i < T; i++)
        solve(i);

    return 0;
}
