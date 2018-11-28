//
//  C.cpp
//  gcj2016
//
//  Created by Qicai Shi on 4/9/16.
//  Copyright © 2016 Qicai Shi. All rights reserved.
//

#include <iostream>
#include <vector>
#include <string>
#include <math.h>
#include <algorithm>
using namespace std;
int prime(long long data) {
    for (int i = 2; i < sqrt(data) + 2; i ++) {
        if (data % i == 0)
            return i;
    }
    return 0;
}

string itobase2(int data) {
    string res;
    while (data != 0) {
        if (data % 2 == 0) {
            res.push_back('0');
        } else {
            res.push_back('1');
        }
        data /= 2;
    }
    reverse(res.begin(), res.end());
    return res;
}

int main(int argc, const char * argv[]) {
    //freopen("C-small-attempt0.in", "r", stdin);
    //freopen("C-small-attempt0.out", "w", stdout);
    int T;
    scanf("%d", &T);
    int N;
    int J;
    scanf("%d %d", &N, &J);
    printf("Case #1:\n");
    long long data;
    long long weight;
    vector<int> factor;
    int fact;
    int res;
    res = 50;
    int j;
    for (int i = 32769; i <= 65536 - 1; i += 2) {
        data = 0;
        factor.clear();
        for (int base = 2; base <= 10; base++) {
            j = i;
            weight = 1;
            data = 0;
            while (j != 0) {
                data += weight * (j % 2);
                j /= 2;
                weight *= base;
            }
            fact = prime(data);
            if (fact != 0) {
                factor.push_back(fact);
            } else {
                break;
            }
        }
        if (factor.size() == 9) {
            cout << itobase2(i);
            for ( int i = 0 ; i < 9; i++) {
                printf(" %d", factor[i]);
            }
            printf("\n");
            res--;
            if (res == 0) {
                break;
            }
        }
    }
    return 0;
}
