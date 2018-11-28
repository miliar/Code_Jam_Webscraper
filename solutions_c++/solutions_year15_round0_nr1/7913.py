//
//  main.cpp
//  qqq
//
//  Created by Misha Babenko on 4/1/15.
//  Copyright (c) 2015 Misha Babenko. All rights reserved.
//

#include <iostream>
#include <vector>
#include <algorithm>
#include <set>

using namespace std;

const int MaxS = 1e3;

char peopleWithShyness[MaxS + 2];

bool allStand(int sz, int friends) {
    int curStand = friends;
    for (int i = 0; i <= sz; i++) {
        int curPeople = peopleWithShyness[i] - '0';
        if (curPeople == 0)
            continue;
        if (curStand >= i)
            curStand += curPeople;
        else
            return false;
    }
    return true;
}

int main(int argc, const char * argv[]) {
    freopen ("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t;
    scanf ("%d", &t);
    for (int test = 0; test < t; test++) {
        printf ("Case #%d: ", test + 1);
        int sMax = 0;
        scanf ("%d %s", &sMax, peopleWithShyness);
        if (allStand(sMax, 0))
            printf ("0\n");
        else {
            int l = 0, r = 1001;
            while (l < r - 1) {
                int mid = (l + r) / 2;
                if (allStand(sMax, mid))
                    r = mid;
                else
                    l = mid;
            }
            printf ("%d\n", r);
        }
    }
    return 0;
}
