//
//  main.cpp
//  gcj4
//
//  Created by Lewnus on 15/4/11.
//  Copyright (c) 2015年 Lewnus. All rights reserved.
//

#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;

int T,n,x,r,c;

bool calc(int x,int r,int c){
    if (r*c%x) return 0;
    if (x>=7) return 0;
    if (x>2&&min(r,c)<=x-2) return 0;
    return 1;
}

int main(int argc, const char * argv[]) {
    freopen("../../../../../../../../Documents/sw_cpp/sf/gcj4/gcj4/1.in","r",stdin);
    freopen("../../../../../../../../Documents/sw_cpp/sf/gcj4/gcj4/1.out","w",stdout);
    scanf("%d",&T);
    for (int i=1;i<=T;i++){
        scanf("%d%d%d",&x,&r,&c);
        if (calc(x,r,c)) printf("Case #%d: GABRIEL\n",i);
        else  printf("Case #%d: RICHARD\n",i);
    }
}
