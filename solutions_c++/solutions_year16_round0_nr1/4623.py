//
//  main.cpp
//  GoogleCodeJam2016
//
//  Created by BlueCocoa on 16/4/9.
//  Copyright © 2016年 BlueCocoa. All rights reserved.
//

#include <iostream>

using namespace std;

const int INSOMNIA = -1;
unsigned char buffer[256] = { 0 };
unsigned short digits = 0;

#define SHORT_BIT_LOG 4
#define MASK (~(~0 << SHORT_BIT_LOG))
#define setbit(a, x) ((a)[(x) >> SHORT_BIT_LOG] |= 1 << ((x) & MASK))
#define isset(a, x) ((a)[(x) >> SHORT_BIT_LOG] & (1 << ((x) & MASK)))

long long bleatrix(long long N, int times = 1) {
    if (N == 0) {
        return INSOMNIA;
    }
    long long current = N * times;
    bzero(buffer, sizeof(unsigned char) * 256);
    sprintf((char *)buffer, "%lld", current);
    for (int i = 0; buffer[i] != '\0'; i++) {
        setbit(&digits, (unsigned int)buffer[i] - '0');
        if (digits == 1023) {
            digits= 0;
            return current;
        }
    }
    return bleatrix(N, times + 1);
}

int main(int argc, const char * argv[]) {
    long long N, total, current = 0;
    cin>>total;
    while ((current++) != total) {
        cin>>N;
        N = bleatrix(N);
        if (N == -1) {
            cout<<"Case #"<<current<<": INSOMNIA"<<'\n';
        } else {
            cout<<"Case #"<<current<<": "<<N<<'\n';
        }
    }
    return 0;
}
