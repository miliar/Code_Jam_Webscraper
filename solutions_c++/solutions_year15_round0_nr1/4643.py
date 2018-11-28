//
//  main.cpp
//  StandingOvation
//
//  Created by Michael Walker on 4/10/15.
//  Copyright (c) 2015 Michael Walker. All rights reserved.
//

#include <iostream>
#include <fstream>

int main(int argc, const char * argv[]) {
    int T = 3;
    int S[2000];
    int count = 1;
    int max;
    int invite;
    int sum;
    int tracker;
    freopen("/Users/Michael/Desktop/A-large.in", "r", stdin);
    std::ofstream out("/Users/Michael/Desktop/output");
    scanf("%i", &T);
    while (T--) {
        tracker = 0;
        invite = 0;
        sum = 0;
        out << "Case #" << count << ": ";
        scanf("%i", &max);
        for (int i = 0; i < max + 1; i++) {
            scanf("%1i", &S[i]);
        }
        for (int i = 0; i < max + 1; i++) {
            if (S[i] == 0) {
                tracker++;
            }
        }
        if (tracker == 0) {
            out << 0 << "\n";
        }
        else {
            for (int i = 0; i < max + 1; i++) {
                sum += S[i];
                while (sum < i + 1) {
                    invite++;
                    sum++;
                }
            }
            out << invite << "\n";
        }
        
        count++;
    }
    out.close();
    return 0;
}
