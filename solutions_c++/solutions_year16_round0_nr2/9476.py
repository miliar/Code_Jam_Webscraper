//
//  QB.cpp
//  2016 Qualification Round Problem B
//
//  Created by meltaweel.
//  Copyright (c) 2016 meltaweel. All rights reserved.
//

#include <cstring>
#include <string.h>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>

using namespace std;

#define toDigit(c) (c-'0')

int T,i;


int main(int argc, char *args[]) {
    
    if (argc == 2 && strcmp(args[1], "small") == 0) {
        freopen("small.in","rt",stdin);
        freopen("small.out","wt",stdout);
    }
    else if (argc == 2 && strcmp(args[1], "large") == 0) {
        freopen("large.in","rt",stdin);
        freopen("large.out","wt",stdout);
    }
    else {
        freopen("test.in", "r", stdin);
        
    }
    
    cin>>T;
    
    
    int res;
    
    std:string stack;
    std::getline(std::cin,stack);
    for (i=1; i<T+1; i++) {
       
        
        std::getline(std::cin,stack);
        
            int shifts=0;
        
            for (int j= 0; j<stack.length();j++){
                if(j>0 && stack[j] != stack[j-1])
                    shifts++;
            }
        
        
            res = (stack[stack.length()-1] == '-')?shifts+1:shifts;
        
        
            printf("Case #%d: %d",i,res);
        
       
        
        cout<<endl;
        
    }
    
    
    return 0;
}


