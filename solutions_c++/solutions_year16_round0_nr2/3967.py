//
//  main.cpp
//  b
//
//  Created by LegaDyan on 16/4/9.
//  Copyright © 2016年 LegaDyan. All rights reserved.
//

#include <iostream>
#include <cstdio>

using namespace std;

int main(int argc, const char * argv[]) {
	freopen("b.in.txt", "r", stdin);
	freopen("b.txt", "w", stdout);
    int t;
    cin >> t;
    for (int i = 0; i < t; i++) {
        char s[1000];
        scanf("%s", s);
        int len = strlen(s);
        int num = 0;
        if (s[0] == '-') num++;
        for (int i = 1; i < len; i++)
            if (s[i - 1] == '+' && s[i] == '-') num+=2;
        printf("Case #%d: %d\n", i + 1, num);
    }
    return 0;
}
