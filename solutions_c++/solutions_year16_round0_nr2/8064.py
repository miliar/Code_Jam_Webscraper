//
//  0.cpp
//  0
//
//  Created by Apple on 3/12/16.
//  Copyright © 2016 ;. All rights reserved.
//

#include <algorithm>
#include <cmath>
#include <iostream>
#include <cstdio>
#include <vector>
#include <cstring>
#include <string>
#include <map>
#include <deque>
#include <queue>

using namespace std;

#define ll long long
#define maxn 100111
#define maxx 1000000000

char str[1111];

int main(){
//    freopen("inp.txt", "r", stdin);
//    freopen("out.txt","w",stdout);
    
    int ntest;
    scanf("%d\n",&ntest);
    for(int test=1;test<=ntest;test++){
        scanf("%s\n",str);
        int res = 0;
        for(int i=1;i<strlen(str);i++){
            if( str[i] != str[i-1])
                res++;
        }
        if( str[strlen(str)-1] == '-'){
            res++;
        }
        printf("Case #%d: %d\n",test,res);
    }
}