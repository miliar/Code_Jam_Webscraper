//
//  main2.cpp
//  contest
//
//  Created by xianran on 5/4/14.
//  Copyright (c) 2014 xianran. All rights reserved.
//

#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    int ntest;
    ofstream fout;
    fout.open("/Users/xianran/Desktop/result.txt", ios::out);
    
    cin >> ntest;
    for (int nt = 1; nt <= ntest; nt++) {
        int A, B, K;
        int count = 0;
        
        cin >> A >> B >> K;
        
        for (int a = 0; a < A; a++) {
            for (int b = 0; b < B; b++) {
                int c = a & b;
                if (c < K)
                    count++;
            }
        }
        
        fout << "Case #" << nt << ": " << count << endl;
    }
    
    fout.close();
}
