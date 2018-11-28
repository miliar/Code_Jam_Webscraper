//
//  main.cpp
//  CodeJam1
//
//  Created by Krunoslav Zaher on 4/8/17.
//  Copyright © 2017 Bellabeat. All rights reserved.
//

#include <stdio.h>
#include <vector>
using namespace std;

int solve(vector<bool> data, int k) {
    int steps = 0;

    for (int i = 0; i <= data.size() - k; ++i) {
        if (!data[i]) {
            steps += 1;
            for (int j = i; j < i + k; ++j) {
                data[j] = !data[j];
            }
        }
    }

    for (int i = 0; i < data.size(); ++i) {
        if (!data[i]) {
            return -1;
        }
    }

    return steps;
}

int main(int argc, const char * argv[]) {
    auto filename = "/Users/kzaher/Projects/codejam/CodeJam1/CodeJam1/Test1.txt";

    FILE *file = fopen(filename, "rb");

    int count;
    fscanf(file, "%d\n", &count);

    for (int i = 0; i < count; ++i) {
        vector<bool> data;

        char c;
        do {
            fscanf(file, "%c", &c);
            if (c == '-') {
                data.push_back(false);
            }
            else if (c == '+') {
                data.push_back(true);
            }
            else {
                int spatula = 0;
                fscanf(file, "%d\n", &spatula);

                int result = solve(data, spatula);
                if (result >= 0) {
                    printf("Case #%d: %d\n", i + 1, result);
                }
                else {
                    printf("Case #%d: IMPOSSIBLE\n", i + 1);
                }
            }
        }
        while (c != ' ');
    }
    
    return 0;
}
