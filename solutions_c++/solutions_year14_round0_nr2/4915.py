//
//  main.cpp
//  cj2014
//
//  Created by Boychuk, Petro on 4/11/14.
//  Copyright (c) 2014 Boychuk, Petro. All rights reserved.
//

#include <iostream>
#include <set>
#include <vector>
#include <algorithm>

using namespace std;


void solve() {
    
    double c,f,x;
    cin >> c >> f >> x;
    
    double time = 0;
    double speed = 2;
    vector<double> possible;
    for (int i=0; i<50000; i++) {
        possible.push_back(time + (x)/speed);
        double time_to_c = c / (speed);
        speed += f;
        time += time_to_c;
    }
    
    
    sort(possible.begin(), possible.end());
    
    cout.setf(ios::fixed);
    
    cout.precision(8);
    cout << possible[0];
    cerr << possible[0] << endl;
    
}


int main(int argc, const char * argv[])
{
    
    freopen("inputB.txt", "r", stdin);
    freopen("outputB.txt", "w", stdout);

    int t;
    cin >> t;
    
    for (int i=0; i<t; i++) {
        cout << "Case #" << i+1 << ": ";
        solve();
        cout << endl;
        
    }
    
    return 0;
}

