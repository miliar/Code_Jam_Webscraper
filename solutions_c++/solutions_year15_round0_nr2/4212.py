//
//  main.cpp
//  code_B
//
//  Created by yxfish13 on 15/4/11.
//  Copyright (c) 2015年 x-yu13. All rights reserved.
//

#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
int N;
int A[11000];
int main(int argc, const char * argv[]) {
    // insert code here...
    //std::cout << "Hello, World!\n";
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    int T,dt=0;
    cin>> T;
    while (T--){
        dt++;
        int S;cin>>S;
        for (int i=1;i<=S;i++) scanf("%d",&A[i]);
        int ans=100000;
        for (int i=1;i<=1000;i++){
            int now=0;
            for (int j=1;j<=S;j++)
                now+=(A[j]-1)/i;
            now+=i;
            if (ans>now) ans=now;
        }
        printf("Case #%d: %d\n",dt,ans);
    }
    return 0;
}
