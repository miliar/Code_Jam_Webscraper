//
//  main.cpp
//  GoogleCodeJam2016
//
//  Created by BlueCocoa on 16/4/9.
//  Copyright © 2016年 BlueCocoa. All rights reserved.
//

#include <iostream>

using namespace std;

#pragma mark
#pragma mark - Google Code Jam 2016 Problem B

#define HAPPYSIDE '+'
#define BLANKSIDE '-'

char cakes[128] = { 0 };

long long filp_cakes() {
    int pos = 0;
    long long filps = 0;
    char next_side = cakes[0];
    char current_side = cakes[0];
    size_t len = strlen(cakes);
    while (cakes[pos]) {
        while (pos < len && (next_side = cakes[++pos]) == current_side);
        if (next_side != '\0') {
            filps++;
            current_side = next_side;
        } else {
            if (current_side == BLANKSIDE) {
                filps++;
                current_side = HAPPYSIDE;
            }
        }
    }
    return filps;
}

int main(int argc, const char * argv[]) {
    long long total, current = 0;;
    cin>>total;
    while ((current++) != total) {
        bzero(cakes, sizeof(char) * 128);
        cin>>cakes;
        cout<<"Case #"<<current<<": "<<filp_cakes()<<'\n';
    }
    return 0;
}
