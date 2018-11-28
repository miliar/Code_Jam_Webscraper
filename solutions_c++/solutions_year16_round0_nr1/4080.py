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

long long myCount(long long N) {
    int bucket[10] = { 0 };
    
    long long n = N;
    while (n) {
        long long x = n;
        while (x) {
            bucket[x%10]++;
            x /= 10;
        }
        int j;
        for (j = 0; j < 10; ++j)
            if (bucket[j] == 0)
                break;
        if (j == 10)
            return n;
        n += N;
        
    }
    return 0;
}

int main(int argc, const char * argv[]) {
    ofstream outfile("/Users/Wenfeng/Desktop/a-small-out.txt");
    if (!outfile.is_open()) {
        cout << "file not open" << endl;
        return -1;
    }
    
    int T, N;
    
    cin >> T;
    
    for (int i = 1; i <= T; ++i) {
        cin >> N;
        long long res = myCount(N);
        if (N)
            outfile << "Case #" << i << ": " << res << endl;
        else
            outfile << "Case #" << i << ": INSOMNIA" << endl;
    }
    outfile.close();
    return 0;
}
