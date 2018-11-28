//
//  main.cpp
//  QualificationRound2016
//
//  Created by Wenfeng G on 4/9/16.
//  Copyright © 2016 Wenfeng G. All rights reserved.
//

#include <iostream>
#include <fstream>
using namespace std;

int times(string s) {
    int size = (int)s.size();
    int buckets[size];
    int res(0);
    
    for (int i = 0; i < size; ++i) {
        if (s[i] == '+')
            buckets[i] = 1;
        else
            buckets[i] = 0;
    }
    
    for (int i = size-1; i >= 0; --i) {
        if (buckets[i])
            continue;
        else {
            ++res;
            for (int j = 0; j <= i; ++j)
                buckets[j] = !buckets[j];
        }
    }
    return res;
}

int main(int argc, const char * argv[]) {
    ofstream outfile("/Users/Wenfeng/Desktop/a-small-out.txt");
    if (!outfile.is_open()) {
        cout << "file not open" << endl;
        return -1;
    }
    
    int T;
    string S;
    
    cin >> T;
    for (int i = 1; i <= T; ++i) {
        cin >> S;
        outfile << "Case #" << i << ": " << times(S) << endl;
    }
    outfile.close();
    return 0;
}
