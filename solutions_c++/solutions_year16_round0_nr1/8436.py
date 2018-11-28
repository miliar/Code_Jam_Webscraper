//
//  main.cpp
//  googleCodeJam
//
//  Created by Haneen Mohammed on 4/9/16.
//  Copyright © 2016 Haneen Mohammed. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <stdio.h>      /* printf, fgets */
#include <set>
#include <sstream>      // std::ostringstream

using namespace std;

int main(int argc, const char * argv[]) {
    string line;
    int T = 0;     // Number of test cases
    int long long n = 0, N= 0; // N: starting number, n: increments
    int long long lastN = 0;
    int long i = 1;
    int long x = 0; // case number
    set<char> myset;
    set<char>::iterator it;

    ofstream result;    // output file
    result.open ("/Users/haneen/codes/googleCodeJam/googleCodeJam/result.txt");

    
    ifstream myfile ("/Users/haneen/codes/googleCodeJam/googleCodeJam/sample.txt"); // input file
    if (!myfile.is_open()) {
        cout << "Failed to open file" << endl;
        exit (0);
    }
    getline (myfile,line);
    T = atoi(line.c_str());
    cout << "Number of Test Cases = " << T << endl;
    while ( getline (myfile,line) ) {
       // cout << line << endl;
        N = atoll(line.c_str());
        n = N;
        x++;
        // Process this case
        if ( N == 0 ) {
            cout << "INSOMNIA" << endl; // write this
            result << "Case #" << x << ": INSOMNIA" << endl;
        }
        else {
            // Get each digit in line
            // add it to set
            // reset counters
            myset.clear();
            i = 1;
            while( myset.size() != 10 ) {
                std::ostringstream os;
                os << n;
                std::string digits = os.str();
                
                
                for (int k = 0; k < digits.length(); k++) {
                    myset.insert(digits[k]);
                }
                /*std::cout << " myset contains :";
                for (it=myset.begin(); it!=myset.end(); ++it)
                std::cout << ' ' << *it;
            
                std::cout << '\n';
                 */
                lastN = n;
                n = (++i * N);
            }
            cout << "N = " << N << " Last N = " << lastN << endl;
            result << "Case #" << x << ": " << lastN << endl;

        }
    }
    
    result.close();
    myfile.close();
    return 0;
}
