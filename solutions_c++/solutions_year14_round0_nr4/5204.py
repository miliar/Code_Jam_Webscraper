//
//  main.cpp
//  gcj1
//
//  Created by Dan Raviv on 3/19/14.
//

#include <iostream>
#include <map>
#include <vector>
#include <algorithm>
using namespace std;
#include <stdio.h>

typedef struct case_t {
    vector<double> myBlocks, enemyBlocks;
} case_t;

typedef struct res_t {
    int deceitScore, warScore;
} res_t;

res_t solve(const case_t& c);

int main(int argc, const char * argv[])
{
    int nCases;
    cin >> nCases;
    
    vector<case_t> cases (nCases);
    for (auto& it : cases) {
        int nBlocks;
        cin >> nBlocks;
        for (int i=0; i<nBlocks; ++i) {
            double item;
            cin >> item;
            it.myBlocks.push_back(item);
        }
        for (int i=0; i<nBlocks; ++i) {
            double item;
            cin >> item;
            it.enemyBlocks.push_back(item);
        }
    }
    
    vector<res_t> results (nCases);
    for (int i=0; i<nCases; ++i) {
        results[i] = solve(cases[i]);
    }
    
    for (int i=0; i<nCases; ++i) {
        res_t& res = results[i];
        printf("Case #%d: %d %d\n", i+1, res.deceitScore, res.warScore);
    }
    
    return 0;
}

int solveWar(const case_t& c)
{
    vector<double> mySorted = c.myBlocks;
    sort(mySorted.begin(), mySorted.end());
    
    vector<double> enemySorted = c.enemyBlocks;
    sort(enemySorted.begin(), enemySorted.end());
    
    int score = 0;
    size_t nBlocks = mySorted.size();
    for (size_t i=0; i<nBlocks; ++i)
    {
        double myVal = mySorted[i];
        auto it=enemySorted.begin();
        for (;it != enemySorted.end(); ++it)
        {
            if (*it > myVal)
            {
                break;
            }
        }
        if (it == enemySorted.end())
        {
            enemySorted.erase(enemySorted.begin());
            score++;
        }
        else
        {
            enemySorted.erase(it);
        }
    }
    return score;
}

int solveDeceit(const case_t& c)
{
    vector<double> mySorted = c.myBlocks;
    sort(mySorted.begin(), mySorted.end());
    
    vector<double> enemySorted = c.enemyBlocks;
    sort(enemySorted.begin(), enemySorted.end());

    size_t nBlocks = mySorted.size();
    int score = 0;

    for (size_t i=0; i<nBlocks; ++i)
    {
        if (mySorted[0] < enemySorted[0]) {
            mySorted.erase(mySorted.begin());
            enemySorted.erase(enemySorted.begin()+(nBlocks-1-i));
        }
        else {
            mySorted.erase(mySorted.begin());
            enemySorted.erase(enemySorted.begin());
            ++score;
        }
    }
    return score;
}

res_t solve(const case_t& c)
{
    return { solveDeceit(c), solveWar(c) };
}








