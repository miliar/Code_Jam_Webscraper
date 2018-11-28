//
//  main.cpp
//  Standing Ovation
//
//  Created by meltaweel on 4/11/15.
//  Copyright (c) 2015 meltaweel. All rights reserved.
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

int N;
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
    
    cin>>N;
    
    char line[1001];
    int i,j,max,stood,needed,si;
    
    for (i=1; i<N+1; i++) {
        
        cin>>max;
        cin>>line;
        
        stood = toDigit(line[0]);
        needed = 0;
        for(j=1;j<=max;j++){
            si =toDigit(line[j]);
            if(stood < j && si > 0 ){
                needed += j-stood;
                stood += j-stood;
            }
            stood+=si;
            
        }
                
        printf("Case #%d: %d", i, needed);
        cout<<endl;
    }
    
    return 0;
}


