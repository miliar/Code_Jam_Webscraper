//
//  main.cpp
//  GCJ-2-b
//
//  Created by Andriy Medvid' on 31.05.14.
//  Copyright (c) 2014 Andriy Medvid'. All rights reserved.
//

#include <iostream>
#include <cmath>
#include <cstring>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

int T, t;

void PPref() {
    printf("Case #%d: ", t+1);
}

int main(int argc, const char * argv[])
{
    freopen("/Users/andriymedvid/Desktop/GCJ-input/A-large.in", "r", stdin);
    freopen("/Users/andriymedvid/Desktop/GCJ-answers/A-large.out", "w", stdout);
    cin >> T;
    int n, x;
    int mas[10010];
    for(t = 0; t < T; t++) {
        cin >> n >> x;
        for(int i = 0; i < n; i++)
            cin >> mas[i];
        sort(mas, mas+n);
        int k = 0;
        int beg = 0, end = n-1;
        while(beg < end) {
            while(mas[beg] + mas[end] > x && beg < end)
                end--;
            if(beg < end) {
                k++;
            }
            beg++;
            end--;
        }
        PPref();
        printf("%d\n", n-k);
    }
    
}
