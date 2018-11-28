//
//  main.cpp
//  GCJ14_R2_B
//
//  Created by Ningchen Ying on 5/31/14.
//  Copyright (c) 2014 Ningchen Ying. All rights reserved.
//

#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <vector>
using namespace std;
int a[100100];


int main(int argc, const char * argv[])
{
    int T;
    //freopen("/Users/YNingC/Documents/CodeForces/GCJ14_R2_B/GCJ14_R2_B/B-small-attempt1.in","r",stdin);
    //freopen("/Users/YNingC/Documents/CodeForces/GCJ14_R2_B/GCJ14_R2_B/B-small-attempt1.out","w", stdout);
    freopen("/Users/YNingC/Documents/CodeForces/GCJ14_R2_B/GCJ14_R2_B/B-large.in","r",stdin);
    freopen("/Users/YNingC/Documents/CodeForces/GCJ14_R2_B/GCJ14_R2_B/B-large.out","w", stdout);
    cin>>T;
    for (int ca = 1; ca <= T; ca++){
        int N;
        cin>>N;
        for (int i = 0;i< N;i++){
            cin>>a[i];
        }
        int L = 0, R = N;
        int ans = 0;
        //binary search
        while(L<R){
            int mini = a[L];
            //mid
            int id = L;
            for (int i = L; i<R; i++){
                if (a[i]<mini){
                    mini = a[i];
                    id = i;
                }
            }
            if (id-L < R-id-1){
                for (int i = id; i>L; i--){
                    ans++;
                    swap(a[i], a[i-1]);
                }
                L++;
            }else {
                for (int i = id; i+1<R; i++){
                    ans++;
                    swap(a[i],a[i+1]);
                }
                R--;
            }
        }
        printf("Case #%d: %d\n",ca, ans);
    }
    return 0;
}


