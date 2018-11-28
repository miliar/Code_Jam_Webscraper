//
//  main.cpp
//  cj2014
//
//  Created by Boychuk, Petro on 4/11/14.
//  Copyright (c) 2014 Boychuk, Petro. All rights reserved.
//

#include <iostream>
#include <set>

using namespace std;
void solve() {
    
    int a,b;
    cin >> a;
    
    set<int> s1,s2;
    
    for (int i=0; i<4; i++) {
        for (int j=0; j<4; j++) {
            int t;
            cin >> t;
            if(a == i+1) {
                s1.insert(t);
            }
        }
    }
    
    cin >> b;
    
    for (int i=0; i<4; i++) {
        for (int j=0; j<4; j++) {
            int t;
            cin >> t;
            if(b == i+1) {
                s2.insert(t);
            }
        }
    }
    
    set<int> intersect;
    set_intersection(s1.begin(),s1.end(),s2.begin(),s2.end(),
                     std::inserter(intersect,intersect.begin()));
    
    if(intersect.size() == 1) {
        cout << *intersect.begin();
    } else if(intersect.size() == 0) {
        cout  << "Volunteer cheated!";
    } else {
        cout << "Bad magician!";
    }
    
}


int main(int argc, const char * argv[])
{
    
    freopen("inputA.txt", "r", stdin);
    freopen("outputA.txt", "w", stdout);
    
    int t;
    cin >> t;
    
    for (int i=0; i<t; i++) {
        cout << "Case #" << i+1 << ": ";
        solve();
        cout << endl;
        
    }

    return 0;
}

