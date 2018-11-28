#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <math.h>
#include <iostream>
#include <fstream>
#include <stdio.h>
#include <stdlib.h>
#include <cassert>
#include <string.h>
#include <iomanip>
using namespace std;
#define ll long long

double solve(ll mask, vector<double> &prob, ll k) {
    
    vector<double> kVec;
    for (ll i = 0; i < prob.size(); i++) {
        if (mask & (1 << i)) {
            kVec.push_back(prob[i]);
        }
    }
    
    if (kVec.size() != k)
        return -1;
    
    
    ll mask2 = 0;
    double bestProb = 0;
    
    ll totalCount = 0;
    
    while (mask2 < pow(2, k)) {
        
        ll counter = 0;
        for (ll i = 0; i < k; i++) {
            if (mask2 & (1 << i))
                counter++;
        }
        
        if (counter != k/2) {
            mask2++;
            continue;
        }
        
        totalCount++;
        
        double curProb1 = 1;
        double curProb2 = 1;
        
        for (ll i = 0; i < k; i++) {
            if (mask2 & (1 << i)) {
                curProb1 *= kVec[i];
                curProb2 *= (1-kVec[i]);
            }
            else {
                curProb1 *= (1-kVec[i]);
                curProb2 *= kVec[i];
            }
        }
        
        double curProb = curProb1 + curProb2;
        
        bestProb += curProb1;
        mask2++;
    }
    
    return bestProb;
}

int main() {
    std::ios::sync_with_stdio(false);
    cin.tie(0);

    ll t;
    cin >> t;
    
    for (ll z = 0; z < t; z++) {
        ll n, k;
        cin >> n >> k;
        vector<double> prob(n);
        for (ll i = 0; i < n; i++)
            cin >> prob[i];
        
        
        ll mask = 0;
        double ans = 0;
        while (mask < pow(2,n)) {
            
            double a = solve(mask, prob, k);
            if (a != -1)
                ans = max(ans, a);
            mask++;
        }
        
        cout << "Case #" << z+1 << ": " << ans << endl;
        
    }
}