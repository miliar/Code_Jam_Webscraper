//
//  main.cpp
//
//  Created by 林思娜 on 4/4/15.
//  Copyright (c) 2015 林思娜. All rights reserved.
//

#include <iostream>
#include <vector>
#include <cstring>

using namespace std;

int friendnum (int Smax, string people) {
    int result = 0;
    vector<int> sum(Smax + 1);
    sum[0] = people[0] - '0';
    for (int i = 1; i <= Smax; i++) {
        sum[i] = sum[i-1] + (people[i] - '0');
    }
    for (int i = 1; i <= Smax; i++) {
        result = max(result, i - sum[i-1]);
    }
    return result;
}

int main(int argc, const char * argv[]) {

    freopen("/Users/linsina/Downloads/A-large.in", "r", stdin);
    freopen("/Users/linsina/Downloads/A-large.out", "w", stdout);
    int n;
    cin >> n;
    vector<int> Smax(n);
    vector<string> people(n);
    //vector<vector<int>> num(n, )
    for (int i = 0; i < n; i++)
    {
        cin >> Smax[i] >> people[i];
    }
    for (int i = 0; i < n; i++) {
        cout << "Case #" << i+1 << ": " <<friendnum(Smax[i], people[i]) << endl;
    }
    
}
