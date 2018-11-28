#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <fstream>
#include <sstream>
#include <cmath>
#include <stack>
#include <queue>
#include <vector>
#include <cassert>
#include <utility>

using namespace std;

long long solve(long long r, long long t){
    long long black = 0;

    long long ring = 0;

    while(true){
        //black circle
        if (ring % 2 == 1){
            t -= (r + ring) * (r + ring) - (r - 1 + ring) * (r - 1 + ring);

            if (t >= 0) black++;
            else break;
        }

        ring ++;
    }

    return black;
}

int main(){

    ifstream in("A-small-attempt0.in");
    ofstream out("A-small-attempt0.out");

    int T;
    in >> T;

    int test;
    for (test = 1; test <= T; test++){

        long long r;
        long long t;

        in >> r >> t;

        out << "Case #" << test << ": " << solve(r, t) << endl;

    }

    in.close();
    out.close();

    return 0;
}
