//
//  main.cpp
//  GoogleCodeJam
//
//  Created by Luan Nguyen on 4/9/16.
//  Copyright © 2016 Luan Nguyen. All rights reserved.
//

#include <iostream>
#include <vector>
#include <string>
#include <fstream>

using namespace std;


void print(const vector<int>& r)
{
//    for (auto c : r)
//        cout << c << " ";
//    cout << endl;
}

int getMask(long long N)
{
    int mask = 0;
    while (N > 0)
    {
        int c = N % 10;
        mask |= (1<<c);
        N /= 10;
    }
    
    return mask;
}

string find(int x)
{
    if (x == 0)
        return "INSOMNIA";
    
    int mask = 0;
    long long N = 0;
    do
    {
        N += x;
        int t = getMask(N);
        mask |= t;
    }
    while (mask != 1023);
    
    return std::to_string(N);
}

int main(int argc, const char * argv[])
{
    ofstream outFile;
    outFile.open("/users/superkinhluan/documents/Xcode projects/GoogleCodeJam/GoogleCodeJam/a-large.out", ios::out);
    
    ifstream inFile;
    inFile.open("/users/superkinhluan/documents/Xcode projects/GoogleCodeJam/GoogleCodeJam/a-large.in", ios::in);
    
    int T;
    inFile >> T;
    
    for (int i = 1; i <= T; ++i)
    {
        int N;
        inFile >> N;
        
        auto res = find(N);
        //cout << res << endl;
        outFile << "Case #" << i << ": " << res << endl;
    }
    
    outFile.close();
    inFile.close();
    
    return 0;

}
