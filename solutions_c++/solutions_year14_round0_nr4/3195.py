//
//  main.cpp
//  GoogleCodeJam2014
//
//  Created by Shahab Uddin on 4/12/14.
//  Copyright (c) 2014 Shahab Uddin. All rights reserved.
//

#include <iostream>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <cstdio>
#include <map>

using namespace std;

int naomi [1000 + 10];
int ken [1000 + 10];
int n;
map<int, bool> kenMap;
map<int, bool> naomiMap;

void makeKenMap();

bool canKenCapture(int num);

void eliminate()
{
    for ( int i = n - 1; i >= 0; i-- ) {
        if (kenMap [ken [i]]) {
            kenMap [ken [i]] = false;
            break;
        }
    }
}

void makeNaomiMap()
{
    for ( int i = 0; i < n; i++ ) {
        naomiMap [naomi [i]] = true;
    }
}

bool canNaomiCapture(int num)
{
    for ( int i = n - 1; i >= 0; i-- ) {
        if (kenMap [ken [i]] && ken [i] < num) {
            kenMap [ken [i]] = false;
            return true;
        }
    }

    return false;
}

int deceitfulWar()
{
    kenMap.clear();

    makeKenMap();

    makeNaomiMap();

    int ret = 0;

    for ( int i = n - 1; i >= 0; i-- ) {

        if (naomiMap [naomi [i]]) {
            if (canNaomiCapture(naomi [i])) {
                naomiMap [naomi [i]] = false;
                ret++;
            } else {

                for ( int j = 0; j < n; j++ ) {
                    if (naomiMap [naomi [j]]) {
                        naomiMap [naomi [j]] = false;
                        eliminate();
                        break;
                    }
                }

            }
        }
    }

    return ret;

}

void makeKenMap()
{
    for ( int i = 0; i < n; i++ ) {
        kenMap [ken [i]] = true;
    }
}

bool canKenCapture(int num)
{
    for ( int i = 0; i < n; i++ ) {
        if (num < ken [i] && kenMap [ken [i]]) {
            kenMap [ken [i]] = false;
            return true;
        }
    }

    return false;

}

int war()
{
    makeKenMap();

    int ret = 0;

    for ( int i = 0; i < n; i++ ) {
        if (!canKenCapture(naomi [i])) ret++;
    }


    return ret;

}

int main(int argc, const char * argv[])
{
    freopen("/Users/Shahab/Documents/Sourcecode/CPP/GoogleCodeJam2014/GoogleCodeJam2014/Deceitful_War/large_input.txt", "r", stdin);
    freopen("/Users/Shahab/Documents/Sourcecode/CPP/GoogleCodeJam2014/GoogleCodeJam2014/Deceitful_War/large_output.txt", "w", stdout);

    int testCases;

    scanf ("%d", &testCases);

    int cases = 0;

    while ( testCases-- ) {

        scanf ("%d", &n);

        char inp [20];

        for ( int i = 0; i < n; i++ ) {
            scanf ("%s", inp);
            sscanf(inp, "0.%d", &naomi [i]);
        }

        for ( int i = 0; i < n; i++ ) {
            scanf ("%s", inp);
            sscanf(inp, "0.%d", &ken [i]);
        }

        sort(naomi, naomi + n);
        sort(ken, ken + n);

        printf ("Case #%d: %d %d\n", ++cases, deceitfulWar(), war());

    }

    return 0;
}


