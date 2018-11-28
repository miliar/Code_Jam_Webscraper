//
//  d.cpp
//  
//
//  Created by liumingming on 4/10/16.
//
//

#include <stdio.h>
#include <algorithm>
#include <iostream>
#include <string>
#include <cstring>
#include <string.h>
#include <set>
#include <map>

using namespace std;

int main(){
    //freopen("1.txt", "r",stdin);
    int t, s, c, k;
    scanf("%d", &t);
    for(int i = 0; i < t; ++i){
        scanf("%d%d%d", &k, &c, &s);
        printf("Case #%d: ", i+1);
        printf("1");
        for(int j = 1; j < s; ++j){
            printf(" %d", j + 1);
        }
        printf("\n");
    }
    
    return 0;
}
