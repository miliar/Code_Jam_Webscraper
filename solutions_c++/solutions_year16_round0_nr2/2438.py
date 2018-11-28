//
//  pancakes.cpp
//  codejam
//
//  Created by Adam Bielski on 09.04.2016.
//  Copyright © 2016 Adam Bielski. All rights reserved.
//

#include <iostream>
#include <string>

using std::cin;
using std::cout;

int solve(const char* str) {
    int k=0;
    for (int i=1; i<strlen(str); ++i) {
        if (str[i]!=str[i-1])
            k++;
    }
    if ((str[0] == '+' && k%2 == 1) || (str[0] == '-' && k%2 == 0))
        k++;
    return k;
}

int main(int argc, char** argv) {
 
    int N;
    cin >> N;
    for (int i=0; i<N; ++i) {
        std::string in;
        cin >> in;
        int result = solve(in.c_str());
        cout << "Case #" << i+1 << ": " << result << std::endl;
    }
    return 0;
}
