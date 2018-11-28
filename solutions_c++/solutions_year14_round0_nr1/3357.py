//
//  main.cpp
//  GoogleCodeJam2014
//
//  Created by Shahab Uddin on 4/12/14.
//  Copyright (c) 2014 Shahab Uddin. All rights reserved.
//

#include <iostream>
#include <cstring>

void takeCardInput(int a [4] [4]) {

    for (int i = 0; i < 4; i++ ) {
        for ( int j = 0; j < 4; j++ ) {
            scanf ("%d", &a [i] [j]);
        }
    }
}

void verdict(int f [20], int c) {

    int foundTwo = 0;
    int num = 0;

    for ( int i = 0; i < 20; i++ ) {
        if (f [i] == 2) {
            foundTwo++;
            num = i;
        }
    }

    if (foundTwo == 1) {
        printf ("Case #%d: %d\n", c, num);
    } else if (foundTwo > 1) {
        printf ("Case #%d: Bad magician!\n", c);
    } else if (foundTwo == 0) {
        printf ("Case #%d: Volunteer cheated!\n", c);
    }
}

int main(int argc, const char * argv[])
{
    freopen("/Users/Shahab/Documents/Sourcecode/CPP/GoogleCodeJam2014/GoogleCodeJam2014/small_input.txt", "r", stdin);
    freopen("/Users/Shahab/Documents/Sourcecode/CPP/GoogleCodeJam2014/GoogleCodeJam2014/small_output.txt", "w", stdout);

    int testCases;

    scanf ("%d", &testCases);

    int cases = 1;

    while ( testCases-- ) {

        int firstChoice;

        scanf ("%d", &firstChoice);

        int firstArrangement [4] [4];

        takeCardInput(firstArrangement);

        int secondChoice;

        scanf ("%d", &secondChoice);

        int secondArrangement [4] [4];

        takeCardInput(secondArrangement);

        int freq [16 + 4];

        memset (freq, 0, sizeof freq);

        for ( int i = 0; i < 4; i++ ) {
            freq [firstArrangement [firstChoice - 1] [i]]++;
        }

        for ( int i = 0; i < 4; i++ ) {
            freq [secondArrangement [secondChoice - 1] [i]]++;
        }

        verdict(freq, cases);

        cases++;
    }

    return 0;
}


