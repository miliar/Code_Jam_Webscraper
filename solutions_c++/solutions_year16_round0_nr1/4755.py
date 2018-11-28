//
//  main.cpp
//  gcj2016
//
//  Created by Qicai Shi on 4/9/16.
//  Copyright © 2016 Qicai Shi. All rights reserved.
//

#include <iostream>
#include <vector>
using namespace std;
int main(int argc, const char * argv[]) {
    
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0.out", "w", stdout);
    int T;
    scanf("%d", &T);
    printf("%d", T);
    int n;
    vector<bool> digitMask(10, false);
    int tmpNum;
    int timer;
    int digitMeetCount;
    bool notEnough = true;
    for (int i = 1; i <= T; i++) {
        scanf("%d", &n);
        if (n == 0) {
            printf ("Case #%d: INSOMNIA\n", i);
            continue;
        }
        notEnough = true;
        digitMask.assign(10, false);
        timer = 0;
        digitMeetCount = 0;
        while (notEnough) {
            tmpNum = n * timer;
            while (tmpNum != 0) {
                if (digitMask[tmpNum % 10] == false){
                    digitMeetCount++;
                    digitMask[tmpNum % 10] = true;
                }
                tmpNum /= 10;
            }
            if (digitMeetCount == 10) {
                break;
            }
            timer++;
        }
        printf("Case #%d: %d\n", i, timer * n);
    }
    return 0;
}
