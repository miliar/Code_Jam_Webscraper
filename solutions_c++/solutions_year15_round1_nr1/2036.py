//
//  A.cpp
//  Cpp
//
//  Created by Johnson Hu on 11/4/15.
//  Copyright (c) 2015 Johnson Hu. All rights reserved.
//

#include <iostream>
#include <fstream>
using namespace std;

int main( )
{
    ifstream in_stream;
    ofstream out_stream;
    in_stream.open("A-large.in");    out_stream.open("A-large.out");

    int T; //cases
    int N;
    int m[1000];
    in_stream >> T;
    for (int i = 0; i < T; i++) {
        in_stream >> N;
        for (int j = 0; j < N; j++) {
            in_stream >> m[j];
        }
        int y = 0;
        for (int j = 0; j < N - 1; j++) {
            if (m[j] > m[j+1]) y = y + m[j] - m[j+1];
        }
        int x = 0;
        for (int j = 0; j < N - 1; j++) {
            if (m[j] - m[j+1] > x) x = m[j] - m[j+1];
        }
        int z = 0;
        for (int j = 0; j < N - 1; j++) {
            if (m[j] - x < 0) {
                z = z + m[j];
            } else z = z + x;
        }
        out_stream << "Case #" << i+1 << ": " << y << " " << z;
        if (i < T - 1) out_stream << endl;
    }


    in_stream.close();
    out_stream.close();
    return 0;
}
