//
//  main.cpp
//  codejam1
//
//  Created by Youngsun Suh on 2015-04-10.
//  Copyright (c) 2015 Youngsun Suh. All rights reserved.
//


#include <iostream>
#include <string>
#include <vector>

using namespace std;

int getFriends(vector<int> &nAuds) {
    int nFriends = 0;
    int sum = 0;
    
    for (int i=0; i<nAuds.size(); i++) {
        int diff = sum - i;
        if (diff < 0) {
            nFriends -= diff;
            sum -= diff;
        }
        sum += nAuds[i];
    }
    return nFriends;
}

int main(int argc, const char * argv[]) {
    int nCase;
    cin >> nCase;
    cin.ignore();
    for (int i=0; i<nCase; i++) {
        vector<int> nAuds;
        int maxLevel;
        cin >> maxLevel;
        
        for (int j=0; j<=maxLevel; j++) {
            char nAud;
            cin >> nAud;
            nAuds.push_back(nAud - '0');
        }
        cout << "Case #" << i+1 << ": "
            << getFriends(nAuds) << endl;
    }
    return 0;
}

