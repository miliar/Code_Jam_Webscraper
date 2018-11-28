//
//  main.cpp
//  bleatrix
//
//  Created by Ray Xu on 10/04/2016.
//  Copyright © 2016 Ray Xu. All rights reserved.
//

#include <iostream>


#include <iostream>
#include <fstream>
#include <string>
using namespace std;


const int maxT = 2147483647;
const int maxN = 200;

bool done(int hashDigit[]){
    for (int i = 0; i < 10; i++){
        if (hashDigit[i] == 0){
            return false;
        }
    }
    return true;
}

string Bleatrix(long N )
{
    string ret;
    if (N==0)
        return("INSOMNIA");
    int hashDigit[10] = {};
    for (int m = 0; m < 10;m++){
        hashDigit[m]= 0;
    }
    
    int maxLoop=maxT/N;
    
    for (long i = 1; i <= maxLoop; i++)
    {
        long tN = i*N;
        while (tN != 0){
            int m = tN % 10;
            hashDigit[m] = 1;
            tN /= 10;
        }
        if (done(hashDigit)){
            ret = to_string(i*N);
            break;
        }
    }
    
    if (!done(hashDigit))
    {
        ret = "INSOMNIA";
    }
    return ret;
    
}


int main(int argc, const char* argv[])
{
    std::freopen("A-large.in", "r", stdin);
    std::freopen("A-large.out", "w", stdout);
    int T;
    cin >> T;
    for (int i = 1; i <= T; i++)
    {
        long testcase;
        cin >> testcase;
        string ret = Bleatrix(testcase);
        cout << "Case #" << i << ": " << ret << endl;
    }
    
    return 0;
}


