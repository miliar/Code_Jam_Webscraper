//
//  main.cpp
//  d
//
//  Created by LegaDyan on 16/4/9.
//  Copyright © 2016年 LegaDyan. All rights reserved.
//

#include <iostream>
using namespace std;

int main(int argc, const char * argv[]) {
    int t;
    scanf("%d", &t);
    for (int i = 0; i < t; i++) {
        int k, c, s;
        scanf("%d %d %d", &k, &c, &s);
        long long sum = 1;
        for (int j = 0; j < c - 1; j++) sum *= k;
        printf("Case #%d:", i + 1);
        for (int j = 0; j < k; j++) printf(" %lld", sum * j + 1);
        cout << endl;
    }
    return 0;
}
