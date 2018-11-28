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
    freopen("/Users/andriymedvid/Desktop/GCJ-input/B-small-attempt0.in", "r", stdin);
    freopen("/Users/andriymedvid/Desktop/GCJ-answers/B-small-attempt0.out", "w", stdout);
    cin >> T;
    int n;
    int mas[101];
    int cmas[101];
    for(t = 0; t < T; t++) {
        cin >> n;
        for(int i = 0; i < n; i++) {
            cin >> mas[i];
            cmas[i] = mas[i];
        }
        sort(cmas, cmas+n);
        
        int Min = 10000;
        
        do {
            bool goDown = false;
            bool valid = true;
            for(int i = 0; i < n-1; i++) {
                if(cmas[i] > cmas[i+1]) {
                    goDown = true;
                } else if(goDown) {
                    valid = false;
                }
            }
            if(valid) {
                int res = 0;
                bool visited[11];
                for(int i = 0; i < n; i++)
                    visited[i] = false;
                for(int i = 0; i < n; i++) {
                    for(int j = 0; j < n; j++)
                        if(cmas[i] == mas[j]) {
                            visited[j] = true;
                            int k = 0;
                            for(int ii = 0; ii < j; ii++)
                                if(visited[ii])
                                    k++;
                            res += abs(j - k) + abs(i - k);
                            break;
                        }
                }
                Min = std::min(Min, res / 2);
            }
        } while(next_permutation(cmas, cmas+n));
        
        PPref();
        printf("%d\n", Min);
    }
    
}
