//
//  bb.cpp
//  LeetCode
//
//  Created by chushumo on 5/3/14.
//  Copyright (c) 2014 Chu Shumo. All rights reserved.
//

#include <iostream>
#include <vector>
#include <stack>
#include <cstdlib>

using namespace std;

void small(){
    int num_case;
    scanf("%d",&num_case);
    for (int i=0;i<num_case; ++i) {
        int a,b,k;
        scanf("%d %d %d",&a,&b,&k);
        long counter = 0;
        for (int m=0;m<a;m++) {
            for(int n=0; n<b; n++){
                int r = m&n;
                if(r<k && r>=0){
                    counter++;
                }
            }
        }
        printf("Case #%d: %ld\n",i+1,counter);
    }
}
int main(){
    small();
}
