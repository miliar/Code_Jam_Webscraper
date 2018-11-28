//
//  main.cpp
//  standingOvation
//
//  Created by Dan Perez on 4/11/15.
//  Copyright (c) 2015 com.perezda. All rights reserved.
//

#include <iostream>
#include <vector>
#include <fstream> 

using namespace std;

int calcNeeded(vector<int> &v)
{
    int totalNeeded = 0;
    int totalStanding = 0;
    for (int i=0; i < v.size(); ++i) {
        if (totalStanding < i && v[i] > 0) {
            totalNeeded += i-totalStanding;
            totalStanding += i-totalStanding;
        }
        totalStanding += v[i];
    }
    return totalNeeded;
}

int main(int argc, const char * argv[]) {
    int T = 0;
//    ifstream myFile = ifstream("standingOvation.txt");

    cin >> T;
//    myFile >> T;

    for (int t=0; t<T; ++t) {
        int smax = 0;

        cin >> smax;
//        myFile >> smax;

        string s;

        cin >> s;
//        myFile >> s;

        vector<int> v(smax+1, 0);
        for (int i=0; i<s.length(); ++i) {
            char c = s[i];
            int si = c - '0';
            v[i]=si;
        }
        int rc = calcNeeded(v);
        cout << "Case #" << t+1 << ": " << rc << endl;
    }


    return 0;
}
