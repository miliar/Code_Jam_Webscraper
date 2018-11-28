//
//  main.cpp
//  Codeforces
//
//  Created by Taygrim on 20.03.13.
//  Copyright (c) 2013 Taygrim. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>
#include <string>
#include <set>
#include <map>
#include <algorithm>
#include <queue>
#include <stack>

using namespace std;

int main()
{
    ifstream cin("A-large.in.txt");
    ofstream cout("A-large.out.txt");
    int T;
    cin >> T;
    for(int w = 0; w < T; w++) {
        int n, x;
        cin >> n >> x;
        vector<int> mass(n);
        for(int i = 0; i < n; i++)
            cin >> mass[i];
        
        sort(mass.begin(), mass.end());
        int l = 0;
        int kol = 0;
        for(int i = ((int)mass.size()) - 1; i >= l; i--) {
            kol++;
            if(mass[i] + mass[l] <= x)
                l++;
        }
        cout << "Case #" << w + 1 << ": " << kol << "\n";
    }
}