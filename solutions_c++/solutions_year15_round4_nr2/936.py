//
//  main.cpp
//  B
//
//  Created by Jared Feng on 5/30/15.
//  Copyright (c) 2015 Jared Feng. All rights reserved.
//

#include <iostream>
#include <algorithm>
#include <cassert>
#include <cmath>
#include <iomanip>
using namespace std;

const double EPS = 1e-9;

struct record
{
    double r , c;
    bool operator < (const record &rhs) const {
        return this->c < rhs.c;
    }
} s[110];

static inline int dblcmp(const double &x , const double &y)
{
    if (y - x > EPS) return -1;
    else return x - y > EPS;
}

void process(int case_id)
{
    int n;
    double v, x , ans = 0.0;
    cin >> n >> v >> x;
    for (int i = 0 ; i < n ; ++i)
    {
        cin >> s[i].r >> s[i].c;
    }
    sort(s , s + n);
    if (dblcmp(s[0].c, x) > 0 || dblcmp(s[n-1].c, x) < 0)
    {
        cout << "Case #" << case_id << ": " << "IMPOSSIBLE" << endl;
        return ;
    }
    double R = 0.0 , S = 0.0;
    for (int i = 0 ; i < n ; ++i)
    {
        R += s[i].r;
        S += s[i].r * (s[i].c - x);
    }
    int cmp = dblcmp(S , 0.0);
    if (cmp == 0)
    {
        ans = v / R;
        cout << "Case #" << case_id << ": " << ans << endl;
        return ;
    }
    else if (cmp > 0)
    {
        for (int i = n - 1 ; i >= 0 ; --i)
        {
            double S2 = s[i].r * (s[i].c - x);
            if (dblcmp(S - S2 , 0.0) > 0)
            {
                R -= s[i].r;
                S -= S2;
            }
            else
            {
                R -= S / (s[i].c - x);
                S = 0.0;
                break;
            }
        }
    }
    else if (cmp < 0)
    {
        for (int i = 0; i < n ; ++i)
        {
            double S2 = s[i].r * (s[i].c - x);
            if (dblcmp(S, S2) < 0)
            {
                R -= s[i].r;
                S -= S2;
            }
            else
            {
                R -= S / (s[i].c - x);
                S = 0.0;
                break;
            }
        }
    }
    if (dblcmp(R , 0.0) <= 0)
    {
        cout << "Case #" << case_id << ": " << "IMPOSSIBLE" << endl;
        return ;
    }
    ans = v / R;
    cout << "Case #" << case_id << ": " << ans << endl;
}
int main()
{
    cout << fixed << setprecision(10);
    int t;
    cin >> t;
    for (int i = 1 ; i <= t ; ++i)
        process(i);
    return 0;
}