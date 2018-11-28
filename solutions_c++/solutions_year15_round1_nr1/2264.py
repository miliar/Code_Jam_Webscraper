//
//  main.cpp
//  A. Mushroom Monster
//
//  Created by Dmytro Kotsur on 4/18/15.
//  Copyright (c) 2015 Dmytro Kotsur. All rights reserved.
//

#include <iostream>
#include <vector>
#include <fstream>

using namespace std;

int T, N;
vector<int> m;

ifstream in("/Users/dkotsur/Projects/Contests/Google Code Jam 2015/Round 1A 2015/in.txt");
ofstream out("/Users/dkotsur/Projects/Contests/Google Code Jam 2015/Round 1A 2015/out.txt");

int main(int argc, const char * argv[])
{
    
    in >> T;
    
    for (int t = 1; t <= T; ++t) {
        in >> N;
        m.assign(N, 0);
        for (int i = 0; i < N; ++i) {
            in >> m[i];
        }
        
        int min1 = 0, min2 = 0, max_rate = 0;
        for (int i = 0; i < N - 1; ++i) {
            if (m[i+1] < m[i]) {
                min1 += m[i] - m[i+1];
                max_rate = max(max_rate, m[i] - m[i+1]);
            }
        }

        for (int i = 0; i < N - 1; ++i) {
            min2 += min(m[i], max_rate);
        }
        
        out << "Case #" << t << ": " << min1 << " " << min2 << endl;
    }

    
    
    return 0;
}

