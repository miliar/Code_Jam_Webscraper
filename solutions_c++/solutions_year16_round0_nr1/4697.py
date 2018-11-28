//
//  GCJQA.cpp
//  playground
//
//  Created by 張正昊 on 9/4/2016.
//  Copyright © 2016 Adam Chang. All rights reserved.
//

#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <queue>
#include <vector>
#include <cstdlib>
#include <cstdio>
#include <string>
#include <cstring>
#include <ctime>
#include <iomanip>
#include <cmath>
#include <set>
#include <stack>
#include <cmath>
#include <map>
#include <complex>

using namespace std;

bool mkr[10];
bool check(){
    for(int i = 0; i <= 9; i++){
        if(!mkr[i]) return false;
    }
    return true;
}
void arrange(long long a){
    while (a) {
        mkr[a%10] |= 1;
        a /= 10;
    }
}

int main(){
    int caseCnt;
    scanf(" %d",&caseCnt);
    for(int d = 1;d <= caseCnt;d++){
        long long n;
        printf("Case #%d: ",d);
        scanf(" %lld",&n);
        if(n == 0){
            puts("INSOMNIA");
        }else{
            memset(mkr, false, sizeof(mkr));
            long long cur = n;
            arrange(cur);
            while (!check()) {
                cur += n;
                arrange(cur);
            }
            printf("%lld\n",cur);
        }
        
    }
    return 0;
}
